/////////////// Method 1 ///////////////
name = "Radha"
lc= name.lower()
vowel = ["a", "e", "i", "o", "u"]
count = 0

for x in lc:
    if x in vowel:
        print(x)
        count = count + 1
    else:
        count = count
print (count)            



///////////////Method 2 : using function ///////////////  
def count_vowel (name):
    lc = name.lower()
    vowel = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for x in lc:
        if x in vowel:
            count = count + 1
    return count


name = input (str("Enter Name: ")) 
result = count_vowel(name)
print("Total count = ", result)
