import main
import login



def high_score(winning_amt):
    game = main.deal_or_no_deal()
    name= login.login()
    earnings={}
    with open("C:\\Users\\high_score.txt", "r") as file:
        for line in file:
            name, earning = line.strip().split(":")
            earnings[name] = float(earning)

    print("High Scores:\n")
   
   
     
    for name, earning in sorted(earnings.items(), key=lambda x:x[1]):
        print(f"{name}: {earning}")

    #name = input("Enter your name: \n")
    print(f"Your High Score from your current game {game}\n")
   

    earnings[name] =game

    with open("C:\\Users\\high_score.txt", "w") as file:
        for name, earning in earnings.items():
            file.write(f"{name}:{earning}\n")
            
# Start the game
def main():
    tutorial_mode= input("Type 'T' to play tutorial mode: ")
    if tutorial_mode=='T':
        high_scores=high_score(main.deal_or_no_deal())              
        return high_scores


       
if __name__ == '__main__':
    main()