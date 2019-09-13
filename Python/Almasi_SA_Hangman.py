#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 20:25:27 2019

@author: sirvanalmasi
"""
import random, sys
# Haven't used random - however in a comment I have put how you would use it
#   if you wanted to randomly select a word from the word bank.


# Global Variables
# Our wordBank and the number of lives
wordBank = ['alpha', 'force', 'coke', 'laptop']
lives = 7

# Let the user define the number of lives when running the code
try:
    if (len(sys.argv) > 1):
        lives = int(sys.argv[1])
except:
    # if there was an error in entering a correct lives default back
    print("ERROR in accepting the number of lives, defaulting to "+str(lives))

print(">> You have "+str(lives)+" lives")
print(">> Select an integer from 0 to "+str(len(wordBank)-1))

'''
# If you want to show the words for dev purposes
for i in range(len(wordBank)):
    print(str(i) + " - " + str(wordBank[i]))
'''


'''
Let the user choose an integer for themselves
--or we can alternatively choose a random number as follows:
chosenWord = random.randint(0, len(wordBank))
'''
def inputFunc():
    print(">> Please select an integer from the given range.")
    chosenWord = input(">> Choose a word index (e.g. 2): ")
    return chosenWord

chosenWord = inputFunc()

inputCheck = True
while(inputCheck == True):
    try:
        # Will be successful if we can change the str to int
        chosenWord = int(chosenWord)
        if ((chosenWord > len(wordBank)-1) or (chosenWord < 0)):
            # still wrong
            chosenWord = inputFunc()
        else:
            # Correct statement
            inputCheck = False
    except:
        # Most likely chosenWord is not int
        chosenWord = inputFunc()

##      
# Let the game begin
##
def joinPrint(word):
    print(''.join(word))

# Hold the chosen word in a temp variable
theWord = wordBank[chosenWord]

# Create an array of equal length to the chosen word
# which includes the stars
guessedWord = []
remainingStars = len(theWord)
for i in range(len(theWord)):
    guessedWord.append("*")

joinPrint(guessedWord)

# function which has the input command because its repetitive
def inputGuess():
    chosenCharacter = input(">> Select a character: ").lower()
    return chosenCharacter

# Keep asking the user for inputs until there are no more lives or
# the game has been won.
while(lives > 0):
    chosenCharacter = inputGuess()
    foundWord = False
    for i in range(len(theWord)):
        if((chosenCharacter == theWord[i]) and (chosenCharacter != "0")):
            guessedWord[i] = chosenCharacter
            remainingStars -= 1
            foundWord = True
    
    if (foundWord is False):
        lives -= 1
        print("oops wrong character")
    else:
        theWord = theWord.replace(str(chosenCharacter), "0")
    
    print(''.join(guessedWord))
    print("Lives: " + str(lives))
    if(remainingStars==0):
        print("Print wohooo... you have won")
        break
