# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 23:53:18 2020

@author: janar
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg=0
    count=0
    for i in student_marks[query_name]:
        avg+=i
        count+=1
    print(format(avg/count,'.2f'))