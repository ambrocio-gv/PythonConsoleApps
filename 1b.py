#Input: consists of a unit of measurement on one line, followed by two integers a and b,on
#two separate lines.
#The unit will consist of lowercase and uppercase English letters. There will be no spaces in
#the unit. The unit will be at most 100 characters long.

#Output : On a single line, output the sum of a and b, in the following format: [sum][space][unit]

measurement = input("Enter measurement: ")[:100]
while measurement.isalpha() == False:
    measurement = input("Enter measurement again: ")[:100]

a = int(input("Enter a:"))
b = int(input("Enter b:"))
print(str(a + b) + " " + measurement  )

