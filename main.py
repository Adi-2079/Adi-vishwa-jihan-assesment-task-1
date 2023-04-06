from simple_colors import *
import random
def list_to_string(list):
    string = ""
    for i in list:
        string += i + " "
    return string

def deal_or_no_deal():
    print("This is the game deal or no deal. In this game you will pick briefcases until all of the 26 briefcases have been chosen. you will either earn money via the bank offer or eliminating every briefcases.")
    print("Let's play!")
deal_or_no_deal()

def get_offer():
    offer - sum(briefcases.values()) / len(briefcases)
    offer = round (offer, 2)
    return offer

def briefcases():

    briefcases = {}
    amount = [0.1, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000 ]
    for i in range(1,27):
        briefcases[str(i)] = amount.pop(amount.index(random.choice(amount)))
    return briefcases

def deal_no_deal():
    briefcases1 = briefcases()
    offer = 0 
    remaining_briefcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    remaining_briefcases_coloured = [green(1, "bold"), green(2, "bold"), green(3, "bold"), green(4, "bold"), green(5, "bold"), 
                                        green(6, "bold"), green(7, "bold"), green(8, "bold"), green(9, "bold"), green(10, "bold"), 
                                        green(11, "bold"), green(12, "bold"), green(13, "bold"), green(14, "bold"), green(15, "bold"),
                                        green(16, "bold"), green(17, "bold"), green(18, "bold"), green(19, "bold"), green(20, "bold"),
                                        green(21, "bold"), green(22, "bold"), green(23, "bold"), green(24, "bold"), green(25, "bold"), green(26, "bold")]
    print(list_to_string(remaining_briefcases_coloured))
    briefcase_eliminate = 6
    print(" Eliminate " + str(briefcase_eliminate) + " briefcases ")
    first_briefcases = int(input())
    print("You removed breifcase " + str(first_briefcases) + " which contained ", briefcases1.pop(str(first_briefcases)))
    if first_briefcases in briefcases1:
        briefcases1.remove(first_briefcases)
    remaining_briefcases_coloured[first_briefcases - 1] = black(str(first_briefcases), "bold")
    print(list_to_string(remaining_briefcases_coloured))
     
deal_no_deal()