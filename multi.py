import random

def board(briefcases, chosen_cases):
    print("Here are the remaining briefcases:")
    for briefcase in briefcases:
        if briefcase not in chosen_cases:
            print(briefcase, end=' ')
    print("\n")


def offer(prize_amounts):
    total_prize_amount = sum(prize_amounts)
    average_prize_amount = total_prize_amount / len(briefcases)
    offer_amount = round(average_prize_amount * 0.5, 2)
    return offer_amount

def variables():
    global briefcases
    global prize_amounts
    global chosen_cases
    global players
    briefcases = list(range(1, 27))
    prize_amounts = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
    chosen_cases = []
    players = []





def play_game():
    print("""
                                                                  
@@@@@@@   @@@@@@@@   @@@@@@   @@@           @@@@@@   @@@@@@@   
@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@          @@@@@@@@  @@@@@@@@  
@@!  @@@  @@!       @@!  @@@  @@!          @@!  @@@  @@!  @@@  
!@!  @!@  !@!       !@!  @!@  !@!          !@!  @!@  !@!  @!@  
@!@  !@!  @!!!:!    @!@!@!@!  @!!          @!@  !@!  @!@!!@!   
!@!  !!!  !!!!!:    !!!@!!!!  !!!          !@!  !!!  !!@!@!    
!!:  !!!  !!:       !!:  !!!  !!:          !!:  !!!  !!: :!!   
:!:  !:!  :!:       :!:  !:!   :!:         :!:  !:!  :!:  !:!  
 :::: ::   :: ::::  ::   :::   :: ::::     ::::: ::  ::   :::  
:: :  :   : :: ::    :   : :  : :: : :      : :  :    :   : :  
                                                               
                                                               
@@@  @@@   @@@@@@      @@@@@@@   @@@@@@@@   @@@@@@   @@@       
@@@@ @@@  @@@@@@@@     @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@       
@@!@!@@@  @@!  @@@     @@!  @@@  @@!       @@!  @@@  @@!       
!@!!@!@!  !@!  @!@     !@!  @!@  !@!       !@!  @!@  !@!       
@!@ !!@!  @!@  !@!     @!@  !@!  @!!!:!    @!@!@!@!  @!!       
!@!  !!!  !@!  !!!     !@!  !!!  !!!!!:    !!!@!!!!  !!!       
!!:  !!!  !!:  !!!     !!:  !!!  !!:       !!:  !!!  !!:       
:!:  !:!  :!:  !:!     :!:  !:!  :!:       :!:  !:!   :!:      
 ::   ::  ::::: ::      :::: ::   :: ::::  ::   :::   :: ::::  
::    :    : :  :      :: :  :   : :: ::    :   : :  : :: : :  
                                                               
                                                                             
@@@@@@@@@@   @@@  @@@  @@@       @@@@@@@  @@@  @@@@@@@   @@@        @@@@@@   
@@@@@@@@@@@  @@@  @@@  @@@       @@@@@@@  @@@  @@@@@@@@  @@@       @@@@@@@@  
@@! @@! @@!  @@!  @@@  @@!         @@!    @@!  @@!  @@@  @@!       @@!  @@@  
!@! !@! !@!  !@!  @!@  !@!         !@!    !@!  !@!  @!@  !@!       !@!  @!@  
@!! !!@ @!@  @!@  !@!  @!!         @!!    !!@  @!@@!@!   @!!       @!@!@!@!  
!@!   ! !@!  !@!  !!!  !!!         !!!    !!!  !!@!!!    !!!       !!!@!!!!  
!!:     !!:  !!:  !!!  !!:         !!:    !!:  !!:       !!:       !!:  !!!  
:!:     :!:  :!:  !:!   :!:        :!:    :!:  :!:        :!:      :!:  !:!  
:::     ::   ::::: ::   :: ::::     ::     ::   ::        :: ::::  ::   :::  
 :      :     : :  :   : :: : :     :     :     :        : :: : :   :   : :  
                                                                             
                                                                           
@@@ @@@  @@@@@@@@  @@@@@@@      @@@@@@@@@@    @@@@@@   @@@@@@@   @@@@@@@@  
@@@ @@@  @@@@@@@@  @@@@@@@@     @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  
@@! !@@  @@!       @@!  @@@     @@! @@! @@!  @@!  @@@  @@!  @@@  @@!       
!@! @!!  !@!       !@!  @!@     !@! !@! !@!  !@!  @!@  !@!  @!@  !@!       
 !@!@!   @!!!:!    @!@!!@!      @!! !!@ @!@  @!@  !@!  @!@  !@!  @!!!:!    
  @!!!   !!!!!:    !!@!@!       !@!   ! !@!  !@!  !!!  !@!  !!!  !!!!!:    
  !!:    !!:       !!: :!!      !!:     !!:  !!:  !!!  !!:  !!!  !!:       
  :!:    :!:       :!:  !:!     :!:     :!:  :!:  !:!  :!:  !:!  :!:       
   ::     :: ::::  ::   :::     :::     ::   ::::: ::   :::: ::   :: ::::  
   :     : :: ::    :   : :      :      :     : :  :   :: :  :   : :: ::   
                                                                                                     """)
         # Ask for the number of players
    num_players = int(input("How many players? "))
    for i in range(num_players):
        player_name = input(f"What is player {i+1}'s name? ")
        players.append(player_name)

    for player_name in players:
        chosen_case = random.choice(briefcases)
        chosen_cases.append(chosen_case)
        briefcases.remove(chosen_case)
        print(f"{player_name}, your chosen briefcase is: {chosen_case}")

    num_rounds = 6
    for round_num in range(num_rounds):
        print(f"\n\nRound {round_num+1}")
        board(briefcases, chosen_cases)
        for player_num, player_name in enumerate(players):
            if player_name not in chosen_cases:
                print(f"\n{player_name}, it's your turn!")
                chosen_briefcase = int(input("Which briefcase do you choose? "))
                briefcases.remove(chosen_briefcase)
                prize_amount = prize_amounts.pop(random.randrange(len(prize_amounts)))
                print(f"You have eliminated ${prize_amount}!")
                if chosen_briefcase == chosen_cases[player_num]:
                    print(f"\n{player_name}, you have won ${prize_amount} and your original briefcase is worth ${chosen_briefcase}!")
                    chosen_cases.remove(chosen_briefcase)

    print("\n\nGame Over!")
    print("Here are the final offers for each player:")
    for player_name in players:
        while player_name not in chosen_cases:
            player_offer = offer(prize_amounts)
            print(f"{player_name}, the offer is: ${player_offer}")
            decision = input("Do you accept the offer? (yes/no) ")
            if decision.lower() == "yes":
                print(f"{player_name}, you have accepted the offer!")
                break
            else:
                print(f"{player_name}, you have declined the offer!")
                chosen_briefcase = int(input("Which briefcase do you choose? "))
                briefcases.remove(chosen_briefcase)
                prize_amount = prize_amounts.pop(random.randrange(len(prize_amounts)))
                print(f"\n{player_name}, you have eliminated ${prize_amount}!")
                if chosen_briefcase == chosen_cases[player_num]:
                    print(f"\n{player_name}, you have won ${prize_amount} and your original briefcase is worth ${chosen_briefcase}!")
                    chosen_cases.remove(chosen_briefcase)

# Initialize game variables
variables()

# Start the game










