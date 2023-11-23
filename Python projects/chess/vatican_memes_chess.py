"""
Emojis:
⬜ | white large square | \u2B1C
⬛ | black large square | \u2B1B
"""

grid = [[["8"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"]], 
        [["7"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"]], 
        [["6"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"]], 
        [["5"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"]], 
        [["4"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"]], 
        [["3"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"]], 
        [["2"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"]], 
        [["1"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"], ["\u2B1B"], ["\u2B1C"]],
        [["  "], ["A "], ["B "], ["C "], ["D "], ["E "], ["F "], ["G "], ["H "]]]


def print_grid(grid):
    for i in grid:
        row = []
        for j in i:
            row.append("".join(j))
        print("".join(row))

print_grid(grid)

#♔♕♖♗♘♙♚♛♜♝♞♟︎