# Q1. make a digital clock program

# In the first line you are asked to input the current time
# current time is represented by hour A(0<=A<=23), minute B(0<=B<=59), and second C(0<=C<=59)
# In the second line you are asked to input the time passed by seconds D(0<=D<=500,000)
# Write a program that prints the hour, minute, second in order spaced by a blank character after D seconds is passed

h, m, s = map(int, input().split())
if h<0 or h>23:
    print("0<=h<=23")
if m<0 or m>59:
    print("0<=m<=59")
if s<0 or s>59:
    print("0<=s<=59")

sec = int(input())

s1 = (s+sec)%60

m1 = (s+sec)//60
m2 = (m+m1)%60

h1 = (m+m1)//60
h2 = (h+h1)%24

print(h2, m2, s1)


# Q2. Find out which quadrant the input point is
# You are asked to input 2 arbitrary real numbers x(-1000<=x<=1000, x!=0) and y(-1000<=y<=1000, y!=0).
# Write a program that prints the quadrant of the coordinate plane for the given input.

x, y = map(int, input().split())
if x<-1000 or x>1000 or x==0:
    print("-1000<=x<=1000, x!=0")
if y<-1000 or y>1000 or y==0:
    print("-1000<=y<=1000, y!=0")

if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x>0 and y>0:
    print(3)
else:
    print(4)


# Q3. GPA
# Write a program that input 3 grades and print the GPA
# Grades must match the following rules
# A+: 4.5 A0: 4.0
# B+: 3.5 B0: 3.0
# C+: 2.5 C0: 2.0
# F: 0.0

c1, c2, c3 = map(int, input().split())
if c1=="A+":
    c1=4.5
elif c1=="A0":
    c1=4.0
elif c1=="B+":
    c1=3.5
elif c1=="B0":
    c1=3.0
elif c1=="C+":
    c1=2.5
elif c1=="C0":
    c1=2.0
elif c1=="F":
    c1=0.0
else:
    print("Grade mismatch")

if c2=="A+":
    c2=4.5
elif c2=="A0":
    c2=4.0
elif c2=="B+":
    c2=3.5
elif c2=="B0":
    c2=3.0
elif c2=="C+":
    c2=2.5
elif c2=="C0":
    c2=2.0
elif c2=="F":
    c2=0.0
else:
    print("Grade mismatch")

if c3=="A+":
    c3=4.5
elif c3=="A0":
    c3=4.0
elif c3=="B+":
    c3=3.5
elif c3=="B0":
    c3=3.0
elif c3=="C+":
    c3=2.5
elif c3=="C0":
    c3=2.0
elif c3=="F":
    c3=0.0
else:
    print("Grade mismatch")

print((c1+c2+c3)/3)

# Q4. Add 2 binary numbers
# You are asked to input 2 binary numbers spaced with a blank character
# Write a program that adds 2 binary numbers and print the result as a binary number.
# The result must start with 1.
A, B = map(str, input().split())
A = int(A, 2)
B = int(B, 2)
C = A+B
print(bin(C)[2:])
