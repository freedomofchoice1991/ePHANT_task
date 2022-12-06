import random
import string

def randName ():
    randomNameLength = (6,7,8,9,10,11,12,13)
    L = random.choice(randomNameLength)
    res = ''
    for i in range (1,L):
        res += random.choice(string.ascii_letters)
    return(res)    

#=======

def generateName ():  
    CustomerTypes = ('S','P')
    randomCustomerType = random.choice (CustomerTypes)
    if randomCustomerType == 'S':
        name = randName()
        return (name)
    else:
        name1 = randName()
        name2 = randName()
        return (name1,name2)

generateName()
