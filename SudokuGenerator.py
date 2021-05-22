import random as rd

class SudokuGenerator:
    def __init__(self,N=9) -> None:
        self.N = N
        self.unsolvedGrid = [[0]*N for i in range(N)]
        self.solvedGrid = None
        self.posLis = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8),
            (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 0), (2, 1), (2, 2), (2, 3), 
            (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), 
            (3, 8), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (5, 0), (5, 1), (5, 2), 
            (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), 
            (6, 7), (6, 8), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (8, 0), (8, 1), 
            (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]

    def helper_generateSudoku(self):
        positions = self.findEmpty()

        if positions == None:
            return True

        row,col = positions

        for val in range(1,10):
            if self.validPosition(val,row,col):
                self.unsolvedGrid[row][col] = val
                if self.helper_generateSudoku():
                    return True
                self.unsolvedGrid[row][col] = 0

        return False

    def findEmpty(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.unsolvedGrid[i][j] == 0:
                    return (i,j)

        return None

    def validPosition(self,val,row,col):

        for i in range(self.N):
            if self.unsolvedGrid[i][col] == val:
                return False
        for i in range(self.N):
            if self.unsolvedGrid[row][i] == val:
                return False

        box_Rowpos = row//3
        box_Colpos = col//3

        for i in range(box_Rowpos*3,box_Rowpos*3+3):
            for j in range(box_Colpos*3,box_Colpos*3+3):
                if self.unsolvedGrid[i][j] == val:
                    return False

        return True

    def generateSudoku(self):

        for _ in range(self.N):
            row,col = rd.randint(1,self.N-1),rd.randint(1,self.N-1)
            val = rd.randint(1,self.N)
            if self.validPosition(val,row,col):
                self.unsolvedGrid[row][col] = val

        if self.helper_generateSudoku():
            self.solvedGrid = self.unsolvedGrid
            self.unsolvedGrid = [[0]*self.N for i in range(self.N)]
            return self.removeElement()

    def removeElement(self):
        filledPos = []
        i = 0
        no_of_fills = rd.choice([30,31,32,33,34,35])
        for i in range(no_of_fills):
            while(True):
                pos  = rd.choice(self.posLis)
                if pos not in filledPos:
                    row,col = pos
                    self.unsolvedGrid[row][col] = self.solvedGrid[row][col]
                    filledPos.append(pos)
                    break

        return self.unsolvedGrid

    def print_board(self,bo):
        for i in range(len(bo)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")

            for j in range(len(bo[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(bo[i][j])
                else:
                    print(str(bo[i][j]) + " ", end="")



if __name__ == '__main__':
    s = SudokuGenerator()
    s.print_board(s.generateSudoku())
    print("\n Enter to see Answer")
    input()
    s.print_board(s.solvedGrid)
    
    
