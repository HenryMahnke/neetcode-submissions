class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictArray = []
        indexArray = []
        outputStrs = []
        for i in range(len(strs)):
            curDict = {}
            for j in range(len(strs[i])):
                curVal = curDict.get(strs[i][j],0) 
                curDict[strs[i][j]] = curVal + 1
            print(curDict)
            if not dictArray:
                dictArray.append([curDict])
                indexArray.append([i])
                outputStrs.append([strs[i]])

            else:
                added = False
                for k in range(len(dictArray)): #exclusive of i
                    print("test")
                    print(dictArray[k])
                    if curDict == dictArray[k][0]:
                        dictArray[k].append([curDict])
                        indexArray[k].append(i) #the i'th index is what we are currently indexing through
                        outputStrs[k].append(strs[i])
                        added = True
                if not added:
                    indexArray.append([i])
                    outputStrs.append([strs[i]])
                    dictArray.append([curDict])
        return outputStrs