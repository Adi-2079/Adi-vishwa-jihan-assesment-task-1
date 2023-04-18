from simple_colors import *
import random
import time

def deal_or_no_deal_briefcases():
    global briefcases 
    global remaining_briefcases
    briefcases = {}
    amount = [0.1, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
    for i in range (1,27):
        briefcases[str(i)] = amount.pop(amount.index(random.choice(amount))) 
        remaining_briefcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
        return briefcases, remaining_briefcases
    
def list_to_string(lst):
    return ' '.join(map(str, lst))

def instructions():
    print("This is the game deal or no deal. To begin, you will pick one briefcase which will be kept safe throughout the game.")
    print("There will be multiple rounds of this game. After every round, the bank will offer you a deal")
    print("If you accept that deal, you win the money. If not you keep playing and eventually win the money in the first briefcase you chose")
    print("Let's play!")

def player_briefcase(remaining_briefcases):
    print("You must pick a briefcase and this briefcases will be kept safe throughout the game")
    chosen_briefcase = int(input("Chosen briefcase: "))
    while chosen_briefcase not in range(1, 27):
        print("Sorry. This number is not valid. Please pick again")
        chosen_briefcase = int(input("Chosen briefcase: "))
    remaining_briefcases.remove(chosen_briefcase)
    print("You chose briefcase " + str(chosen_briefcase))
    return chosen_briefcase, remaining_briefcases

def get_offer(briefcases):
    offer = sum(briefcases.values()) / len(briefcases)
    return round(offer, 2)

def deal_or_no_deal():
    briefcases, remaining_briefcases = deal_or_no_deal_briefcases()
    player_briefcase_num, remaining_briefcases = player_briefcase(remaining_briefcases)
    while len(remaining_briefcases) > 19:
        briefcases_left = list_to_string(remaining_briefcases)
        print("Chose a briefcase to eliminate from the following ")
        print(green(briefcases_left, ("bold")))
        briefcase_to_eliminate = int(input("Eliminated briefcase:\n "))
        if briefcase_to_eliminate not in remaining_briefcases:
            print("Sorry. Briefcase has already been chosen. Please pick again.")
            continue
        remaining_briefcases.remove(briefcase_to_eliminate)
        print("Briefcase value is $ " + str(briefcases[str(briefcase_to_eliminate)]))
deal_or_no_deal()









   


