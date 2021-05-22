# Q1. make a digital clock program

# In the first line you are asked to input the current time
# current time is represented by hour A(0<=A<=23), minute B(0<=B<=59), and second C(0<=C<=59)
# In the second line you are asked to input the time passed by seconds D(0<=D<=500,000)
# Write a program that prints the hour, minute, second in order spaced by a blank character after D seconds is passed

A, B, C = map(int, input().split())
pass_seconds = int(input())

second = (C + pass_seconds) % 60
if C + pass_seconds > 59:
    extra_minute = round((C + pass_seconds) / 60)
else:
    extra_minute = 0
minute = (B + extra_minute) % 60
if (B + extra_minute) > 59:
    extra_hour = round((B + extra_minute) / 60)
else:
    extra_hour = 0
hour = A + extra_hour

if hour > 23:
    hour -= 24

print(str(hour) + " " + str(minute) + " " + str(second))


# Q2. Find out which quadrant the input point is
# You are asked to input 2 arbitrary real numbers x(-1000<=x<=1000, x!=0) and y(-1000<=y<=1000, y!=0).
# Write a program that prints the quadrant of the coordinate plane for the given input.

x = int(input("input arbitrary real number\n"))
y = int(input("input arbitrary real number\n"))

if (x )

