"""
Created on Mon Jan  8 09:40:47 2024

play with dollars

@author: Faeze Afghahi
"""

import random

random.seed()

people =[]
for i in range (0,50):
    people.append(100)
    
#print(people)
for beshkan in range(0,10000):
    for person1 in range(0,50):
        person2 = random.randrange(0,50)
        while people[person2] == 0:
            person2 = random.randrange(0,50)
        if people[person1] != 0:
            #print (person1,person2)
            people[person1] = people[person1]-1
            people[person2] = people[person2]+1


import matplotlib.pyplot as plt
#%matplotlib inline
#people.sort()
plt.bar(range(0,50),sorted(people, reverse=True))
