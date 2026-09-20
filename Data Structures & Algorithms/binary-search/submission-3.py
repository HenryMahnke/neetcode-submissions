class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        m = r//2
        while True:
            if nums[m] < target:
                l = m
                m = (r+l)//2
                if m == l: 
                    break
            elif nums[m] > target:
                r = m 
                m = (r+l)//2
                if m == r: 
                    break
            else: 
                return m
        return -1
        