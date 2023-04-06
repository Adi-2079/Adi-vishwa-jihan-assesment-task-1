def deal_or_no_deal():
    print("This is the game deal or no deal. In this game you will pick briefcases until all of the 26 briefcases have been chosen. you will either earn money via the bank offer or eliminating every briefcases.")
    print("Let's play!")

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
    briefcases1 = briefcases
    offer = 0 
    remaining_briefcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    remaining_briefcases_coloured = [magenta(1, "bold"), magenta(2, "bold"), magenta(3, "bold"), magenta(4, "bold"), magenta(5, "bold"), 
                                        cyan(6, "bright"), cyan(7, "bright"), cyan(8, "bright"), cyan(9, "bright"), cyan(10, "bright"), 
                                        red(11, "bold"), red(12, "bold"), red(13, "bold"), red(14, "bold"), red(15, "bold"),
                                        blue(16, "bold"), blue(17, "bold"), blue(18, "bold"), blue(19, "bold"), blue(20, "bold"),
                                        green(21, "bold"), green(22, "bold"), green(23, "bold"), red(24, "bold"), green(25, "bold"), green(26, "bold")]
     

yay
