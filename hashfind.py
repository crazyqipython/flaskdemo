#coding:utf-8
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    #put data in slot
    def put_data_in_slot(self,key,data,slot):
        if self.slots[slot] == None: # '==None' ? or  'is None' ?
            self.slots[slot] = key
            self.data[slot] = data
            return True
        else:
            if self.slots[slot] == key: # not None
                self.data[slot] = data #replace
                return True
            else:
                return False

    def put(self, key, data):
        slot = self.hash_function(key, self.size);#调用hash_function
        result = self.put_data_in_slot(key,data,slot);#调用put_data_in_slot
        while not result:
            slot = self.rehash(slot, self.size);#调用rehash
            result=self.put_data_in_slot(key,data,slot);#调用put_data_in_slot

    #reminder method
    def hash_function(self, key, size):
        return key % size

    #plus 1
    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):#查找值
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True#查找失败
        return data

    def __getitem__(self, key):#重构获取值方法
        return self.get(key)

    def __setitem__(self, key, data):#重构存值方法
        self.put(key, data)

#key和槽的对应关系，槽和数值的对应关系。
if __name__=='__main__':
    
    table=HashTable();
    table[54]='cat';
    table[26]='dog';
    table[93]='lion';
    table[17]="tiger";
    table[77]="bird";
    table[44]="goat";
    table[55]="pig";
    table[20]="chicken";
    print table.slots;
    print table.data;
    print table[93]
    print table[94]
