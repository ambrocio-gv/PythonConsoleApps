#In
#Input consists of a program that determines whether a sequence is a palindrome, consisting og an arbitrary number of test cases.
#Each test case is a single line that containss any number of integers (1<=x<=1000) seorated by spaces.
#Input is terminated by single integer 0.

#Out
#For each test case, output a single line. If the set of numbers in the test case is the same
#when read backwards, out yes. Otherwise, output No.

while True:
    x = input("x:")
    length = len(x)
    last = length -1
    xset = x.split( )
    xlength = len(xset)
    if " " in x and x[last] != " " and x[0] != " ":
        xrev = []
        for i in range(xlength):            
            xset[i] = int(xset[i])            
            xrev.append(i)           
        if 1 <= xset[i] and xset[i] <= 1000:
            j=1
            while j <= xlength:
                xrev[j-1] = xset[xlength-j]
                j=j+1
            if xrev == xset:
                print("Yes")
            elif xrev!= xset:
                print("No")       
    elif (x == "0"):
        break
       
    
    