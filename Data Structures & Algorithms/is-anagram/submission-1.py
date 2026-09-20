class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        numZeros = 0
        myDict = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            curS = myDict.get(s[i] , 0)

            myDict[s[i]] = curS+1

            curT = myDict.get(t[i],0)
            myDict[t[i]] = curT -1
        for j in range(len(t)):
            cur = myDict.get(s[j])
            if cur == 0:
                numZeros+=1
            else:
                return False

        if numZeros == len(s): 
            return True
        return False