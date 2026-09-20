class Solution:

    def encode(self, strs: List[str]) -> str:
        # could come up with a ticker for how many time it wraps when shifting - but then youre doing a delimter anyway 
        #so a asmarter way of doing it is to make the delimtiter to start,a nd then just block off 8 byte chunks of digits, or use underscores or something 
        outputStr = ""
        for curStr in strs:
            lenOfStr = len(curStr)
            outputStr += f"-{lenOfStr}-"
            for curChar in curStr:
                valOfChar = ord(curChar)
                outputStr += str(valOfChar)
                outputStr += "_"
            print(outputStr)
                
        print(outputStr)
        return outputStr

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s)-1:
            curChar = s[i]
            if curChar == "-":
                #know that we need to then read the delimter
                #only read the delimiter
                i+=1 
                lengthToReadStr = "" 
                while s[i] != "-":
                    lengthToReadStr += s[i]
                    i+=1
                lengthToRead = int(lengthToReadStr)
                if int(lengthToRead) == 0:
                    print(s[i:])
                    i+=1
                    output.append("")
                    continue
                print(curChar)

                print("length_to_read", lengthToRead)

                #this is the delimiter
                curChar = s[i]
                print(curChar)
                #clears the next dash 
                #this is the start of the string
                i+=1
                curChar = s[i]
                print(curChar)
                curString = ""
                while curChar != "-" and i < len(s)-1:
                    # sub reading expression 
                    print("remaining bit of String", s[i:])
                    print("entering sub expression")
                    outChar = ""
                    while curChar != "_" and i <len(s)-1:
                        print("curChar" , curChar)
                        outChar += s[i]
                        i+=1
                        curChar = s[i]
                    #this is now a value of int that we want to turn into string/char
                    print("outchar", outChar)
                    curString+=chr(int(outChar))
                    if not (i == len(s)-1):
                        i+=1
                        curChar = s[i]
                
                output.append(curString)
                print(curString)
                print("end of string curChar", curChar)
            print(output)
        return output 