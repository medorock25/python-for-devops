import os
import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[3])
ope = sys.argv[2]
def adding(num1, num2):
    add = num1 + num2
    return add

def sub(num1, num2):
    sub = num1 - num2
    return sub

if ope == "add":
    print(adding(num1, num2))
elif ope == "sub":
    print(sub(num1, num2))


