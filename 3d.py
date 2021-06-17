#In
#Inputs prints a set of strings in revers it consists of an arbitrary number of test cases.
#Each test case starts with a line containing a number N(1<=N<=20).
#The following N lines contain one string each. Input is terminated by a value of -1.

#Out
#For each test case, output the word Case, the case number (starting from 1) and a colon in
#a line. Then print N lines containing the given strings in reverse.
case = 1
i = 1

def check (x):    
    while True:        
        try:
            x = int(x)
            if x >= 1 and x <= 20:
                return(x)
            elif x == -1:
                return(x)
            else:
                x = input("N:")    
        except ValueError:
            x = input("N:")
            
while True:    
    print ("Case " + str(case) + ":")
    case = case + 1
    N = input("N:")
    N = check(N)
    if (N == -1):
        break
    else:         
        ans = []
        for x in range(N):
            ans.append(x)        
        while i <= N:                  
            S = input("S:")
            ans[N-i] = S 
            i = i + 1           
        for x in range(N):             
            print(ans[x])     
    





