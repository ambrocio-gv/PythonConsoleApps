#In
#The program accepts any number of integers, one on one on each line, ranging -100 to 100 
#inclusive. Input is terminated by any value that is outside the acceptable range.

#Out
#On a single line, print the sum of all the numbers from the input


x = int(input("x:"))
total = 0
while True:
    
    
    if (x >= -100 and x <= 100):
        total = total + x
        x = int(input("x:"))
        
    else:
        print(total)
        break
         