class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        grid = collections.defaultdict(set) # (row // 3) * 3 + (col // 3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".": continue

                if val in rows[r] or val in cols[c] or val in grid[(r // 3) * 3 + (c // 3)]: return False

                rows[r].add(val)
                cols[c].add(val)
                grid[(r // 3) * 3 + (c // 3)].add(val)
        
        return True


        



        