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
Question 9
Level 2

Question£º
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''
arr=[]
while True:
 print(''.join(arr))
 arr=[]
 inp = input("Enter lines")
 for item in inp:
  arr.append(item.capitalize())
'''
Solution:
lines = []
while True:
    s = raw_input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print sentence
'''