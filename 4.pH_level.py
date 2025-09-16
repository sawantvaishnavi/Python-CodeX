# Write an if, elif, else statement that:

# If ph is greater than 7, output "Basic".
# If ph is less than 7, output "Acidic".
# Else, output "Neutral".

import random
ph_level = random.randint(0,14)

print(ph_level)
if ph_level > 7:
    print('Basic')
elif ph_level < 7:
    print('Acidic')  
else:
    print('Neutral')    
