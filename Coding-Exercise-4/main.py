import random as rd;

def question1():
    print("Starting");
    num = 0;
    while(num != 10):
        print(num, end=' ');
        num += 1;
    print("\nDone");

def question2():
    print("Starting");
    num = -20;
    while(num < 0):
        print(num, end=' ');
        num += 2;
    print("\nDone");

def question3():
    while(True):
        a = input("Enter Number A: ");
        b = input("Enter Number B: ");

        print(f"Value of A to the Power of B is: {a**b}");

def question4():
    sum = 0;
    while(input("Enter Input: ").lower() != "done"):
        sum += rd.randint(1, 100);
        print(sum);
        
def question5():
    secret_num = 50;
    guess = 0;
    count = 0;
    while(guess != secret_num):
        guess = int(input("Enter Guess: "));
        count += 1;
        if(guess > secret_num):
            print("Too High");
        elif(guess < secret_num):
            print("Too Low");
        else:
            print("Correct");
            print(f"It Took You {count} Tries To Guess The Number");

#question1();
#question2();
#question3();
#question4();
#question5();