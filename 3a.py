#In
#The first line of input consists of an integer N, representing the number of test cases.
#Each test case is composed of two lines, each containing a positive integer. These two
#integers represent Hashmat and is compared to his opponent by using a function named
#difference(a, b), which returns the difference between a and b, by sybtracting the smaller
#number from the larger number 

#Out
#For each test case, output the difference in strength between Hasmat and his opponent
#on a separate line.



N = int(input("N:"))
i = 1
def difference( a, b ):   
    if a >= b:
        diff = a - b
    elif b > a:
        diff = b - a        
    return diff

def check (x):    
    while True:        
        try:
            x = int(x)
            if x >= 0:
                return(x)
            else:
                x = input("input again:")    
        except ValueError:
            x = input("input again:") 

while True:    
    while (i <= N):
        a = (input("a:"))
        a = check(a)
        b = (input("b:"))
        b = check(b)
        diff = difference(a , b)
        print (diff)
        i = i + 1       
    break        
        
    
    
    