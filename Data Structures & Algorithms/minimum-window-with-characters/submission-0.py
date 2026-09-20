class Solution:
    def minWindow(self, s: str, t: str) -> str:
        substring = ""
        if len(s) < len(t): 
            return substring
        shortest = float('inf')
        l = 0
        r = 0
        tCount = {}
        for ch in t:
            tCount[ch] = tCount.get(ch,0) + 1 
        print(tCount)
        while r < len(s):
            is_subset = True
            print(s[l:r+1])
            #fills count
            subCount = {}
            for ch in s[l:r+1]: 
                subCount[ch] = subCount.get(ch,0) + 1
            #can't compare hashmaps directly, have to see if they ahve the same values
            for i in tCount.keys():
                if tCount[i] > subCount.get(i,0):
                    is_subset = False 
                

            if is_subset:
                #shrink the window as much as we can
                while is_subset: 
                    subCount[s[l]] = subCount[s[l]] -1
                    print(subCount)
                    if subCount[s[l]] == 0: 
                        del subCount[s[l]]
                        #remove the key
                    for i in tCount.keys():
                        if tCount[i] > subCount.get(i,0):
                            is_subset = False 
                    l+=1
                    
                print(subCount) 
                # print("l", l ," r", r)
            
                #then add most recent(that tripped it) back
                l-=1
                # print("l", l ," r", r)

                subCount[s[l]] = subCount.get(s[l],0) + 1
                windowlen = r-l + 1
                curSubstring = s[l:r+1]
                # print(subCount) 
                # print(windowlen)
                # print(curSubstring)

                if windowlen < shortest: 
                    shortest = windowlen
                    substring = curSubstring
                #advance l
                l+=1
                # print("cursubstring", curSubstring) 
                # print("l", l ," r", r)
            else: 
                r+=1
        return substring