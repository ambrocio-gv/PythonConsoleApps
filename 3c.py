#In
#Given a single word, take the last characted of that word and a print a new word with the last
#character added to the front and the back of the given word, There is no need to change the
#case of the last character. The given word is guaranteed to have at least one character
#Each test case is a line that contains one string, which is the owrd to process.
#Input is terminated by the word STOP.

#Out
#For each test case, print the new word on its own line.

while True:
    S = input("S:")
    if S == "STOP":
        break
    elif not S.isdigit():
        Slist = list(S)
        length = len(Slist)
        Slast = Slist[length-1]
        Slist.insert(0,Slast)
        Slist.append(Slast)
        word = ''.join(Slist)
        print(word)
    

