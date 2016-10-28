# -*- coding: utf-8 -*-
__author__ = 'Alexander'

open = ['[', '<', '}', '(']
close = [']', '>', '{', ')']

def verify(param):
    arr = []
    for char in str(param):
        if char in open:
            arr.append(char)
        elif char in close:
            if (len(arr) == 0):
                print('0')
                return
            if (open.index(arr[-1]) == close.index(char)):
                arr.pop()
    if (len(arr) == 0):
        print('1')
    else:
        print('0')


verify("---(++++)----") #1
verify("") # 1
verify("before ( middle []) after ") # 1
verify(") (") # 0
verify("} {") # 1 //no, this is not a mistake.
verify("<( >)") # 0
verify("( [ <> () ] <> )") # 1
verify(" ( [)") # 0