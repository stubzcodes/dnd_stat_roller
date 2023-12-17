import random

stats = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

i = 0

#Roll 4d6 for each D&D stat and remove the lowest result

while i < len(stats):
    stat = stats[i]
    
    roll_count  = 0
    rolls = []
    
    while roll_count < 4 :
        rolls.append(random.randint(1,6))
        roll_count += 1
        
    total = sum(rolls) - min(rolls)
    
    print(f'{stat}: {total}')
        
    i += 1



    
