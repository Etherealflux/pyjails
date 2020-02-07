#! /usr/bin/python3

import readline
import re
from jail import intro

print(intro(7))

print("Welcome to your doom!!!")
print()
print("Protections:")
print("I will only accept 16 bytes of input at a time.")
print()

while True:
    try:
        cmd = input(">>> ")
        if len(cmd) > 16
            print("NO!")
        else:
            print(eval(cmd))
    except EOFError:
        exit()
    except Exception as e:
        print("Error ", e)
