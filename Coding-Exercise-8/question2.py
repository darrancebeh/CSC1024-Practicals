import random;

def RandomNumGen():
    low = int(input("Enter the lower bound: "));
    high = int(input("Enter the upper bound: "));

    comp_num = random.randint(low, high);
    return comp_num;

def UserGuess():
    guess = int(input("Enter your guess: "));
    return guess;

def GuessCheck(guess,comp_num):
    if guess == comp_num:
        return True;
    else:
        return False;

def main():
    flag = RandomNumGen();
    print("I am thinking of a number...'");
    guess = UserGuess();

    while(GuessCheck(flag, guess) != True):
        print("Wrong Guess!");
        guess = UserGuess();
    print("Correct Guess!");

main();