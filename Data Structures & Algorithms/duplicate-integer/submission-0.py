class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = {} #probably a suggestive name lol
        for i in range(len(nums)): 
            cur = myDict.get(nums[i],0)
            if cur != 0: 
                return True 
            else:
                myDict[nums[i]] = cur+1
        return False