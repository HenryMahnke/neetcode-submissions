class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            #check the rows
        for row in board: 
            rowHash ={}
            for elemInRow in row: 
                curVal= rowHash.get(elemInRow, 0)
                if elemInRow == '.':
                    continue
                if curVal != 0 or not int(elemInRow) <10 or not int(elemInRow) > 0: 
                    return False 
                else: 
                    # print(elemInRow)
                    rowHash[elemInRow] = curVal + 1
        #check the columns
        transposed_array = [list(row) for row in zip(*board)]    
        #check the cols  
        for col in transposed_array:
            colHash ={}
            for elemInCol in col: 
                curVal= colHash.get(elemInCol, 0)
                if elemInCol == ".":
                    continue
                if curVal != 0 or not int(elemInCol) <10 or not int(elemInCol) > 0: 
                    return False 
                else: 
                    colHash[elemInCol] = curVal + 1
        #now check the boxes 
        #tempted to flatten the board ^^ would make above operations better 
        flattened = []
        for row in board: 
            flattened.extend(row)
            #maybe need *
        for curBoxRow in range(3):
            for curBoxCol in range(3):
                boxHash = {}
                boxStart = 27 * curBoxRow + 3*curBoxCol
                # print(boxStart)
                for i in range(3): 
                    for j in range(3): 
                        curEl = flattened[boxStart+9*i+j]
                        curVal  = boxHash.get(curEl,0) 
                        if curEl == ".": 
                            continue
                        if curVal != 0: 
                            return False
                        boxHash[curEl] = curVal + 1
        return True