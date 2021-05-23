# Only letter (upper- and lowercase) and numeric (0–9) symbols should be affected
# All other symbols should pass through encryption and decryption unaffected.
# The shifting of a symbol should wrap around its set.
# one word (string) at a time, encode it, and print out the encoded version.
# continue until the single symbol “.” is given as input, which should terminate the program.
# must accept a single command-line argument defining the shift delta
# The value of delta must be an integer between -9 and +9

#入力は単語ごとに受け取るのか？それともまとめて文章で受け取るのか？

num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
upper_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def shift_num(num, delta):
    shifted_num = ""
    index = num_list.index(num)
    shifted_index = (index + delta) % 10
    shifted_num = num_list[shifted_index]
    return shifted_num


def shift_upper(string, delta):
    shifted_upper = ""
    index = upper_list.index(string)
    shifted_index = (index + delta) % 26
    shifted_upper = upper_list[shifted_index]
    return shifted_upper


def shift_lower(string, delta):
    shifted_lower = ""
    index = lower_list.index(string)
    shifted_index = (index + delta) % 26
    shifted_lower = lower_list[shifted_index]
    return shifted_lower


def shift_code(string:str, delta:int):
    flag = True
    for x in string:
        ord_x = ord(x)
        if (ord_x >= 48 and ord_x <= 57):
            shifted_str += shift_num(x, delta)
        elif (ord_x >= 65 and ord_x <= 90):
            shifted_str += shift_upper(x, delta)
        elif (ord_x >= 97 and ord_x <= 122):
            shifted_str += shift_lower(x, delta)
        else:
            shifted_str += x
            if x == '.':
                flag = False
                break

    if (flag == True):
        return shifted_str, True
    else:
        return shifted_str, False


def main():
    string = input("Input a word you want to encrypt:\n")
    delta = int(input("Input delta:\n"))
    encoded_str = ""
    str_list = string.split(" ")

    for x in str_list:
        shifted_str, flag = shift_code(x, delta)
        if (flag):
            encoded_str += shifted_str + " "
            continue
        else:
            break

    print(encoded_str)

main()
