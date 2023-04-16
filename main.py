from simple_colors import *
import random
import time

def deal_or_no_deal_briefcases():
    global remaining_briefcases
    briefcases = {}
    amount = [0.1, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000 ]
    for i in range(1,27):
        briefcases[str(i)] = amount.pop(amount.index(random.choice(amount)))
        remaining_briefcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    return deal_or_no_deal_briefcases

def list_to_string(list):
    string = ""
    for i in list:
        string += i + " "
    return string

def instructions():
    print("This is the game deal or no deal. To begin you will pick one briefcase that will be yours. The game will progress through many rounds as you eliminate briefcases. You will either win the money in your briefcases or through an offer mmade by the bank.")
    print("Let's play!")
instructions()

def player_briefcase():
    print("You must pick a briefcase and this briefcase will be kept safe throughout the game")
    chosen_briefcase = int(input("Chosen Briefcase:"))
    remaining_briefcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    if chosen_briefcase in remaining_briefcases:
        remaining_briefcases.remove(chosen_briefcase)
        print("You chose briefcase " + str(chosen_briefcase))
player_briefcase()


def get_offer(briefcases):
    offer = sum(briefcases.values()) / len(briefcases)
    offer = round (offer, 2)
    return offer


def deal_no_deal():
    briefcases = deal_or_no_deal_briefcases()
    offer = 0 
    remaining_briefcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    remaining_briefcases_colorgreen = green(1, ('bold')), green(2, ('bold')), green(3, ('bold'),), green(4, ('bold')), green(5, ('bold')), green(6, ('bold')), green(7, ('bold' )), green(8, ('bold')), green(9, ('bold')), green(10, ('bold')), green(11, ('bold')),  green(12, ('bold')),  green(13, ('bold')),  green(14, ('bold')),  green(15, ('bold')), green(16, ('bold')),  green(17, ('bold')),  green(18, ('bold')), green(19, ('bold')),  green(20, ('bold')), green(21, ('bold')),  green(22, ('bold')),  green(23, ('bold')),  green(24, ('bold')),  green(25, ('bold')),  green(26, ('bold'))
    briefcases_eliminate = 6
   
    print("You are required to eliminate " + str(briefcases_eliminate) + " briefcases, please choose them from the list below")
    print(list_to_string(remaining_briefcases_colorgreen))
    
    first_briefcase = int(input("Briefcase: "))
    if first_briefcase in remaining_briefcases:
        remaining_briefcases.remove(first_briefcase)
        print("You removed briefcase " + str(first_briefcase)  " which contained $", briefcases.pop(str(first_briefcase)))
    else:
        print("Sorry, number is not in the list")
    

    print("You are now required to pick 5 more briefcases, please pick another from the new list below")
    print(list_to_string(remaining_briefcases_colorgreen))
    second_briefcase = int(input)
    if second_briefcase in remaining_briefcases:
        remaining_briefcases.remove(second_briefcase)
    else:
        print("Sorry, number is not in the list ")
deal_no_deal()


   


