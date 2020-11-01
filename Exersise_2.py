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
Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''
def fact(number):
    a = 1
    for i in range(1,number+1):
       a = a*i
    print(a)

fact(1)
####################################recursive !
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x =int(input("Enter number"))
print(fact(x))