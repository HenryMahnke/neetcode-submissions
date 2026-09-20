class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #we should be able to do this in O(n) time and O(n) space  
        """i think what we want to do is some type of make a dict of len n where all values are the target, then 
        we can subtract the current and then we could look it up"""
        myDict = {} 
        for i in range(len(nums)): 
            diff = target - nums[i]
            cur = nums[i]
            if cur in myDict: 
                return [myDict[cur], i]
            else: 
                myDict[diff] = i
        return None