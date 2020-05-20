from random import choice



class TicTacToe:
    def __init__(self):
        self.board =   {1:[ ], 2:[ ], 3:[ ],
                        4:[ ], 5:[ ], 6:[ ],
                        7:[ ], 8:[ ], 9:[ ]}
        self.winningCombo = [[1,2,3], [4,5,6], [7,8,9],]
    def printBoard(self):
        print("",self.board[1], self.board[2], self.board[3], '\n',
       self.board[4], self.board[5], self.board[6], '\n',
      self.board[7], self.board[8], self.board[9] )
        return

    def checkBoard(self):
        for x in self.winningCombo:
            print(*x)


    def mainlogic(self):
        while True:
            printBoard(board)
            if playerWin:
                print("You win!")
                break
            elif playerLose:
                print("You lose faggit git gud scrub")
                break
            else:
                print("It's a tie! We go AGANE")
                break
    print("Thanks for playing! We have left the loop.")

if __name__ == '__main__':
    mainClass = TicTacToe()
    mainClass.printBoard()
    mainClass.checkBoard()
