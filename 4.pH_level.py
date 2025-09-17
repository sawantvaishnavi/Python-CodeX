import random
ph_level = random.randint(0,14)

print(ph_level)
if ph_level > 7:
    print('Basic')
elif ph_level < 7:
    print('Acidic')  
else:
    print('Neutral')    
