# 1. n個体初期化する
# 2. ランダムに2個体 p1, p2 を選ぶ
# 3. p1,p2を交叉して m個体作る
# 4. ｛p1,p2,m個体｝から，ベスト2つを p1,p2の代わりに集団に戻し，2.に戻る
import random
# n個体初期化する
def make_random_bit(n:int):
    l = []
    for i in range(n):
        bit = ""
        for j in range(40):
            x = random.random()
            if x > 0.5:
                bit += "1"
            else:
                bit += "0"
        l.append(bit)

    return l

# p1,p2を交叉して m個体作る
# 一様交叉
def uniform_crossover(p1:str, p2:str, m:int):
    l = []
    for i in range(m):
        child = ""
        for j in range(40):
            x = random.random()
            if x > 0.5:
                child += p1[j]
            else:
                child += p2[j]
        l.append(child)
    return l

# p1,p2を交叉して m個体作る
# 一様交叉
# mが奇数だとちょっと工夫する
def spc(p1, p2, m):
    l = []
    for i in range(m // 2):
        a = random.randint(1, 40)
        p1_x = p1[a:]
        p2_x = p2[a:]
        child1 = p1[:a] + p2_x
        child2 = p2[:a] + p1_x
        l.append(child1)
        l.append(child2)
    return l

# 点数計算
def cal_score(x):
    score = 0
    l = []
    a = 0
    b = 4
    while b <= 40:
        y = x[a:b]
        l.append(y)
        a += 4
        b += 4

    for i in l:
        if i == "1111":
            score += 4
        else:
            ct = i.count("0")
            score += ct - 1
    return score

def get_best_score(l:list):
    if cal_score(l[0]) > cal_score(l[1]):
        best1 = cal_score(l[0])
        best2 = cal_score(l[1])
        best1_x = l[0]
        best2_x = l[1]
    else:
        best1 = cal_score(l[1])
        best2 = cal_score(l[0])
        best1_x = l[1]
        best2_x = l[0]

    for i in range(2, len(l)):
        score = cal_score(l[i])
        if score > best1:
            best2 = best1
            best2_x = best1_x
            best1 = score
            best1_x = l[i]
        elif score > best2:
            best2 = score
            best2_x = l[i]
    return best1, best1_x, best2_x


def main(n:int, m:int, loop:int):
    # n個体初期化する
    l = make_random_bit(n)

    for i in range(loop):
        # ランダムに2個体 p1, p2 を選ぶ
        # 選んだ２個体は集団から抜く
        p1 = l[random.randrange(0, n)]
        l.pop(l.index(p1))
        p2 = l[random.randrange(0, n-1)]
        l.pop(l.index(p2))
        # p1,p2を交叉して m個体作る
        #　一様交叉
        # crossover = uniform_crossover(p1, p2, m)
        # 一点交叉
        crossover = spc(p1, p2, m)
        # ｛p1,p2,m個体｝からベスト2つをp1,p2の代わりに集団に戻し，2.に戻る
        crossover.append(p1)
        crossover.append(p2)
        best1, best1_x, best2_x = get_best_score(crossover)
        l.append(best1_x)
        l.append(best2_x)

    # 最後に集団内の最善評価値を返す
    best1, best1_x, best2_x = get_best_score(l)
    return best1

sum = 0
for i in range(10):
    a = main(1000, 10, 10000)
    sum += a

print(sum / 100)