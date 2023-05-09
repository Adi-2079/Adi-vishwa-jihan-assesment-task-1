def multiplayer():
   global briefcases #This statement globlazies the briefcase
   global remaining_briefcases #This statement globalizes the remaining breifcases
   briefcases = {} #This statement turns the briefcases into a dictionary
   amount = [0.1, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000] #This statement creates the amount to be put in the briefcases
   
 
   briefcases = {}
   amount = [0.1, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
   for i in range (1,27):
       briefcases[str(i)] = amount.pop(amount.index(random.choice(amount)))
       remaining_briefcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
       return briefcases, remaining_briefcases
global amount
multiplayer_mode=input("Type M to play multiplayer mode and N to play single player ")


if multiplayer_mode=='M':


    amount = [0.1, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
    for i in range (1,27):
     winning_amounts = amount.pop(amount.index(random.choice(amount)))
chosen_cases = []
players = []
multiplayer()


def print_board():
    global briefcase
    print(" These are the remaining briefcases: ")
    for briefcase in briefcases:
          if briefcase not in chosen_cases:
               print(briefcase, end=' ')
print("\n")


def play_game():
    global player_name
    num_players = int(input( "How many players? "))


    for i in range(num_players):
          player_name = input(f"What is the player {i+1}'s name? ")
          players.append(player_name)


    for player_name in players:
     chosen_case = int(input("Chosen Briefcase"))
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


if multiplayer_mode != "M":
