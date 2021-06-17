#In
#Print a pyramid using only while loops
#The input consists of an arbitrary number of lines.
#Each line will contain a positive integer N, which denotes the row number with the most number of asterisks.
#Input is terminated by a value of -1.

#Out
#Print the diamonds representing each of the values of N in the input.
#Each diamond should be separated by a blank line.
#There should also be only one blank line after the last diamond.




x = int(input("Please enter the amount of rows: "))

row = 0
while(row < x):
    row += 1
    spaces = x - row

    spaces_count = 0
    while(spaces_count < spaces):
        print(" ", end='')
        spaces_count += 1

    stars = 2*row-1
    while(stars > 0):
        print("*", end='')
        stars -= 1

    print()

