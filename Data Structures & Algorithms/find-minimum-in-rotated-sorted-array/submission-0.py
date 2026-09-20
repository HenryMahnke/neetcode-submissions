class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums)-1 
        while l < r: 
            m = (l+r)//2 
            if nums[r] > nums[m]: #know m is past pivot
                r = m 
            else:  #nums[r] < nums[m]
                l =m+1
            print("m ", m, "l " , l, "r ", r) 
        print("l",l,"r",r)
        return nums[l]
            
        