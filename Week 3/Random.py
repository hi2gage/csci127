import random

def main():

    number_guesses = 0
    answer = random.randint(1,10)
    guess = 0
    
    while (guess != answer):
        guess = int(input("Enter your guess[1,10}"))
        number_guesses += 1
    
    print("congratulations! It took you", number_guesses, "guesses")
main()
