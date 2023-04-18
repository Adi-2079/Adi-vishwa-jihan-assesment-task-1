from simple_colors import *
import random
import time
import os

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
    print("This is the game deal or no deal. Every briefcase has a random value from 1 cent to 1 million dollars! To begin, you will pick one briefcase which will be kept safe throughout the game.")
    print("There will be multiple rounds of this game. After every round, the bank will offer you a deal")
    print("If you accept that deal, you win the money. If not you keep playing and eventually either accept an offer, or win the money in either the first briefcase you chose or the last briefcase left.")
    print("Throughout the game, if you feel you have eliminated too many briefcases with high values, just accept the offer and walk away with bundles of cash!")
    print("Let's play!")
    time.sleep(25)
    os.system("clear")
instructions()

def player_briefcase(remaining_briefcases):
    global chosen_briefcase
    print("You must pick a briefcase and this briefcases will be kept safe throughout the game")
    chosen_briefcase = int(input("Chosen briefcase: "))
    while chosen_briefcase not in range(1, 27):
        print("Sorry. This number is not valid. Please pick again")
        chosen_briefcase = int(input("Chosen briefcase: "))
    remaining_briefcases.remove(chosen_briefcase)
    print("You chose briefcase " + str(chosen_briefcase))
    return chosen_briefcase, remaining_briefcases


def get_random_offer():
    return round(random.uniform(10000, 250000), 2)



def deal_or_no_deal():
    briefcases, remaining_briefcases = deal_or_no_deal_briefcases()
    player_briefcase_num, remaining_briefcases = player_briefcase(remaining_briefcases)
    number_of_briefcases_to_eliminate = 6
    while len(remaining_briefcases) > 25 - number_of_briefcases_to_eliminate:
        briefcases_left = list_to_string(remaining_briefcases)
        print("Chose a briefcase to eliminate from the following ")
        print(green(briefcases_left, ("bold")))
        briefcase_to_eliminate = int(input("Eliminated briefcase:\n "))
        remaining_briefcases.remove(briefcase_to_eliminate)
        if str(briefcase_to_eliminate) in briefcases:
            briefcase_content = briefcases[str(briefcase_to_eliminate)]
            print("You removed briefcase", briefcase_to_eliminate, "Which contained $ ", briefcase_content)
            briefcases.pop(str(briefcase_to_eliminate))
            time.sleep(4)
            os.system("clear")
        else:
            print("You removed briefcase", briefcase_to_eliminate, "which has already been removed.")
            time.sleep(4)
            os.system("clear")

    if len(remaining_briefcases) == 19:
        offer = get_random_offer()
        print("The bank is thinking of an offer")
        time.sleep(1.5)
        print("The offer is.....")
        time.sleep(1.5)
        print("...")
        time.sleep(1.5)
        print("...")
        time.sleep(1.5)
        print("The bank's offer is: ", offer)
        print("Please type D to accept this deal and N to decline this deal and keep playing")
        time.sleep(4.5)
        os.system("clear")
        acceptance = input("Selection: ")
   
        if acceptance == "D":
                    print("You have won $ ", offer, "the game has ended!")
                    time.sleep(4.5)
                    os.system("clear")
        elif acceptance == "N":
                    print("You have declined $ ", offer, "let us continue to the next round.")
                    print("The first round has ended. You will now pick 5 briefcases to be discarded from the list.")
                    time.sleep(5.5)
                    os.system("clear")
    
    while len(remaining_briefcases) >14:
            briefcases_left = list_to_string(remaining_briefcases)
            
            print("Chose the briefcases to eliminate from the following list")
            print(green(briefcases_left, ("bold")))
            briefcase_to_eliminate = int(input("Eliminated briefcase:\n "))
            if briefcase_to_eliminate not in remaining_briefcases:
                print("Sorry. Briefcase has already been chosen. Please pick again.")
                continue
            remaining_briefcases.remove(briefcase_to_eliminate)
            if str(briefcase_to_eliminate) in briefcases:
                 briefcase_content = briefcases[str(briefcase_to_eliminate)]
                 print("You removed briefcase", briefcase_to_eliminate, "Which contained $ ", briefcase_content)
                 time.sleep(4.5)
                 os.system("clear")
            else:
                print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
    offer = get_random_offer()
    print("The bank is thinking of an offer")
    time.sleep(1.5)
    print("The offer is.....")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("The bank's offer is: ", offer) 
    print("Please type D to accept this deal and N to decline this deal and keep playing")
    time.sleep(3.5)
    os.system("clear")
    acceptance = input("Selection: ")
    if acceptance == "D":
            print("You have won $ ", offer, "the game has ended!")
            time.sleep(3.5)
            os.system("clear")
    elif acceptance == "N":
                print("You have declined $ ", offer, "let us continue to the next round.")
                print("The second round has ended. You will now pick 4 briefcases to be discarded from the list.")
                time.sleep(5.5)
                

    while len(remaining_briefcases) >10:
            briefcases_left = list_to_string(remaining_briefcases)
            
            print("Chose the briefcases to eliminate from the following list")
            print(green(briefcases_left, ("bold")))
            briefcase_to_eliminate = int(input("Eliminated briefcase:\n "))
            if briefcase_to_eliminate not in remaining_briefcases:
                print("Sorry. Briefcase has already been chosen. Please pick again.")
                time.sleep(4.5)
                os.system("clear")
                continue
            remaining_briefcases.remove(briefcase_to_eliminate)
            if str(briefcase_to_eliminate) in briefcases:
                 briefcase_content = briefcases[str(briefcase_to_eliminate)]
                 print("You removed briefcase", briefcase_to_eliminate, "Which contained $ ", briefcase_content)
                 time.sleep(3.5)
                 os.system("clear")
            else:
                print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
    offer = get_random_offer()
    print("The bank is thinking of an offer")
    time.sleep(1.5)
    print("The offer is.....")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("The bank's offer is: ", offer) 
    print("Please type D to accept this deal and N to decline this deal and keep playing")
    time.sleep(3.5)
    os.system("clear")
    acceptance = input("Selection: ")
    if acceptance == "D":
            print("You have won $ ", offer, "the game has ended!")
            time.sleep(3.5)
            os.system("clear")
    elif acceptance == "N":
                print("You have declined $ ", offer, "let us continue to the next round.")
                print("The third round has ended. In the fourth round, you will eliminate 3 briefcases.")
                time.sleep(5.5)
                os.system("clear")
    
    while len(remaining_briefcases) >7:
            briefcases_left = list_to_string(remaining_briefcases)
            
            print("Chose the briefcases to eliminate from the following list")
            print(green(briefcases_left, ("bold")))
            briefcase_to_eliminate = int(input("Eliminated briefcase:\n "))
            if briefcase_to_eliminate not in remaining_briefcases:
                print("Sorry. Briefcase has already been chosen. Please pick again.")
                time.sleep(4.5)
                os.system("clear")
                continue
            remaining_briefcases.remove(briefcase_to_eliminate)
            if str(briefcase_to_eliminate) in briefcases:
                 briefcase_content = briefcases[str(briefcase_to_eliminate)]
                 print("You removed briefcase", briefcase_to_eliminate, "Which contained $ ", briefcase_content)
                 time.sleep(3.5)
                 os.system("clear")
            else:
                print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
    offer = get_random_offer()
    print("The bank is thinking of an offer")
    time.sleep(1.5)
    print("The offer is.....")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("The bank's offer is: ", offer) 
    print("Please type D to accept this deal and N to decline this deal and keep playing")
    time.sleep(3.5)
    os.system("clear")
    acceptance = input("Selection: ")
    if acceptance == "D":
            print("You have won $ ", offer, "the game has ended!")
            time.sleep(3.5)
            os.system("clear")
    elif acceptance == "N":
                print("You have declined $ ", offer, "let us continue to the next round.")
                print("The fourth round has ended. In the fifth round, you will eliminate 2 briefcases")
                time.sleep(5.5)
                os.system("clear")
    while len(remaining_briefcases) >5:
            briefcases_left = list_to_string(remaining_briefcases)
            
            print("Chose the briefcases to eliminate from the following list")
            print(green(briefcases_left, ("bold")))
            briefcase_to_eliminate = int(input("Eliminated briefcase:\n "))
            if briefcase_to_eliminate not in remaining_briefcases:
                print("Sorry. Briefcase has already been chosen. Please pick again.")
                time.sleep(3.5)
                os.system("clear")
                continue
            remaining_briefcases.remove(briefcase_to_eliminate)
            if str(briefcase_to_eliminate) in briefcases:
                 briefcase_content = briefcases[str(briefcase_to_eliminate)]
                 print("You removed briefcase", briefcase_to_eliminate, "Which contained $ ", briefcase_content)
                 time.sleep(4)
                 os.system("clear")
            else:
                print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
    offer = get_random_offer()
    print("The bank is thinking of an offer")
    time.sleep(1.5)
    print("The offer is.....")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("The bank's offer is: ", offer) 
    print("Please type D to accept this deal and N to decline this deal and keep playing")
    time.sleep(3.5)
    os.system("clear")
    acceptance = input("Selection: ")
    if acceptance == "D":
                    print("You have won $ ", offer, "the game has ended!")
                    time.sleep(6)
                    os.system("clear")
    elif acceptance == "N":
                    print("You have declined $ ", offer, "let us continue to the next round.")
                    print("The fifth round has ended. In the sixth round you will eliminate one briefcase.")
                    time.sleep(5.5)
                    os.system("clear")

    while len(remaining_briefcases) >4:
            briefcases_left = list_to_string(remaining_briefcases)
            
            print("Chose the briefcases to eliminate from the following list")
            print(green(briefcases_left, ("bold")))
            briefcase_to_eliminate = int(input("Eliminated briefcase:\n "))
            if briefcase_to_eliminate not in remaining_briefcases:
                print("Sorry. Briefcase has already been chosen. Please pick again.")
                time.sleep(6)
                os.system("clear")
                continue
            remaining_briefcases.remove(briefcase_to_eliminate)
            if str(briefcase_to_eliminate) in briefcases:
                 briefcase_content = briefcases[str(briefcase_to_eliminate)]
                 print("You removed briefcase", briefcase_to_eliminate, "Which contained $ ", briefcase_content)
                 time.sleep(6)
                 os.system("clear")
            else:
                print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
    offer = get_random_offer()
    print("The bank is thinking of an offer")
    time.sleep(1.5)
    print("The offer is.....")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("The bank's offer is: ", offer) 
    print("Please type D to accept this deal and N to decline this deal and keep playing")
    time.sleep(3.5)
    os.system("clear")
    acceptance = input("Selection: ")
    if acceptance == "D":
                    print("You have won $ ", offer, "the game has ended!")
                    time.sleep(4)
                    os.system("clear")
    elif acceptance == "N":
                    print("You have declined $ ", offer, "let us continue to the next round.")
                    print("The sixth round has ended. In the seventh round you will eliminate one briefcase.")
                    time.sleep(4.5)
                    os.system("clear")

    while len(remaining_briefcases) >3:
            briefcases_left = list_to_string(remaining_briefcases)
            
            print("Chose the briefcases to eliminate from the following list")
            print(green(briefcases_left, ("bold")))
            briefcase_to_eliminate = int(input("Eliminated briefcase:\n "))
            if briefcase_to_eliminate not in remaining_briefcases:
                print("Sorry. Briefcase has already been chosen. Please pick again.")
                time.sleep(6)
                os.system("clear")
                continue
            remaining_briefcases.remove(briefcase_to_eliminate)
            if str(briefcase_to_eliminate) in briefcases:
                 briefcase_content = briefcases[str(briefcase_to_eliminate)]
                 print("You removed briefcase", briefcase_to_eliminate, "Which contained $ ", briefcase_content)
                 time.sleep(4)
                 os.system("clear")
            else:
                print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
    offer = get_random_offer()
    print("The bank is thinking of an offer")
    time.sleep(1.5)
    print("The offer is.....")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("The bank's offer is: ", offer) 
    print("Please type D to accept this deal and N to decline this deal and keep playing")
    time.sleep(4)
    os.system(clear)
    acceptance = input("Selection: ")
    if acceptance == "D":
                    print("You have won $ ", offer, "the game has ended!")
                    time.sleep(6)
                    os.system("clear")
    elif acceptance == "N":
                    print("You have declined $ ", offer, "let us continue to the next round.")
                    print("The seventh round has ended. In the eight round you will pick one briefcase to be eliminated.")
                    time.sleep(12)
                    os.system("clear")

    while len(remaining_briefcases) >2:
            briefcases_left = list_to_string(remaining_briefcases)
            
            print("Chose the briefcases to eliminate from the following list")
            print(green(briefcases_left, ("bold")))
            briefcase_to_eliminate = int(input("Eliminated briefcase:\n "))
            if briefcase_to_eliminate not in remaining_briefcases:
                print("Sorry. Briefcase has already been chosen. Please pick again.")
                time.sleep(6)
                os.system("clear")
                continue
            remaining_briefcases.remove(briefcase_to_eliminate)
            if str(briefcase_to_eliminate) in briefcases:
                 briefcase_content = briefcases[str(briefcase_to_eliminate)]
                 print("You removed briefcase", briefcase_to_eliminate, "Which contained $ ", briefcase_content)
                 time.sleep(4)
                 os.system("clear")
            else:
                print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
    offer = get_random_offer()
    print("The bank is thinking of an offer")
    time.sleep(1.5)
    print("The offer is.....")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("The bank's offer is: ", offer) 
    print("Please type D to accept this deal and N to decline this deal and keep playing")
    time.sleep(4)
    os.system("clear")
    acceptance = input("Selection: ")
    if acceptance == "D":
                    print("You have won $ ", offer, "the game has ended!")
                    time.sleep(6)
                    os.system("clear")
    elif acceptance == "N":
                    print("You have declined $ ", offer, "let us continue to the next round.")
                    print("The eighth round has ended. In the ninth round you will pick one briefcase to be discarded")
                    time.sleep(11)
                    os.system("clear")
    while len(remaining_briefcases) >1:
            briefcases_left = list_to_string(remaining_briefcases)
            
            print("Chose the briefcases to eliminate from the following list")
            print(green(briefcases_left, ("bold")))
            briefcase_to_eliminate = int(input("Eliminated briefcase:\n "))
            if briefcase_to_eliminate not in remaining_briefcases:
                print("Sorry. Briefcase has already been chosen. Please pick again.")
                time.sleep(4.5)
                os.system("clear")
                continue
            remaining_briefcases.remove(briefcase_to_eliminate)
            if str(briefcase_to_eliminate) in briefcases:
                 briefcase_content = briefcases[str(briefcase_to_eliminate)]
                 print("You removed briefcase", briefcase_to_eliminate, "Which contained $ ", briefcase_content)
                 time.sleep(6)
                 os.system("clear")
            else:
                print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
    offer = get_random_offer()
    print("The bank is thinking of an offer")
    time.sleep(1.5)
    print("The offer is.....")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("The bank's offer is: ", offer) 
    print("Please type D to accept this deal and N to decline this deal and keep playing")
    time.sleep(4)
    os.system("clear")
    acceptance = input("Selection: ")
    if acceptance == "D":
                    print("You have won $ ", offer, "the game has ended!")
                    time.sleep(6)
                    os.system("clear")
    elif acceptance == "N":
                    print("You have declined $ ", offer, "let us continue to the next round.")
                    print("The ninth round has ende. In the last round, you will discard one briefcase and either pick between your original briefcase or the one that remains. Choose wisely.")
                    time.sleep(18)
                    os.system("clear")

    while len(remaining_briefcases) >0:
            briefcases_left = list_to_string(remaining_briefcases)
            
            print("There is one briefcase left in the list. You must pick between your original briefcase and the last briefcase left in the list.")
            print(green(briefcases_left, ("bold")))
            print("Type the number of the original briefcase to choose the original briefcase, and the number in the list to choose the remaining briefcase.")
            
            briefcase_won = int(input("Briefcase won:\n "))
            if briefcase_won == chosen_briefcase:
                print("You have won...")
                time.sleep(1.5)
                print("...")
                time.sleep(1.5)
                print("...")
                time.sleep(1.5)
                print("...")
                time.sleep(1.5)
                briefcase_content = briefcases[str(briefcase_won)]
                print("You just won...... $ ", briefcase_content)
            else:
                briefcase_won == remaining_briefcases
                print("You have won...")
                time.sleep(1.5)
                print("...")
                time.sleep(1.5)
                print("...")
                time.sleep(1.5)
                print("...")
                time.sleep(1.5)
                briefcase_content = briefcases[str(briefcase_won)]
                print("You just won...... $ ", briefcase_content)
            
deal_or_no_deal()





    













   


