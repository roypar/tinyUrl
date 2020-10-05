import json5


class TinyUrl:
    instance = None

    def __init__(self, dbName):
        if TinyUrl.instance is not None:
            raise Exception('Singleton instance already exists')
        else:
            try:
                fp = open(dbName, 'r')
                data = json5.load(fp)
                print('Initializing instance from Db')
                self.dbName = dbName
                self.dbSize = data['dbSize']
                self.nextHash = data['nextHash']
                self.entries = data['entries']
            except FileNotFoundError:
                print('Db Does not exist. Initializing empty instance')
                self.dbName = dbName
                self.dbSize = 100
                self.nextHash = 0
                self.entries = {}

            TinyUrl.instance = self

    @classmethod
    def getInstance(cls):
        return cls.instance

    def setDbSize(self, size):
        if size < len(self.entries):
            raise Exception('Size setting will lead to data loss')
        else:
            self.dbSize = size

    def getDbSize(self):
        return self.dbSize

    def getRemovableItem(self):
        temp_key = list(self.entries.keys())[0]
        min_score = self.entries[temp_key]['rank'] + self.entries[temp_key]['hits']
        for key in self.entries.keys():
            entry_score = self.entries[key]['rank'] + self.entries[key]['hits']
            if entry_score < min_score:
                min_score = entry_score
                temp_key = key

        return temp_key

    def deleteEntry(self, smallUrl):
        if smallUrl in self.entries.keys():
            del self.entries[smallUrl]

    def makeNewEntry(self, url):
        for key_url in self.entries.keys():
            if self.entries[key_url]['original'] == url:
                return key_url

        if len(self.entries) >= self.getDbSize():
            key_to_del = self.getRemovableItem()
            self.deleteEntry(key_to_del)

        key = f'tinyUrl{self.nextHash}'
        value = {'original': url, 'hits': 0, 'rank': self.nextHash}
        self.entries[key] = value
        self.nextHash += 1
        return key

    def fetchOriginal(self, smallUrl):
        if smallUrl in self.entries.keys():
            tempDict = self.entries[smallUrl]
            tempDict['hits'] += 1
            return tempDict['original']
        else:
            return 'NA'

    def saveInDb(self):
        data = {'dbName': self.dbName, 'dbSize': self.dbSize, 'nextHash': self.nextHash, 'entries': self.entries}
        with open(self.dbName, 'w') as fp:
            json5.dump(data, fp)
