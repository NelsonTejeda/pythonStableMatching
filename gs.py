#Stable Matching
#Created by: Nelson Tejeda
#Date: 11/30/2021
#Purpose: takes as input equal numbers of two types of participants (n men and n women) each participant giving their preference for whom to be matched to among the participants.
#Input: y/n
#Output: people, preferences, realtime prints
import random
import os


females = ["ada","aja","aki","alix","ally","alma","amy", "ann","anna","ara"]
males = ["pete","zane","chet","che","dane","guy","grey","kai","van","jax"]

trueFemales = females.copy()


def randomizeFemales(f):
    c = 0
    while c != len(f):
        ran = random.randint(0,len(f) - 1)
        temp = f[c]
        f[c] = f[ran]
        f[ran] = temp
        c += 1
    return f

def randomizeMales(m):
    c = 0
    while c != len(m):
        ran = random.randint(0,len(m) - 1)
        temp = m[c]
        m[c] = m[ran]
        m[ran] = temp
        c += 1
    return m

# for i in randomizeFemales(females):
#     print(i)
# print("SPACE!!!")
# for k in randomizeMales(males):
#     print(k)


preferences = {
    "pete" : randomizeFemales(females),
    "zane" : randomizeFemales(females),
    "chet" : randomizeFemales(females),
    "che" : randomizeFemales(females),
    "dane" : randomizeFemales(females),
    "guy" : randomizeFemales(females),
    "grey" : randomizeFemales(females),
    "kai" : randomizeFemales(females),
    "van" : randomizeFemales(females),
    "jax" : randomizeFemales(females),

    "ada" : randomizeMales(males),
    "aja" : randomizeMales(males),
    "aki" : randomizeMales(males),
    "alix" : randomizeMales(males),
    "ally" : randomizeMales(males),
    "alma" : randomizeMales(males),
    "amy" : randomizeMales(males),
    "ann" : randomizeMales(males),
    "anna" : randomizeMales(males),
    "ara" : randomizeMales(males)
}

freeList = {
    "pete" : 0,
    "zane" : 0,
    "chet" : 0,
    "che" : 0,
    "dane" : 0,
    "guy" : 0,
    "grey" : 0,
    "kai" : 0,
    "van" : 0,
    "jax" : 0,

    "ada" : 0,
    "aja" : 0,
    "aki" : 0,
    "alix" : 0,
    "ally" : 0,
    "alma" : 0,
    "amy" : 0,
    "ann" : 0,
    "anna" : 0,
    "ara" : 0
}

men = ["pete","zane","chet","che","dane","guy","grey","kai","van","jax"]
itr = len(men) - 1
nextWoman = 0
#set a counter to the men that are free
while(freeList[men[itr]] == 0 and itr >= 0):
    m = men[itr]
    w = preferences[m][nextWoman]
    print(m + " proposes to " + w)
    if(freeList[w] == 0):
        freeList[m] = w
        freeList[w] = m
        print(w + " accepts")
        men.pop(itr)
        itr -= 1
        if(itr == -1):
            break
        print("----------------------------")
    elif(preferences[w].index(m) > preferences[w].index(freeList[w])):
        #setting the guy that got dumped free
        dumped = freeList[w]
        freeList[dumped] = 0
        #assigning the man and woman
        freeList[m] = w
        freeList[w] = m
        #pop the female he already proposed to
        preferences[dumped].pop(0)
        #remove the man that stole the female from the stack
        men.pop(itr)
        #add the man that was dumped back on the stack
        men.append(dumped)
        print(w + " likes " + m + " more, and dumps " + dumped)
        print("----------------------------")
    else:
        print(w + " rejects " + m)
        nextWoman += 1

print("Participants:")
print(males)
print(trueFemales)
print("Preferences:")
print(preferences)
print("Pairings:")
print(freeList)
runAgain = input("Run Again (y)/(n)?")
if(runAgain == "y"):
    os.system('python3 gs.py')
#jax,anna -> van,anna