class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        biggerDict = {}
        outputStrs = []
        for i in range(len(strs)): #this runs m times 
            curArray = [0] * 26
            for j in range(len(strs[i])): #this runs n times
                # get the value that we want it to be in the array
                index = ord(strs[i][j]) - ord('a')
            
                curArray[index] +=1
            key = tuple(curArray)
            if key not in biggerDict:
                biggerDict[key] = [strs[i]]
            else: 
                biggerDict[key].append(strs[i])
        # print(biggerDict)
        for k in biggerDict:
            outputStrs.append(biggerDict[k])
        return outputStrs