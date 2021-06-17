#Hangman is a game for two players. One player thinks of a word; and the other player tries to guess it.
#The word is initially represented by a row of dashes (one dash per letter). The guessing player successively
#suggests a letter that is believed to occur in the word.
#If the letter does occur in the owrdm the other player writes down the letter in all of its correct positions.
#If the letter does not occur in the word, th other player has one less guess
#The game ends when the guessing player completes the owrd or exhausts their number of guesses.

import random

def checkword (x): 
    while True:
        if x.isupper() and x.isalpha(): 
            return(x)
        else:
            x = input("Please enter another word for the other player to guess:")
            
def makeblanks (x, y):
    if y == 0:        
        blanks = len(x) * "-"
        return(blanks)
    elif y != 0:
        indices = [i for i, L in enumerate(x) if L == y]        
        blanks = "".join(blankList)
        for index in indices:
            blankList[index] = y
            blanks = "".join(blankList)
        return(blanks)                
    
def unusedletter (x,y):
    if y in x:
        x.remove(y)
        strx = ""        
        return(strx.join(x))
    elif y == 0:
        strx = ""        
        return(strx.join(x))
    else:
        return(x)

def checkletter (x):
    while True:
        if x in alphabetlist:
            return x
        else:
            x = input("Letter is used/wrong, please type a new letter:")

def changeguesscount ():
    while True:
        guesschange = input("Do you want change the number of guesses, the default is 6 ('Y'/'N'):")     
        
        if guesschange == "Y":
            while True:
                guesscount = input("Input guesscount:")
                try:
                    guesscount = int(guesscount)
                    if guesscount >= 0:
                        return(guesscount)            
                    else:
                       guesscount = input("Input guesscount:")    
                except ValueError:
                    continue                   
                
        elif guesschange == "N":
            guesscount = 6
            return(guesscount)
        else:
            continue
    
def repeatgame(x):
    if x != 0:
        while True:
            ask = input("Do you want to play again? ('YES'/'QUIT'):")
            if ask == "QUIT":
                return(ask)             
            elif ask == "YES":
                return               

def randomword(x):
    randomList = ["APPLE", "BANANA", "CHERRY", "LANZONES", "MANGO", "GUYABANO"]
    
    while True:
        if x == 0:
            wordask = input("Do want to type your own word? ('Y'/'N'):")
            if wordask == "N":
                print("A random word will be provided:")
                y = (random.choices(randomList))
                z = "".join(y)
                return(z)
            elif wordask == "Y":
                y = input("Please enter a word for the other player to guess:")
                return(y)
            
#######################################################
gamecounter = 0
while True: 
    
    
    asking = repeatgame(gamecounter)
    if asking == "QUIT":
        break 
    
    
    guesscount = changeguesscount()
    alphabetlist = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letter = 0
    
    
    word = randomword(letter)
    
    #print(word)
    wordList = list(word)
    word = checkword(word)
    blanks = ""
    usedletterList = []
       
    
    while True:        
        FirstMess = "\nGuess the word, {} guess(es) left: {}"          
        blanks = makeblanks(word,letter)
        blankList = list(blanks)    
        print(FirstMess.format(guesscount, blanks))
        
        
        if word == blanks: # win case
            print("Congratulations! You win!")
            gamecounter = gamecounter + 1
            break        
        
        unusedletterString = unusedletter(alphabetlist, letter)
        SecondMess = "Unused letters: {}"
        print(SecondMess.format(unusedletterString)) 
        letter = input("Input letter:")
        print (letter)
        letter = checkletter(letter)
        usedletterList.append(letter)       
            
        if letter not in word: # lose case
            guesscount = guesscount - 1        
            if guesscount == 0:
                print(FirstMess.format(guesscount, blanks))
                print(SecondMess.format(unusedletterString))
                print("SORRY! YOU ARE HANGED!")
                gamecounter = gamecounter + 1
                break
            
            
   
   
        




            


