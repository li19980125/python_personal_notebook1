# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 20:15:09 2020

@author: li19980125
"""

"""
猜数

print("计算机以为您准备好要猜的数")
import random
corret = random.randint(1,100)
counter = 0
while True:
    counter += 1
    cai=int(input("请输入你猜的数 "))
    if cai > corret:
        print("猜大了")
    elif cai < corret:
        print("猜小了")
    else:
        print("猜对了")
        break
print("总共猜了 %d 次" % counter)

"""
"""

from math import sqrt
x = int(input("请输入要判断的数"))
flag = True
for y in range(2,int(sqrt(x))+2):
    if x % y == 0:
        print("输入的数不是素数")
        flag = False
        break
if flag:
    print("输入的数是素数")

"""
"""
print("寻找所有的水仙花数")
for x in range(100,1000):
    if (x//100)**3+(x//10%10)**3+(x%10)**3 == x:
        print("%d" % x)
        print()
print()
print("结束")
"""
"""
print("游戏开始")
from random import randint
wanjia1_money = 50
zhuangjia_money = 100
wanjia1= randint(1,6) + randint(1,6)
if wanjia1 == 7 or wanjia1 ==11:
    zhuangjia_money -=25
    print("玩家摇出了 %d ,玩家还剩 %d 元 ，庄家还剩 %d 元" % (wanjia1,wanjia1_money,zhuangjia_money))
if wanjia1 == 2 or wanjia1 == 3 or wanjia1 == 12:
    wanjia1_money -=25
    print("玩家摇出了 %d ,玩家还剩 %d 元 ，庄家还剩 %d 元" % (wanjia1,wanjia1_money,zhuangjia_money))
while True:
    wanjia2= randint(1,6) + randint(1,6)
    if wanjia2 == 7 : 
        wanjia1_money -=25
        print("玩家摇出了 %d ,玩家还剩 %d 元 ，庄家还剩 %d 元" % (wanjia2,wanjia1_money,zhuangjia_money))
        if wanjia1_money == 0:
            print("玩家破产")
            break
        if zhuangjia_money ==0:
            print("庄家破产")
            break
    if wanjia2 == wanjia1:
        zhuangjia_money -=25
        print("玩家摇出了 %d ,玩家还剩 %d 元 ，庄家还剩 %d 元" % (wanjia2,wanjia1_money,zhuangjia_money))
        if wanjia1_money == 0:
            print("玩家破产")
            break
        if zhuangjia_money ==0:
            print("庄家破产")
            break
print()
  """

"""
%可变参数函数调用以及for in元组  并求和
def lianjia(*arg):
    total = 0
    for i in arg:
        total += i
    return total

print("元组和为 %d" % lianjia(1,2,3,4,5,6))
"""







































