class Solution:

    def encode(self, strs: List[str]) -> str:
        outputStr = ""
        for curStr in strs:
            outputStr += str(len(curStr))
            outputStr += ":"
            outputStr += curStr
        print(outputStr)
        return outputStr

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            print(i)
            curString = ""
            lenStr = ""
            while s[i] != ":":
                lenStr += s[i]
                i += 1
            i += 1
            length = int(lenStr)
            for j in range(length):
                print("cur value", s[i])
                curString += s[i]
                i += 1
            output.append(curString)
        return output