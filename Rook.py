#main board for location rooks
board = [['*','*','*','*'],['*','*','*','*'],['*','*','*','*'],['*','*','*','*']]
#Helper board for checking free cells
# '#' mean this cell is block
# '*' mean this cell is free cell
Helper = [['*','*','*','*'],['*','*','*','*'],['*','*','*','*'],['*','*','*','*']]
count = 0
while count < 4: #put rook('R' character) inder all of cells in first row
    z = 0
    k = 0
    board[0][count] = 'R'
    while z < 4:
        Helper[0][z] = '#'
        z = z + 1
    while k < 4:
        Helper[k][count] = '#'
        k = k + 1
    for i in range(4):
        for j in range(4):
            if Helper[i][j] != '#':
                board[i][j] = 'R'
                for k in range(i,4):
                    Helper[i][k] = '#'
                    Helper[k][j] = '#'
                break
            else:
                continue
    for i in range(4):
        print('\n')
        for j in range(4):
            print(board[i][j], end='\t')
            Helper[i][j] = '*'
            board[i][j] = '*'
    # reset all of cells of Helper board and main board then try new board (we check all of status in board)

    print('\n=================================')
    count = count + 1
