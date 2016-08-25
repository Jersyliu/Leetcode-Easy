class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dictD={'1':1,'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,'8':1,'9':1}
        row,col,blk=[],[],[]
        for i in range(9):
            row+=[dictD.copy()]
            col+=[dictD.copy()]
            blk+=[dictD.copy()]
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if row[i][board[i][j]]==0 or col[j][board[i][j]]==0 or blk[i//3*3+j//3][board[i][j]]==0:
                    return False
                else:
                    row[i][board[i][j]]-=1
                    col[j][board[i][j]]-=1
                    blk[i//3*3+j//3][board[i][j]]-=1
        return True
        
a=Solution()
board=[".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
print a.isValidSudoku(board)