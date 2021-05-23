# dict contains only words(no number). First char is upper.
# 0 <= delta <= 25 can check all the possible return
# デルタが25個ということは、デコードするパターンが25個ということ。
# dictには97000単語あり。
#　デルタは一つのみ、入力は文章という前提ですすめる

#Questions:
# すべての単語は大文字から始まると考えていいのか？
# No
# もしそうでないのなら、大文字と小文字は違うものとして扱うべきか？
# No,辞書の先頭の大文字を小文字にしても良い

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

def decode_upper(string:str, delta:int):
    decode_upper = ""
    index = upper_list.index(string)
    decoded_index = (index - delta) % 26

    decoded_upper = upper_list[decoded_index]
    return decoded_upper


def decode_lower(string:str, delta:int):
    decoded_lower = ""
    index = lower_list.index(string)
    decoded_index = (index - delta) % 26

    decoded_lower = lower_list[decoded_index]
    return decoded_lower


def decode_str(string:str, delta:int):
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
    return dic_list


def check_match(string:str):
    dic_list = read_file()
    check_word = lower_to_upper(string)
    first_char = check_word[0]
    start_index = short_cut[first_char]
    end_index = short_cut[decode_upper(first_char, -1)]
    max_match = 0
    for i in range(start_index, end_index):
        dict_word = dic_list[i].rstrip("\n")
        match = 0
        match_word = dic_list[0]
        # 単語の長さが同じであると想定
        if len(check_word) > len(dict_word):
            r = len(dict_word)
        else:
            r = len(check_word)

        for j in range(r):
            if check_word[j] == dict_word[j]:
                match += 1
        if match > max_match:
            max_match = match
            match_word = check_word

    return max_match


def lower_to_upper(string:str):
    ord_x = ord(string[0])
    new_str = string
    if (ord_x >= 65 and ord_x <= 90):
        return new_str
    else:
        if len(new_str) == 1:
            index = lower_list.index(new_str[0])
            new_str = upper_list[index]
            return new_str
        else:
            index = lower_list.index(new_str[0])
            new_str = upper_list[index] + new_str[1:]
            return new_str

def main():
    string = input("Input a text you want to decode\n")
    str_list = string.split(" ")
    decoded_str = ""
    delta_list = []
    for string in str_list:
        shifted_dict = {}
        match_delta = 0
        max_match = 0
        # シフト後のそれぞれの単語について
        #　min_diffとデルタを調べる
        #　最小min_diffをもつデルタが有望
        for i in range(1, 26):
            delta = i
            shifted_string = decode_str(string, delta)
            match = check_match(shifted_string)
            if match > max_match:
                max_match = match
                match_delta = delta
        delta_list.append(match_delta)

    match_delta = most_frequent(delta_list)
    # それぞれの単語について適切なデルタを求めて配列に入れる
    for k in range(len(str_list)):
        s = decode_str(str_list[k], match_delta)
        decoded_str += s + " "

    print(decoded_str)
    # 配列の中で最も多いデルタを用いてデコード
    # decode_str(string, delta)

    #　出力
    # print(decoded_str)
def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num


main()