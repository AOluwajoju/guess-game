import random

def gameMenu():
    scores=[]
    
    with open('highScores.txt', 'r') as highScores:
        for line in highScores:
            scores.append(line.strip().split('\t'))
    

    while True:
        print("\nGuessing Game!")
        print("Menu:")
        print("1. Play")
        print("2. Score Board")
        print("3. Exit")

        menuInput = input('\n Select an option (1, 2 or 3)\n')

        if menuInput=='1':
            playGame(scores)
        elif menuInput=='2':
            scores.sort(key=sorter)
            print("Score Board!")
            print("Name\tAttempts")
            for score in scores:
                print(f"{score[0]}\t{score[1]}")
        elif menuInput=='3':
            print("Thanks for playing!")
            break
        else:
            print("Enter a valid option\n")    
        

def playGame(scores):
    randNum = random.randint(0, 30)
    name= input("Enter your name: ")
    
    attempts = 1
    correctGuess = False
    while attempts < 10 and not correctGuess:
        try:
            guess = input("Guess a number between 1 and 30:\n")
            if int(guess) > 30 or int(guess) < 1:
                print("Out of range")
                continue
            elif int(guess) == randNum:
                print(f"You guessed it in {attempts} tries!")
                correctGuess = True
                scores.append([name, attempts])
                saveScores(scores)
            else:
                print("Wrong. Try again!\n")
                attempts += 1 
                   
        except ValueError:
            print("Enter a valid number")    
    if not (attempts < 10):
        print("\nGame failed! Attempts limit reached!")        

def saveScores(scores):
    scores.sort(key=sorter)
    
    with open('highScores.txt', 'w') as highScores:
        for score in scores[:10]:
            highScores.write(f"{score[0]}\t{score[1]}\n")     
                  
def sorter(list):
        return int(list[1])                
if __name__ == "__main__":
    gameMenu()              