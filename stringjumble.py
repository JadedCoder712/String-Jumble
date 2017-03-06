"""
stringjumble.py
Author: <your name>
Credit: <sources>

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
backward-backward: ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
forward-backward: handy find may you that tricks or techniques few a are There
backward-forward: erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
#forward-backward

sentence = input("Please enter a string of text (the bigger the better): ")
a2 = sentence.split()
#commandforsorting
#c2 = " ".join(b2)
#print(c2)

#commandforsorting:
length = len(a2)
mylist = range(1, int(length)+1)
for a in mylist:
    print(a2[-a], end=" ")




