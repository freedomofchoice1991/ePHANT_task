 
from cmath import sin
import random
from generateRandomCustomerNames import generateName  


class Customer:

    def __init__(self, name, money, type):
        self.name = name
        self.money = money
        self.type = type
    
    def comeInsideRestaurant (self,restaurant_number_of_seats):
        # print('Entered Rest')
        restaurant_number_of_seats -= 1
        return restaurant_number_of_seats
         

    def exitFromRestaurant (self, restaurant_number_of_seats):
        # print('Exited')
        restaurant_number_of_seats += 1
        return restaurant_number_of_seats

    def payTheBill (self,):
        # print('Bill is paied')
        self.money -= 10
        return self.money



##----Generate 2k random customers----

pairCustomerPool = []
singleCustomerPool = []
familyCustomerPool = []
for i in range(1,2001):
    x = 'c'+'i'
    x = Customer(generateName(),random.randint(50,100), type(generateName()))
    if x.type is tuple:
        pairCustomerPool.append(x)
    elif x.type is list:
        familyCustomerPool.append(x)
    else:
        singleCustomerPool.append(x)    

##--------

