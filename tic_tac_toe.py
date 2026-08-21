board = list("123456789")
for turn in range(9):
    print(" ".join(board[i:i+3] for i in range(0, 9, 3)))
    move = int(input(f"Player {'X' if turn % 2 == 0 else 'O'}, position: ")) - 1
    board[move] = 'X' if turn % 2 == 0 else 'O'
    if any(board[a] == board[b] == board[c] for a,b,c in ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))):
        print("Winner:", board[move]); break
else: print("Draw")

