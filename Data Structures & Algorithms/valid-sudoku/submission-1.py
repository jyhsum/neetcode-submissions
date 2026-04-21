class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def has_duplicated(l):
            nums = [x for x in l if x != '.']
            return len(nums) != len(set(nums))

        for row in board:
            if has_duplicated(row):
                return False

        for col in zip(*board):   # 直接轉置取 column
            if has_duplicated(col):
                return False

        blocks = []
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                block = []
                for i in range(3):
                    for j in range(3):
                        block.append(board[row + i][col + j])
                blocks.append(block)

        for b in blocks:
            if has_duplicated(b):
                return False

        return True