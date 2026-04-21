class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def has_duplicated(l):
            nums = [x for x in l if x != '.']
            if len(nums) != len(set(nums)):
                return True

        for row in board:
            if has_duplicated(row):
                return False

        column = []
        for i in range(9):
            c = []
            for j in range(9):
                c.append(board[j][i])
            column.append(c)
        
        for c in column:
            if has_duplicated(c):
                return False

        blocks = []
        for row in [0, 3, 6]:
            for col in [0, 3, 6]:
                block = []
                for i in range(3):
                    for j in range(3):
                        block.append(board[row + i][col + j])
                blocks.append(block)

        print(blocks)

        for b in blocks:
            if has_duplicated(b):
                return False
                
        return True