#In
#The input conists of an arbitrary number of lines.
#Each line will contain a positive integer N, which denotes the height of one triangle.
#Inout is terminated by a value of -1

#Out
#For each test case, output a triangle with a height of N.
#Output a blank line after every test case.


x = int(input("N:"))
i = 1
while True:
    if x >= 0:
        while i <= x :
            j = 1
            while j <= i:
                print(j, end = " ")
                j = j + 1
            print(" ")
            i = i + 1
        x = int(input("N:")) 
    elif (x == -1):
        break
    else:
       int(input("N:"))     





