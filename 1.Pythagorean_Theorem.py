# asks the user for two numbers, a and b, and then calculates the hypotenuse c and print the answer

a = int(input("enter short side "))
print (a)
b = int(input("enter another short side "))
print (b)

c=((a**2)+(b**2)) ** (1/2)
print("hypotenuse = ",c)
