class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #must use O(1) additional space 
        #alright, so this is a two pointer question 
        #but we have to think through how we should go about it 
        #if we start at the beginning and the end. 
        #if the value is more we know to move right right pointer down 
        #if its less we move the left pointer up. Is it not that easy? 
        l = 0
        r = len(numbers) -1
        while l < r: 
            if numbers[l]+numbers[r] < target: 
                l+=1 
            elif numbers[l]+numbers[r] > target:
                r-=1
            else: 
                break
            print(numbers[l]+numbers[r])
        output = [l+1,r+1]
        return output