class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        nums = sorted(nums)
        for ind, cur in enumerate(nums): 
            l=0
            r = len(nums)-1
            while l < r: 
                if l == ind:
                    l+=1
                    break
                if r == ind: 
                    r -=1
                    break
                val = cur + nums[l] + nums[r]
                if val ==0: 
                    tup = tuple([cur,nums[l],nums[r]])
                    if tup not in res:
                        res.append(tup) 
                    r-=1
                    l+=1
                elif val < 0: 
                    l+=1
                else: 
                    r-=1
        return res

                