#!/usr/bin/python3
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
@Filename : Exersises
@Date : 2020-10-28-20-31
@Project: Python-programming-exercises
@AUTHOR : Dan Even
'''
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''
#################
str=(input("Enter coma separated numbers"))
l=list()
t=tuple()
nstr = ''
for i in str:
    if i !="," :
       nstr = nstr + i
    else:
        l.append(nstr)
        t = t + (nstr,)
        nstr = ''
l.append(nstr)
t = t + (nstr,)
print(l,t)
################################
values=(input("Enter coma separated numbers"))
mylist=values.split(",")
mytuple=tuple(mylist)
print(g,k)
