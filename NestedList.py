# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 12:11:40 2020

@author: janar
"""
if __name__ == '__main__':
    lst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name, score])
    lst2 = [i[1] for i in lst]
    lst2 = set(lst2)
    lst2 = sorted(list(lst2))

    ret = [i[0]  for i in lst if i[1]==lst2[1]]
    ret = sorted(ret)

    for i in range(len(ret)):
        print(ret[i])