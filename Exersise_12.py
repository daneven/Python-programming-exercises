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
uestion 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

        '''
a=[]
for item in range(1000,3001):
    a.append(str(item))
    answ = []
for i in a:
    for n in i:
        if int(n)%2 == 0:
            pass
        else:
            break
    else:
     answ.append(i)
print(','.join(answ))
        # Inner loop was broken, break the outer.
'''
Solution:
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print ",".join(values)
'''