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
sentence = input("Please enter a string of text (the bigger the better): ")

#backward-backward:

a1 = list(sentence)
length1 = len(a1)
mylist1 = range(1, int(length1)+1)
for a in mylist1:
    print(a1[-a], end="")
print(" ")

#forward-backward:
a2 = sentence.split()
length2 = len(a2)
mylist2 = range(1, int(length2)+1)
for b in mylist2:
    print(a2[-b], end=" ")
    
#backward-forward:
    
sentence = input("Please enter a string of text (the bigger the better): ")

a3=sentence.split()

for c in a3:
    words=list(c)
    length3=len(words)
    mylist3=range(1, int(length3)+1)
    for d in mylist3:
        print(words[-d], end="")
    print(" ", end="")

        
    
    



