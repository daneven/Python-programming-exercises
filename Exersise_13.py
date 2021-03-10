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
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''
a=input("sentense with numbers ")
d={"DIGITS":0, "LETTERS":0}
for i in a :
    if i.isnumeric():
        d["DIGITS"]+=1
    elif i.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print (f"numbers= {d['DIGITS']} letters = {d['LETTERS']}")


""" hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
s = raw_input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print "LETTERS", d["LETTERS"]
print "DIGITS", d["DIGITS"]
"""
