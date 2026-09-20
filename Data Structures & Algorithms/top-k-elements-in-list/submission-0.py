class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        for i in range(len(nums)):
            cur = myDict.get(nums[i],0)
            myDict[nums[i]] = cur +1
        #to be honest i don't know how to sort a dict by its values in python 
        sorted_dict = dict(sorted(myDict.items(), key = lambda item: item[1],reverse= True))
        print(sorted_dict)
        ret = []
        for i in range(k):
            print(list(sorted_dict.keys()))
            ret.append(list(sorted_dict.keys())[i])
        return ret