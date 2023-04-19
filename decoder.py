

def newMove(curr, move):
    row, col = curr
    
    if move == 'U':
        row -= 1
    elif move == 'D':
        row += 1
    elif move == 'L':
        col -= 1
    elif move == 'R':
        col += 1
    
    if (row, col) in buttons:
        return row, col
    else:
        return curr

buttons = {
            (0, 0): "1", (0, 1): "2", (0, 2): "3",
            (1, 0): "4", (1, 1): "5", (1, 2): "6",
            (2, 0): "7", (2, 1): "8", (2, 2): "9"
}
           
with open("doc.txt", "r") as f:
    moves = f.readlines()

curr = (1, 1)
code = ""
for movesLine in moves:
    for move in movesLine:
        curr = newMove(curr, move)
    code += buttons[curr]
print(code)