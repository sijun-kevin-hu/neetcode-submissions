class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            if self.isDuplicate(board[i]):
                return False

            col = []
            for j in range(len(board[i])):
                col.append(board[j][i])
                if self.isDuplicate(col):
                    return False

                box_row = (i // 3) * 3
                box_col = (j // 3) * 3
                matrix = []
                for l in range(box_row, box_row + 3, 1):
                    for k in range(box_col, box_col + 3, 1):
                        matrix.append(board[l][k])
                if self.isDuplicate(matrix):
                    return False
                    
        return True


    def isDuplicate(self, row):
        c_set = set()
        for c in row:
            if c == '.':
                continue

            if c in c_set:
                return True
            else:
                c_set.add(c)
        return False
            