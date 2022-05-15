class HashItem: 
    def __init__(self, key, value): 
        self.key = key 
        self.value = value

class HashTable: 
    def __init__(self): 
        self.size = 10
        self.slots = [None for i in range(self.size)] 
        self.count = 0 

    def hashfunction(self,key):
        # Insert your hashing function code
        keystr = str(key)
        hashVal = 0
        for ch in keystr:
            hashVal += ord(ch)
        return (hashVal * len(keystr)) % self.size
    def rehash(self,key):
        # Insert your secondary hashing function code
        keystr = str(key)
        hashVal = 0
        counter = 0
        for ch in str(keystr):
            counter += 1
            hashVal += ord(ch) + counter
        return (hashVal * len(keystr)) % self.size
    def put(self,key,value):
        # Insert your code here to store key and data
        item = HashItem(key, value)
        h = self.hashfunction(key)
        while self.slots[h] is not None: 
            if self.slots[h].key is key: 
                break 
        h = (h + 1) % self.size
        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = item
        
    def get(self,key):
        # Insert your code here to get data by key
        h = self.hashfunction(key)
        while self.slots[h] is not None: 
            if self.slots[h].key is key: 
                return self.slots[h].value 
            h = (h+ 1) % self.size
        
    def __getitem__ (self,key):
        return self.get(key)

    def __getitem__(self, key): 
        return self.get(key)


ht = HashTable()

ht.put('69', 'A')
ht.put('66', 'B')
ht.put('80', 'C')
ht.put('35', 'D')
ht.put('18', 'E')
ht.put('52', 'F')
ht.put('82', 'G')
ht.put('70', 'H')
ht.put('12', 'I')
# print the slot values
for key in ('69','66','80','35','18','52','82','70','12'):
    v = ht.get(key)
    print(v)
# print the data values

# print the value for key 52
