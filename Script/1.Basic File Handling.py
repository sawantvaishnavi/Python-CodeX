1.

#open file in read mode
file = open("file1.txt", "r")
#read the content of entrire file
content = file.read()
print (content)

2.
#open file in read mode
file = open("file1.txt", "r")

#read the content of entrire file
lines = file.readlines()
print (lines)

#close file
file.close()


3.
f1 = open("file1.txt", "r")
lines1 = f1.readlines()
f1.close()

f2 = open("file2.txt", "r")
lines2 = f2.readlines()
f2.close()


	4. Using with no need to close file

with open  ("file1.txt", "r") as f1:
    lines1 = f1.readlines()
    print(lines1)
with open ("file2.txt", "r") as f2:
    lines2 = f2.readlines()
    print(lines2)       

Or 

with open ("file1.txt", "r") as f1, open ("file2.txt", "r") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    print(lines1)
    print(lines2)

	5. 

with open ("file1.txt", "r") as f1:
    content = f1.readlines()
    for line in content:
        print(line.strip())
