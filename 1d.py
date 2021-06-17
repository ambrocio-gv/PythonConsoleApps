#Input : Input consists of a single positive 8-digit integer.
#Output : Output a single integer on one line: the sum of the digits in the input.

number = input()


while len(number) != 8:    
    number = input()
    
if number.isnumeric() == True:
    number = int(number[0])+int(number[1])+int(number[2])+int(number[3])+int(number[4])+int(number[5])+int(number[6])+int(number[7])
    print(number)

