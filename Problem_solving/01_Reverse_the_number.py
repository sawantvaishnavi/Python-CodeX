//////////////// Method 1  ////////////////
num = int (input ("Enter a number: "))
rev_num = 0


while num > 0 :
    last_digit = num % 10    # to get last digit
    rev_num = rev_num * 10 + last_digit   #creating reverse number
    num = num // 10    #remove last digit

print("Reversed Number is: ", rev_num)    


//////////////// Method 2: Using function ////////////////
def reverse_num (num):
    rev_num = 0
    while num > 0:
        last_digit = num % 10
        rev_num = rev_num * 10 + last_digit
        num = num // 10

    return rev_num

num = int(input("Enter number: "))
result = reverse_num(num)
print("Reversed number : ", result)
