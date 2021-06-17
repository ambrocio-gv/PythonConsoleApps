#In
#The input consists of an arbitrary number of cases.
#Each case begines with a single string S from the user, which determines the appropriate
#operation to perform and which function to call.
#String S can be any of these 4 values: negate, add, maximum, or stop.
#if S is "negate", obtain one number from the user, then negate hte number which is
#returned by a function named negate(a).
#if S is "add", obtain twi numbers from the user, then add the two numbers, which is
#returned by a function named add(a,b).
#if S is "maximum", obtain three numbers from the user, then get the largest value among the
#three numbers, which is returned by a function named maximum(a,b,c)
#if S is "stop", the program terminates

#Out
#For each test case, output a single integer on a single line as described in the problem

def negate( x ):
    x = -x
    return x

def add (x, y):
    z = x + y
    return z

def maximum (x, y, z):
    w = max(x, y, z)
    return w

def check (x):    
    while True:        
        try:
            x = int(x)
            if x >= -100 and x <= 100:
                return(x)
            else:
                x = input("input again:")    
        except ValueError:
            x = input("input again:")                  
            
        
while True:    
    S = input("S:")
    if S == "negate":
        a = input("a:")
        a = check(a)
        a = negate(a)
        print (a)
        
    elif S == "add":
        a = input("a:")
        a = check(a)
        b = input("b:")
        b = check(b)
        sum = add(a, b)
        print (sum)
        
        
    elif S == "maximum":
        a = (input("a:"))
        a = check(a)
        b = (input("b:"))
        b = check(b)
        c = (input("c:"))
        c = check(c)
        maxi = maximum(a, b, c) 
        print (maxi)
        
    elif S == "stop":
        break