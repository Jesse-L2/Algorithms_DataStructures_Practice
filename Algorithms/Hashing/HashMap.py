# Credit - neetcode for the python
#           Tree Map    Hash Map* (*average case, could actually be O(n) worst case, but that is not convention)
# Insert    O(log n)    O(1)
# Remove    O(log n)    O(1)
# Search    O(log n)    O(1)
# Inorder   O(n)        O(n) 

# Creating a hash map
countMap = {}
arr = [] * 10 # hypothetical array of elements to add
for name in arr:
    if not name in arr:
        countMap[name] = 1
    else:
        countMap[name] += 1

class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashMap:
    def __init__(self):
        self.size = 0 # initial number of keys
        self.capacity = 2
        self.map = [None, None] # map maintained as an array
    def hash(self, key):
        index = 0
        for char in key:
            index += ord(char)
        return index % self.capacity
    # A hash function takes a key and converts it to an integer. The integer is the index that the key-value pair is stored in the array. The same string will always return the same integer because of the hash function. This can mean some keys would be stored where another key should be stored (collision).
    # collisions can be minimized with Chaining (storing like a linked list) and Open Addressing (finding the next available slot). Chaining is generally preferable. 
    def get(self, key):
        index = self.hash(key)

        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity # will always give a valid index
        return None # can also return an exception

    def put(self, key, val):
        index = self.hask(key)
        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key, val)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif self.map[index].key == key:
                self.map[index].val = val
                return
            index += 1
            index = index % self.capacity
            
    def remove(self, key):
        if not self.get(key):
            return
        index = self.hash(key)
        while True:
            if self.map[index].key == key:
                # Stop search if find hole in list
                self.map[index] = None
                self.size -= 1
                return
            index += 1
            index = index % self.capacity

    def rehash(self): # go through every key in hash map and reassign them to new positions
        self.capacity = 2 * self.capacity
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)

        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.put(pair.key, pair.val)

    def print(self):
        for pair in self.map:
            if pair:
                print(f"({pair.key}, {pair.val})")

