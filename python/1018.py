import sys

input = sys.stdin.readline

board = []
y, x = map(int, input().split())

for i in range(y):
    raw = list(input().strip())
    board.append(raw)

repaint_list = []
# initial_mark = board[0][0]

for i in range(y-7):
    for j in range(x-7):
        repaint_w = 0
        repaint_b = 0
        for coord_y in range(8):
            for coord_x in range(8):
                if (coord_x+coord_y) % 2 == 0:
                    if board[coord_y+i][coord_x+j] != "W":
                        repaint_w += 1
                    if board[coord_y+i][coord_x+j] != "B":
                        repaint_b += 1
                else:
                    if board[coord_y+i][coord_x+j] != "B":
                        repaint_w += 1
                    if board[coord_y+i][coord_x+j] != "W":
                        repaint_b += 1
                                
        repaint_list.append(repaint_w)
        repaint_list.append(repaint_b)



print(min(repaint_list))
# print(repaint_list)
