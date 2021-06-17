#In
#The program accepts any nymber of integer scores ranging from 0 to 100, with one score
#on each line. Input is terminated by an input score of -1.

#Out
#Print the corresponding letter grade of each numerical score, according to the grading 
#system shown below

x = int(input("x:"))

while True:   
    if (x >= -1 and x <= 100):          
        if (x >= 92 and x <= 100):
            print("A")
            x = int(input("x:"))
        elif(x >= 87 and x <= 91):
            print("B+")
            x = int(input("x:"))
        elif(x >= 83 and x <= 86):
            print("B")
            x = int(input("x:"))
        elif(x >= 79 and x <= 82):
            print("C+")
            x = int(input("x:"))
        elif(x >= 75 and x <= 78):
            print("C")
            x = int(input("x:"))
        elif(x >= 70 and x <= 75):
            print("D")
            x = int(input("x:"))
        elif(x >= 0 and x < 70):
            print("F")
            x = int(input("x:"))
        elif(x == -1):
            break
    else:
        x = int(input("x:"))
    

    
    
    
    
    