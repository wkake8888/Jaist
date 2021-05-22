# load puzzle data
def load_file():
    lineList = list()
    with open("input.txt") as f:
        for line in f:
            line.rstrip('\n')
            lineList.append(line)
    return lineList


def find_next_cell(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                return y, x
    return -1, -1


def solve_pazzle():
    return


def output_file():
    return



grid = [[(0,0), (17,0), (16,0), (21,0), (0,0), (0,0), (0,0), (30,0), (16,0)],
[(0,17), 0, 0, 0, (25,0), (0,0), (6,16), 0, 0],
[(0,17), 0, 0, 0, 0, (30,19), 0, 0, 0],
[(0,0), (3,0), (22,19), 0, 0, 0, 0, 0, (9,0)],
[(0,20), 0, 0, 0, 0, 0, (19,16), 0, 0],
[(0,4), 0, 0, (9,24), 0, 0, 0, 0, 0],
[(0,0), (4,31), 0, 0, 0, 0, 0, (14,0), (4,0)],
[(0,6), 0, 0, 0, (0,22), 0, 0, 0, 0],
[(0,3), 0, 0, (0,0), (0,0), (0,19), 0, 0, 0]]

y,x = find_next_cell(grid)
print(y, x)
