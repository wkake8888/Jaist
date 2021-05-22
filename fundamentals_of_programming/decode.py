# dict contains only words(no number). First char is upper.
# 0 <= delta <= 25 can check all the possible return
# デルタが25個ということは、デコードするパターンが25個ということ。
# dictには97000単語あり。
#　デルタは一つのみ、入力は文章という前提ですすめる
すべての単語は大文字から始まると考えていいのか？
もしそうでないのなら、大文字と小文字は違うものとして扱うべきか？

# 方法１：
# すべての単語から適切なデルタを求める

# 入力を単語ごとに分ける
# それぞれにあるデルタでシフトさせて、配列にいれる
# 配列に入っているシフト後の単語を、辞書に照らし合わせて不一致箇所数をカウントする
# 最小不一致数のデルタを変数で管理
# 全てのデルタで試行後、デルタを返す

# 方法2：
# 先頭の単語だけで、適切なデルタを求める

upper_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
short_cut = {"A":0, "B":1228, "C":2447, "D":3798, "E":4499, "F":5075, "G":5513, "H":6212, "I":6950, "J":7265, "K":7756, "L":8315, "M":9128, "N":10653, "O":11148, "P":11481, "Q":12368, "R":12425, "S":13107, "T":14501, "U":15287, "V":15414, "W":15728, "X":16170, "Y":16206, "Z":16345}

def decode_upper(string, delta):
    decode_upper = ""
    index = upper_list.index(string)
    decoded_index = (index - delta) % 26

    decoded_upper = upper_list[decoded_index]
    return decoded_upper


def decode_lower(string, delta):
    decoded_lower = ""
    index = lower_list.index(string)
    decoded_index = (index - delta) % 26

    decoded_lower = lower_list[decoded_index]
    return decoded_lower


def decode_str(string, delta):
    decoded_str = ""
    for x in string:
        ord_x = ord(x)
        if (ord_x >= 65 and ord_x <= 90):
            decoded_str += decode_upper(x, delta)
        elif (ord_x >= 97 and ord_x <= 122):
            decoded_str += decode_lower(x, delta)
        else:
            decoded_str += x

    return decoded_str


def read_file():
    word_dic = open("./word_dictionary/words", "r")
    dic_list = word_dic.readlines()
    # for i in range(len(dic_list)):
    #     dic_list[i].replace("\n", "")
    # print(dic_list)
    return dic_list


def check_match(word):
    dic_list = read_file()
    first_char = word[0]
    start_index = decode_upper(first_char, -1)
    end_index = decode_upper(first_char, -2)

    for i in range(start_index, end_index):
        target_word = dic_list[i]
        

def main():
    string = input("Input a text you want to decode\n")
    str_list = string.split(" ")

    for i in range(1, 26):
        shifted_list = []
        delta = i
        for x in str_list:
            shifted_list.append(decode_str(x, delta))
        
    print(shifted_list)

main()


