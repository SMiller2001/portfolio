#Level 3
from random import *
#Create the list of words you want to choose from.
haiku_five = ["The bird takes a crap", "The flowers are live", "We can survive this", "They will not win this", "It's Nice To See You"]
haiku_seven=["My car takes the worst hit now", "The only way out is up", "Independent List Challenge", "Summer Immersion Program","My Favorite Color is Green" ]
#Generates a random integer.
x = randint(0, len(haiku_five)-1)
y = randint(0, len(haiku_seven)-1)
z = randint(0, len(haiku_five)-1)
#Print statements
print (haiku_five[x])
print (haiku_seven[y])
print (haiku_five[z])


#Level 1
"""
name1 = ["Jaime", "Dylan", "Mary","Lucy","Ryan","Lina","Anne","Vanessa","Peggy", "Destiny", "Faith", "Austin", "Zeke" ]
lol = randint(0, len(name1)-1)
print(name1[lol])
"""
