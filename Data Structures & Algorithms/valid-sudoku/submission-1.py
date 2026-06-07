class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #first set default dicts to check if already in row , column, and box



        # loop through each column by row | return false if any time invalid
        #default dict so that if the key is empty when added it creates a key and adds that number
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        #sample for first spot:
        #{0:{1}}
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue
                #check if current spot is in row or column or box already
                if (board[r][c] in row[r]  
                    or board[r][c] in col[c] 
                    or board[r][c] in square[(r//3,c//3)]
                    ):
                    return False

                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r//3,c//3)].add((board[r][c]))
        return True
                
