n = int(input("Please enter a positive integer...="))
operator = input("Please enter operation...=")

for i in range(1, n + 1):
    equation = ""
    for j in range(1, i + 1):
        if (j == (i)):
            print(str(j), end=' ')
        else:
            print(str(j), end=operator)
        if operator == '+':
            equation += str(j) + "+"
        elif operator == '*':
            equation += str(j) + "*"
        elif operator == '-':
            equation += str(j) + "-"
        else:
            equation += str(j) + "/"

    print('=', eval(equation[:-1]), "\n")
