from colorama import *
import random
import time
import os

def deal_or_no_deal_briefcases(): 
   global briefcases #This statement globlazies the briefcase
   global remaining_briefcases #This statement globalizes the remaining breifcases
   briefcases = {} #This statement turns the briefcases into a dictionary
   amount = [0.1, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000] #This statement creates the amount to be put in the briefcases
   for i in range (1,27):
       briefcases[str(i)] = amount.pop(amount.index(random.choice(amount))) #This statement randomozies the amounts in each briefcase
       remaining_briefcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
   return briefcases, remaining_briefcases

multiplayer_mode=input("Type M to play multiplayer mode and N to play single player ")

if multiplayer_mode=='M':


    amount = [0.1, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
    for i in range (1,27):
     winning_amounts = [str(briefcases)[(i)]] = amount.pop(amount.index(random.choice(amount)))
chosen_cases = []
players = []

def print_board():
    global briefcase
    print(" These are the remaining briefcases: ")
    for briefcase in briefcases:
          if briefcase not in chosen_cases:
               print(briefcase, end=' ')
print("\n")

def offer():
     total_winning_amount = sum(winning_amounts)
     average_winning_amount = total_winning_amount / len(briefcases)
     offer_amount = round(average_winning_amount * 0.5, 2)
     return offer_amount

def play_game():
    global player_name
num_players = int(input( "How many players? "))

for i in range(num_players):
          player_name = input(f"What is the player {i+1}'s name? ")
          players.append(player_name)

for player_name in players:
     chosen_case = random.choice(briefcases)
     chosen_cases.append(chosen_case)
     briefcases.remove(chosen_case)
     print(f"{player_name}, your chosen briefcase is: {chosen_case} ")

num_rounds = 6

global round_num
for round_num in range(num_rounds):
     print(f"\n{player_name} , its your turn")
     chosen_briefcase = int(input(" Which briefcase did you choose ? "))
     briefcases.remove(chosen_briefcase)
     winning_amounts = winning_amounts.pop(random.randrange(len(winning_amounts)))
     print(f"\You have won $(winning_amount)!")
     if chosen_briefcase == chosen_cases[player_name]:
        print(f"\n{player_name}, you have won $[prize_amount] and your orginial briefcase is worth ${chosen_briefcase}!")  

if round_num == num_rounds -1:
          print("\n\nFinal Round! ")
          offer_amount = offer()
          for player_num, player in enumerate(players):
               print(f"\n{player_name}, it's your turn! ")
               print_board()
               deal_or_no_deal = input("You have been offered ${offer_amount}. Deal or no deal? ")
               if deal_or_no_deal.lower() == "deal":
                    print(f"\nCongratulations , {player_name}! You have won ${offer_amount}!")
               elif deal_or_no_deal.lower () == "no deal":
                continue
play_game()
if multiplayer_mode == "N":

  
 def list_to_string(lst):
   return ' '.join(map(str, lst)) #This statement returns the remaining briefcases after the user eliminates a briefcase


 def instructions():
   print("This is the game deal or no deal. Every one of the 26 briefcases has a random value from 1 cent to 1 million dollars! To begin, you will pick one briefcase which will be kept safe throughout the game.")
   print("There will be multiple rounds of this game. After every round, the bank will offer you a deal")
   print("If you accept that deal, you win the money. If not you keep playing and eventually either accept an offer, or win the money in either the first briefcase you chose or the last briefcase left.")
   print("Throughout the game, if you feel you have eliminated too many briefcases with high values, just accept the offer and walk away with bundles of cash!")
   print("Let's play!")
   time.sleep(35)
   os.system("clear")
 instructions()
 def deal_or_no_deal_briefcases(): 
   global briefcases #This statement globlazies the briefcase
   global remaining_briefcases #This statement globalizes the remaining breifcases
   briefcases = {} #This statement turns the briefcases into a dictionary
   amount = [0.1, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000] #This statement creates the amount to be put in the briefcases
   for i in range (1,27):
       briefcases[str(i)] = amount.pop(amount.index(random.choice(amount))) #This statement randomozies the amounts in each briefcase
       remaining_briefcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
   return briefcases, remaining_briefcases


 def player_briefcase(remaining_briefcases):
   global chosen_briefcase #This statement globalizes the chosen briefcase
   print("You must pick a briefcase from 1-26 and this briefcases will be kept safe throughout the game. Remember the number of your briefcase as you will need it later. ")
   chosen_briefcase = int(input("Chosen briefcase: "))
   while chosen_briefcase not in range(1, 27): #This statement creates a loop
       print("Sorry. This number is not valid. Please pick again")
       chosen_briefcase = int(input("Chosen briefcase: "))
   remaining_briefcases.remove(chosen_briefcase) #This statement removes the chosen briefcase from remaining briefcases
   print("You chose briefcase " + str(chosen_briefcase)) #This statement shows the briefcase the user eliminated
   return chosen_briefcase, remaining_briefcases




 def get_random_offer():
   return round(random.uniform(10, 120000), 2) #This statement returns an offer from $10 to $120,000

 def deal_or_no_deal(): #round one
  
   briefcases, remaining_briefcases = deal_or_no_deal_briefcases()
   player_briefcase_num, remaining_briefcases = player_briefcase(remaining_briefcases)
   number_of_briefcases_to_eliminate = 6
   while len(remaining_briefcases) >19: #This makes the code run while there are more than 19 briefcases
           briefcases_left = list_to_string(remaining_briefcases)
          
           print("Chose the briefcases to eliminate from the following list")
           print(green(briefcases_left, ("bold"))) #This statement prints the remaining briefcases in green and bold
           briefcase_to_eliminate = int(input("Eliminated briefcase:\n "))
           if briefcase_to_eliminate not in remaining_briefcases: #This statement prints that the user has selected an invalid briefcase
               print("Sorry. Briefcase has already been chosen. Please pick again.")
               time.sleep(6) #This statement displays the message for six seconds
               os.system("clear") #This statement clears the writing after the time has finished 
               continue
           remaining_briefcases.remove(briefcase_to_eliminate)
           if str(briefcase_to_eliminate) in briefcases:
                briefcase_content = briefcases[str(briefcase_to_eliminate)] #This statement creates the values in each briefcase
                print("You removed briefcase", briefcase_to_eliminate, "which contained $ ", briefcase_content)
                time.sleep(4)
                os.system("clear")
           else:
               print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
   while True: #This statement puts the code in a loop
         offer = get_random_offer()
         print("The bank is thinking of an offer")
         time.sleep(1.5)
         print("The offer is.....")
         time.sleep(1.5)
         print("...")
         time.sleep(1.5)
         print("...")
         time.sleep(1.5)
         print("The bank's offer is: ", offer) #This statement prints the offer from the bank
         print("Please type D to accept this deal and N to decline this deal and keep playing")
         time.sleep(4)
         os.system("clear")
        
         decision = input("Selection: ") #The following code takes the users input to make a decision
         if decision == "D":
                   os.system("clear")
                   print("You have won $ ", offer, "the game has ended!")
                   return get_random_offer
         elif decision == "N":
                   print("You have declined $ ", offer, "let us continue to the next round.")
                   print("The first round has ended. In the second round you will pick 5 briefcases to be eliminated.")
                   time.sleep(8)
                   os.system("clear")
                   break
      
      
   if decision == "N":
           while len(remaining_briefcases) >14: #round 2 
               briefcases_left = list_to_string(remaining_briefcases)
          
               print("Chose the briefcases to eliminate from the following list")
               print(green(briefcases_left, ("bold")))
               briefcase_to_eliminate = int(input("Eliminated briefcase:\n "))
               if briefcase_to_eliminate not in remaining_briefcases:
                   print("Sorry. Briefcase has already been chosen. Please pick again.")
               else:
                   remaining_briefcases.remove(briefcase_to_eliminate)
               if str(briefcase_to_eliminate) in briefcases:
                   briefcase_content = briefcases[str(briefcase_to_eliminate)]
                   print("You removed briefcase", briefcase_to_eliminate, "which contained $ ", briefcase_content)
                   time.sleep(4)
                   os.system("clear")
               else:
                   print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
   while True:
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
      
          decision = input("Selection: ")
          if decision == "D":
                   os.system("clear")
                   print("You have won $ ", offer, "the game has ended!")
                   return get_random_offer
          elif decision== "N":
               print("You have declined $ ", offer, "let us continue to the next round.")
               print("The second round has ended. You will pick 4 to be discarded from the list.")
               time.sleep(5.5)
               break
              
   if decision== "N":
       while len(remaining_briefcases) >10: #round 3
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
                print("You removed briefcase", briefcase_to_eliminate, "which contained $ ", briefcase_content)
                time.sleep(3.5)
                os.system("clear")
           else:
               print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
   while True:
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
      
         decision = input("Selection: ")
         if decision == "D":
                   os.system("clear")
                   print("You have won $ ", offer, "the game has ended!")
                   return get_random_offer
         elif decision== "N":
               print("You have declined $ ", offer, "let us continue to the next round.")
               print("The third round has ended. In the fourth round you will pick 3 briefcases to be eliminated ")
               time.sleep(5.5)
               break
   if decision == "N":
       while len(remaining_briefcases) >7: #round 4
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
                print("You removed briefcase", briefcase_to_eliminate, "which contained $ ", briefcase_content)
                time.sleep(3.5)
                os.system("clear")
           else:
               print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
   while True:
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
      
         decision = input("Selection: ")
         if decision == "D":
                   os.system("clear")
                   print("You have won $ ", offer, "the game has ended!")
                   return get_random_offer
         elif decision== "N":
               print("You have declined $ ", offer, "let us continue to the next round.")
               print("The fourth round has ended. You will now pick 2 briefcase to be discarded from the list.")
               time.sleep(5.5)
               break
   if decision == "N":
       while len(remaining_briefcases) >5:#round 5
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
                print("You removed briefcase", briefcase_to_eliminate, "which contained $ ", briefcase_content)
                time.sleep(4)
                os.system("clear")
           else:
               print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
   while True:
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
      
         decision = input("Selection: ")
         if decision == "D":
                   os.system("clear")
                   print("You have won $ ", offer, "the game has ended!")
                   return get_random_offer
         elif decision== "N":
               print("You have declined $ ", offer, "let us continue to the next round.")
               print("The fifth round has ended. You will now pick 1 briefcase to be discarded from the list.")
               time.sleep(5.5)
               break
   if decision == "N":
       while len(remaining_briefcases) >4: #round 6
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
                print("You removed briefcase", briefcase_to_eliminate, "which contained $ ", briefcase_content)
                time.sleep(6)
                os.system("clear")
           else:
               print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
   while True:
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
      
         decision = input("Selection: ")
         if decision == "D":
                   os.system("clear")
                   print("You have won $ ", offer, "the game has ended!")
                   return get_random_offer
         elif decision== "N":
               print("You have declined $ ", offer, "let us continue to the next round.")
               print("The sixth round has ended. You will now pick 1 briefcase to be discarded from the list.")
               time.sleep(5.5)
               break
   if decision == "N":
       while len(remaining_briefcases) >3: #round 7
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
                print("You removed briefcase", briefcase_to_eliminate, "which contained $ ", briefcase_content)
                time.sleep(4)
                os.system("clear")
           else:
               print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
   while True:
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
      
         decision = input("Selection: ")
         if decision == "D":
                   os.system("clear")
                   print("You have won $ ", offer, "the game has ended!")
                   return get_random_offer
         elif decision== "N":
               print("You have declined $ ", offer, "let us continue to the next round.")
               print("The seventh round has ended. In the eigth round, you will pick one briefcase to be eliminated.")
               time.sleep(5.5)
               break
   if decision == "N":
       while len(remaining_briefcases) >2: #round 8
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
                print("You removed briefcase", briefcase_to_eliminate, "which contained $ ", briefcase_content)
                time.sleep(4)
                os.system("clear")
           else:
               print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
       while True:
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
      
         decision = input("Selection: ")
         if decision == "D":
                   os.system("clear")
                   print("You have won $ ", offer, "the game has ended!")
                   return get_random_offer
         elif decision== "N":
               print("You have declined $ ", offer, "let us continue to the next round.")
               print("The eigth round has ended. In the ninth round you will pick one briefcase to be eliminated")
               time.sleep(5.5)
               break
   
   if decision =="N":
       while len(remaining_briefcases) >1: #round 9
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
                print("You removed briefcase", briefcase_to_eliminate, "which contained $ ", briefcase_content)
                time.sleep(6)
                os.system("clear")
           else:
               print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
   while True:
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
      
         decision = input("Selection: ")
         if decision == "D":
                   os.system("clear")
                   print("You have won $ ", offer, "the game has ended!")
                   return get_random_offer
         elif decision== "N":
               print("You have declined $ ", offer, "let us continue to the next round.")
               print("The ninth round has ended. You will now pick between your original briefcase and the final briefcase.")
               time.sleep(5.5)
               break
   if decision == "N":
    if len(remaining_briefcases) >0: # round 10, This statement runs the code if there is more than 0 briefcases left
           remaining_briefcases.append(chosen_briefcase) #This statement adds users orginial briefcase to the list of briefcases
           briefcases_left = list_to_string(remaining_briefcases)
          
           print(" Your original briefcase has been added to the list. You must pick between your original briefcase and the other briefcase left in the list.")
           print(green(briefcases_left, ("bold"))) #This statement prints the briefcases left after the orginial briefcase has been added back to the list
           print("Type the number of the original briefcase to choose the original briefcase, or the number in the list to choose the remaining briefcase.")
          
           briefcase_won = int(input("Briefcase won:\n ")) #This statement allows the user to type which briefcase they want to win
           if briefcase_won == chosen_briefcase:
               remaining_briefcases.remove(briefcase_won) #This command removes the briefcase 1 from the list 
               print("You have won...")
               time.sleep(1.5)
               print("...")
               time.sleep(1.5)
               print("...")
               time.sleep(1.5)
               print("...")
               time.sleep(1.5)
               briefcase_content = briefcases[str(briefcase_won)] #This statement defines the amount of money in the chosen briefcase
               print("You just won...... $ ", briefcase_content) #This statement prints how much money was in the chosen briefcase
               time.sleep(10)
               os.system("clear")
           elif briefcase_won in remaining_briefcases:
               remaining_briefcases.remove(briefcase_won) #This command removes the chosen briefcase from remaining briefcases


               print("You have won...")
               time.sleep(1.5)
               print("...")
               time.sleep(1.5)
               print("...")
               time.sleep(1.5)
               print("...")
               time.sleep(1.5)
               briefcase_content = briefcases[str(briefcase_won)] #This statement defines the amount of money is the briefcase that is won
               print("You just won...... $ ", briefcase_content) #This statement displays the amounf of money in the briefcases that is won
               time.sleep(10)
               os.system("clear")
           else: #This statement allows the user to pick a briefcase again if their orginial choice was not in the remaining briefcases
                  print("Sorry you have chosen the wrong briefcase please pick again.")
                  briefcase_won = int(input("Briefcase won:" ))
          
deal_or_no_deal() #This statement runs all of the code

tutorial_mode=input("Type T to play tutorial mode:")

if tutorial_mode=='T':
   print("There are 26 briefcases to choose from in the game.Each briefcase holds different cash amount from $0.01 to $1 million.")
   print("At the start, contestant is given 6 briefcases to choose from")
   print("After choosing all 6 briefcases, banker offers a deal. Deal is of high value if the brioefcases chosen are of low-medium value")
   print(" If contestant accepts the offer, game is overand contestant gets the money offered by the banker else game proceeds to round 2 which is 5 briefcases for the contestant to open")
   print("Game continues in multiple rounds until contestant accepts offer or ")
   print("Throughout the game, if you feel you have eliminated too many briefcases with high values, just accept the offer and walk away with bundles of cash!")
   print("Let's play!")
   time.sleep(35)
   os.system("clear")
instructions()
     


     
     
          

               













