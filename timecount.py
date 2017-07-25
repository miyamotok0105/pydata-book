#coding:utf-8
# timecount2.py
import math

def func1():
    ls = []
    for i in range(1000):
        ls.append(i)
    return ls

def func2():
    ls = []
    for i in range(1000):
        ls.append(i * i * i)
    return ls

def func3():
    ls = []
    for i in range(1000):
        ls.append(pow(i,i))
    return ls

func1()
func2()
func3()
