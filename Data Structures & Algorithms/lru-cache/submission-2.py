class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.cache =  {}
        self.get_called = 0
    def get(self, key: int) -> int:
        # default
        self.get_called +=1
        val = self.cache.get(key,(-1,-1))
        if val[0] != -1:
            self.cache[key] = (val[0], self.get_called)
        print(self.cache)
        return val[0]

    def put(self, key: int, value: int) -> None:
        self.get_called +=1
        val = self.cache.get(key,(-1,0))
        if val[0] != -1:
            self.cache[key] = (value,self.get_called)
            return
        if self.length < self.capacity: 
            self.length+=1
            if val[0] == -1:
                # never been called
                self.cache[key] = (value, self.get_called)
        # else evict 
        else: 
            # search to smallest "get called" value
            min_key = ""
            min_called = float('inf')
            for ind, i in enumerate(self.cache):
                val = self.cache.get(i,0)
                called_val = val[1]
                # print("called_val:", called_val) 
                # print(i)
                if called_val < min_called:
                    min_called = called_val 
                    min_key = i
            # then evict the min key and put in the new key 
            # print(min_key)
            # print(self.cache)
            self.cache.pop(min_key)
            self.cache[key] = (value,self.get_called)
        print(self.cache)


