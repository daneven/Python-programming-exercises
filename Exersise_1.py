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
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
for number in range(2000 , 3201):
    arr = []
    a = number % 7
    if a == 0:
        if number % 5 !=0:
            arr.append(number)
        else:
            pass
    for n in range(len(arr)):
       print(f"{arr[n]},",end =" ")

 ###############################
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))
####################