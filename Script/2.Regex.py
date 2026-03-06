#1. To search ERROR in logfile and print the results in terminal
import re
with open ("file2.txt", "r") as file:
    for line in file:
        if re.search(r"ERROR", line):
            print(line)
            

#2. To search ERROR in logfile and write into new output file
import re
with open ("file2.txt", "r") as infile , open ("Summary.txt", "w") as outfile:
    for line in infile:
        if re.search(r"ERROR", line):
            print(line)
            outfile.write(line)


#3. To search ERROR or WARNING
import re
with open ("file2.txt", "r") as infile , open ("Summary.txt", "w") as outfile:
    for line in infile:
        if re.search(r"ERROR|WARNING", line):
            print(line)
            outfile.write(line)
      
#4. To search Slack (VIOLATED) this pattern  -- r"Pattern"  this r means raw string. consider lines as plain text. 
#if name\nAddress is there then that \n will be consider ans just plain text instade of new line.
import re
with open ("file2.txt", "r") as file:
    for line in file:
        if re.search(r"Slack \(VIOLATED\)", line):
            print(line)
            
