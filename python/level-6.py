#! /usr/bin/python3

import readline
import re
from jail import intro

print(intro(6))

print("Welcome to your doom!!!")
print()
print("Protections:")
print("This is a calculator. You cannot use letters.")
print()

while True:
    try:
        cmd = input(">>> ")
        if re.match(".*[a-zA-Z].*", cmd):
            print("NO!")
        else:
            print(eval(cmd))
    except EOFError:
        exit()
    except Exception as e:
        print("Error ", e)
