grid = [[(0,0), (17,0), (16,0), (21,0), (0,0), (0,0), (0,0), (30,0), (16,0)],
[(0,17), 0, 0, 0, (25,0), (0,0), (6,16), 0, 0],
[(0,29), 0, 0, 0, 0, (30,19), 0, 0, 0],
[(0,0), (3,0), (22,19), 0, 0, 0, 0, 0, (9,0)],
[(0,20), 0, 0, 0, 0, 0, (19,16), 0, 0],
[(0,4), 0, 0, (9,24), 0, 0, 0, 0, 0],
[(0,0), (4,31), 0, 0, 0, 0, 0, (14,0), (4,0)],
[(0,6), 0, 0, 0, (0,22), 0, 0, 0, 0],
[(0,3), 0, 0, (0,0), (0,0), (0,19), 0, 0, 0]]

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


def solve_pazzle(grid, row_check_list, col_check_list, x=1, y=1):
    print(x, y)
    if y >= len(grid): #ポインタが最後まで到達したら終了
        return True
    elif grid[y][x] != 0:
        if x == len(grid[0]) - 1:
            if solve_pazzle(grid, row_check_list, col_check_list, 1, y+1):
                return True
        else:
            if solve_pazzle(grid, row_check_list, col_check_list, x+1, y):
                return True
    else:
        for i in range(1, 10):
            if check_puzzle(grid, row_check_list, col_check_list, x, y, i):
                grid[y][x] = i
                if x == len(grid[0]) - 1:
                    if solve_pazzle(grid, row_check_list, col_check_list, 1, y+1):
                        return True
                else:
                    if solve_pazzle(grid, row_check_list, col_check_list, x+1, y):
                        return True
        grid[y][x] = 0
    return False


def output_file():
    return


# チェックする行の条件をまとめたリスト
# [[[合計の値、スタートインデックス、エンドインデックス], [], []],
#  [[], [], []]]
def make_row_check_list(grid):
    row_check_list = []
    flag = "end"
    for y in range(len(grid)):
        yl = []
        for x in range(len(grid[0])):
            # find end
            if type(grid[y][x]) == tuple and flag == "start":
                end = x - 1
                xl.append(end)
                yl.append(xl)
                flag = "end"
            elif x == len(grid[0]) - 1 and flag == "start":
                end = x
                xl.append(end)
                yl.append(xl)
                flag = "end"

            # find start
            if type(grid[y][x]) == tuple and grid[y][x][1] != 0 and flag == "end":
                start = x + 1
                xl = []
                xl.append(grid[y][x][1])
                xl.append(start)
                flag = "start"
        row_check_list.append(yl)

    return row_check_list


# チェックする行の条件をまとめたリスト
# [[[合計の値、スタートインデックス、エンドインデックス], [], []],
#  [[], [], []]]
def make_col_check_list(grid):
    col_check_list = []
    flag = "end"
    for x in range(len(grid[0])):
        xl = []
        for y in range(len(grid)):
            # find end
            if type(grid[y][x]) == tuple and flag == "start":
                end = y - 1
                yl.append(end)
                xl.append(yl)
                flag = "end"
            elif y == len(grid) - 1 and flag == "start":
                end = y
                yl.append(end)
                xl.append(yl)
                flag = "end"

            # find start
            if type(grid[y][x]) == tuple and grid[y][x][0] != 0 and flag == "end":
                start = y + 1
                yl = []
                yl.append(grid[y][x][0])
                yl.append(start)
                flag = "start"
        col_check_list.append(xl)

    return col_check_list


#　引数：パズルの配列、チェックする行のインデックス、
# 手順：
# １．その点がどのチェックリストに属するかチェック
# ２．グリッドのスタートからエンドまでに、バリューと同じ値がないか確認
# ３．チェックする範囲が全て埋まったなら、チェックリストの条件を満たすか確認
def check_row(grid, check_list, x, y, value):
    # その点がどのチェックリストに属するかチェック
    for l in check_list[y]:
        start = l[1]
        end = l[2]
        if x >= start and x <= end:
            tar_l = l
            break
    check_sum = tar_l[0]
    sum = 0
    same_val_flag = False
    full_flag = False
    correct_sum_flag = False
    for i in range(start, end + 1):
        if x == end:
            # グリッドのスタートからエンドまでに、バリューと同じ値がないか確認
            if value != grid[y][i]:
                same_val_flag = True
            else:
                same_val_flag = False
                break

            #チェックする範囲が全て埋まっているか？
            if i == end - 1 and grid[y][i] != 0:
                full_flag = True
            # チェックリストの条件を満たすか？
            if full_flag:
                for i in range(start, end):
                    sum += grid[y][i]
                if check_sum == sum + value:
                    correct_sum_flag = True
                    break
                else:
                    break
        # まだ全て埋まらない
        else:
            # グリッドのスタートからエンドまでに、バリューと同じ値がないか確認
            full_flag = True
            correct_sum_flag = True
            if value != grid[y][i]:
                same_val_flag = True
            else:
                same_val_flag = False
                break
    return same_val_flag and full_flag and correct_sum_flag


def check_col(grid, check_list, x, y, value):
    # その点がどのチェックリストに属するかチェック
    for l in check_list[x]:
        start = l[1]
        end = l[2]
        if y >= start and y <= end:
            tar_l = l
            break
    check_sum = l[0]
    sum = 0
    same_val_flag = False
    full_flag = False
    correct_sum_flag = False
    for i in range(start, end + 1):
        if y == end:
            # グリッドのスタートからエンドまでに、バリューと同じ値がないか確認
            if value != grid[i][x]:
                same_val_flag = True
            else:
                same_val_flag = False
                break

            #チェックする範囲が全て埋まっているか？
            if i == end - 1 and grid[i][x] != 0:
                full_flag = True
            # チェックリストの条件を満たすか？
            if full_flag:
                for i in range(start, end):
                    sum += grid[i][x]
                if check_sum == sum + value:
                    correct_sum_flag = True
                    break
                else:
                    break
        else:
            # グリッドのスタートからエンドまでに、バリューと同じ値がないか確認
            full_flag = True
            correct_sum_flag = True
            if value != grid[i][x]:
                same_val_flag = True
            else:
                same_val_flag = False
                break
    return same_val_flag and full_flag and correct_sum_flag



def check_puzzle(grid, row_check_list, col_check_list, x, y, value):
    if check_col(grid, col_check_list, x, y, value) and check_row(grid, row_check_list, x, y, value):
        return True
    else:
        return False


tes = [
[(0,0), (17,0), (16,0), (21,0), (0,0), (0,0), (0,0), (30,0), (16,0)],
[(0,17), 9, 3, 0, (25,0), (0,0), (6,16), 0, 0],
[(0,17), 0, 0, 0, 0, (30,19), 0, 0, 0],
[(0,0), (3,0), (22,19), 0, 0, 0, 0, 0, (9,0)],
[(0,20), 0, 0, 0, 0, 0, (19,16), 0, 0],
[(0,4), 0, 0, (9,24), 0, 0, 0, 0, 0],
[(0,0), (4,31), 0, 7, 0, 0, 0, (14,0), (4,0)],
[(0,6), 3, 1, 0, (0,22), 0, 0, 0, 0],
[(0,3), 0, 0, (0,0), (0,0), (0,19), 0, 0, 0]
]

def main(grid):
    row_check_list = make_row_check_list(grid)
    col_check_list = make_col_check_list(grid)
    solve_pazzle(grid, row_check_list, col_check_list)
    print(grid)

main(grid)

a = [
[(0, 0), (17, 0), (16, 0), (21, 0), (0, 0), (0, 0), (0, 0), (30, 0), (16, 0)], 
[(0, 17),   9,       7,       1,    (25, 0),(0, 0), (6, 16),   7,       9], 
[(0, 29),   8,       9,       5,       7,   (30, 19),  4,      8,       7], 
[(0, 0),  (3, 0), (22, 19),   7,       1,     4,       2,      5,     (9, 0)], 
[(0, 20),   2,      1,        8,       4,     5,     (19, 16), 9,       7], 
[(0, 4),    1,      3,       (9, 24),  5,     9,       7,      1,       2], 
[(0, 0),  (4, 31),  6,        7,       8,     1,       9,    (14, 0), (4, 0)], 
[(0, 6), 4, 2, 0, (0, 22), 0, 0, 0, 0], 
[(0, 3), 0, 0, (0, 0), (0, 0), (0, 19), 0, 0, 0]]

[[(0, 0), (17, 0), (16, 0), (21, 0), (0, 0), (0, 0), (0, 0), (30, 0), (16, 0)], 
[(0, 17), 9, 7, 1, (25, 0), (0, 0), (6, 16), 7, 9], 
[(0, 29), 8, 9, 7, 5, (30, 19), 4, 8, 7],
[(0, 0), (3, 0), (22, 19), 5, 4, 7, 2, 1, (9, 0)], 
[(0, 20), 2, 4, 8, 1, 5, (19, 16), 9, 7],
[(0, 4), 1, 3, (9, 24), 7, 1, 9, 5, 2],
[(0, 0), (4, 31), 6, 7, 8, 9, 1, (14, 0), (4, 0)],
[(0, 6), 3, 1, 2, (0, 22), 8, 4, 1, 9], 
[(0, 3), 1, 0, (0, 0), (0, 0), (0, 19), 0, 0, 0]]