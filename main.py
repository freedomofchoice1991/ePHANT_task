# !/usr/bin/env/python3
# Copyright ©rezaKarami

from customer import *
from restaurant import *


def main():

    months = 1
    total_account_state_of_restaurant = 0
    listOfMonthlyMoneyEarned = []

    ## Simulation of Three month:
    while months < 4:
        print (f'\n\n\n******** month number {months} *********\n')
        chanceSingleCustomer = 0.01
        chancePairCustomer = 0.02
        numberOfDays = 1

        everydayNumBusySeats = []
        monthly_statistic_account = []

        while (numberOfDays < 31) :
            today_busy_seats = 0

            for hour in range(0,6):
                singleCustomerCounter = 0
                pairCustomerCounter = 0

                for s in singleCustomerPool:
                    if (random.random() <= chanceSingleCustomer):
                        singleCustomerCounter +=1

                for p in pairCustomerPool:
                    if (random.random() <= chancePairCustomer):
                        pairCustomerCounter +=1 

            today_busy_seats = singleCustomerCounter + (2* pairCustomerCounter)
            print(f'======================month: {months} - day: {numberOfDays}====================')
            print(f'number of single customers: {singleCustomerCounter}')          
            print(f'number of pair customers: {pairCustomerCounter}')  
            print('\nAssuming every single person pays 10 euro per meal and service:') 
            print(f"Today's restaurant account balance:{restaurant_balance + (today_busy_seats* 10)}\n")              

            monthly_statistic_account.append(restaurant_balance + (today_busy_seats* 10))
            everydayNumBusySeats.append(today_busy_seats)
            today_busy_seats = 0   

            numberOfDays += 1

        minBusySeats = min(everydayNumBusySeats)    
        print(f'List of everyday busy seats number in month number {months}: ',everydayNumBusySeats) 
        print(f'\nMinimum number of busy seats of this month: {minBusySeats} on day number {everydayNumBusySeats.index(minBusySeats) + 1}\n\n')   

        print('Monthly account balance statistic:')
        for d in range(0,30):
            print(f'Day number {d+1} earned:',monthly_statistic_account[d])
        print(f'\nThis month sum: {sum(monthly_statistic_account)}')    

        total_account_state_of_restaurant += sum(monthly_statistic_account)
        listOfMonthlyMoneyEarned.append(sum(monthly_statistic_account))
        months += 1   

    print('\n\n----------------------------')
    print(f"List of each last 3 months earned: {listOfMonthlyMoneyEarned}" )
    print(f"Total money earned in 3 month: {total_account_state_of_restaurant}")
    print('----------------------------')

if __name__ == '__main__': main() 


### End
