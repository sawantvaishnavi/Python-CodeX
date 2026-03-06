# 1. To search ERROR in logfile
import re
with open ("file2.txt", "r") as infile , open ("Summary.txt", "w") as outfile:
    for line in infile:
        if re.search(r"ERROR", line):
            print(line)
            outfile.write(line)


#2. To search ERROR or WARNING
import re
with open ("file2.txt", "r") as infile , open ("Summary.txt", "w") as outfile:
    for line in infile:
        if re.search(r"ERROR|WARNING", line):
            print(line)
            outfile.write(line)
      
