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
    CustomerTypes = ('S','P','F')
    randomCustomerType = random.choice (CustomerTypes)
    if randomCustomerType == 'S':
        name = randName()
        # print(name)
        return (name)
    elif randomCustomerType == 'P':
        name1 = randName()
        name2 = randName()
        # print(name1,name2)
        return (name1,name2)
    elif randomCustomerType == 'F': 
        listOfFamilyNames = []
        membersOfFamaily = random.randint(3,6)
        for n in range(1,membersOfFamaily+1):
            x = 'name'+'n'
            x = randName()
            listOfFamilyNames.append(x)
        # print(listOfFamilyNames)    
        return listOfFamilyNames    


generateName()
