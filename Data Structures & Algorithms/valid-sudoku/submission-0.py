class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for col_ind in range(len(board)):
            col = []
            if self.isDuplicateRow(board[col_ind]):
                return False

            for row_ind in range(len(board[col_ind])):
                col.append(board[row_ind][col_ind])

            if self.isDuplicateRow(col):
                return False
        
        for box_row in range(3):
            for box_col in range(3):
                start_row = box_row * 3
                start_col = box_col * 3
                box = []
                for r in range(3):
                    for c in range(3):
                        box.append(board[start_row + r][start_col + c])
                
                if self.isDuplicateRow(box):
                    return False

        return True
        
    def isDuplicateRow(self, row):
        dup_set = set()
        for num in row:
            if num == '.':
                continue
            if num in dup_set:
                return True
            else:
                dup_set.add(num)
        
        return False
