class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket_array = [[] for _ in range(len(nums)+1)]
        # why can't you do [[] * len(nums)]
        my_dict = {}
        top_k = []
        counter = 0
        for i in range(len(nums)): 
            cur = my_dict.get(nums[i],0)
            my_dict[nums[i]] = cur+1
        print(my_dict)
        for j in my_dict.keys(): 
            print(j)
            frequency = my_dict[j]
            print(frequency)
            bucket_array[frequency].append(j)
        print(bucket_array)
        kCounter = 0 
        ret = []
        for l in range(len(nums),-1,-1):
            #iterate in reverse 
            # print(bucket_array[l])
            if bucket_array[l] and kCounter < k:
                for p in bucket_array[l]:
                    if kCounter < k:
                        ret.append(p)
                        kCounter+=1
        return ret