# !/usr/bin/env/python3
# Copyright ©rezaKarami

restaurant_number_of_seats = 300
restaurant_balance = 0

def restaurantPayCosts (c, restaurant_balance):
    restaurant_balance -= c
    return restaurant_balance

def restaurantGetMoneyFromCustomers (m, restaurant_balance):
    restaurant_balance += m
    return restaurant_balance

def restaurantPlaceCustomers (restaurant_number_of_seats):
    restaurant_number_of_seats -= 1
    return restaurant_number_of_seats
