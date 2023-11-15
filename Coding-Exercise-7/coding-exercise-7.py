import random;

def question1():
    num = int(input("Enter a number between 1 and 12: "));

    print(f"Displaying Multiplication Table for {num}\n");
    for i in range(1, 13):
        print(f"1 x {num} = {i * num}")


def question2():
    num = int(input("Enter a number below 50: "));

    for i in range(50, num - 1, -1):
        print(i);


def question3():
    direction = input("Enter direction to count (up/down): ").lower();

    if(direction == "up"):
        num = int(input("Input the top number: "));
        print(f"\nCounting up from 1 to {num}\n")
        for i in range(1, num + 1):
            print(i);
    
    elif(direction == "down"):
        num = int(input("Enter a number below 20: "));
        print(f"\nCounting down from 20 to {num}\n")
        for i in range(20, num - 1, -1):
            print(i);


def question4():
    score = 0 ;
    for i in range(0,5):
        num1 = random.randint(1,100);
        num2 = random.randint(1,100);

        sum = num1 + num2;

        ques = int(input(f"{num1} + {num2} = "));

        if(ques == sum):
            print("Correct!");
            score += 1;
        else:
            print(f"Incorrect! The answer was {sum}");

    print("\n\nQuiz Over!");
    print(f"Your score is {score} out of 5");


def question5():
    #Same code as question 4 because I used for-loop to begin with
    score = 0 ;
    for i in range(0,5):
        num1 = random.randint(1,100);
        num2 = random.randint(1,100);

        sum = num1 + num2;

        ques = int(input(f"{num1} + {num2} = "));

        if(ques == sum):
            print("Correct!");
            score += 1;
        else:
            print(f"Incorrect! The answer was {sum}");

    print("\n\nQuiz Over!");
    print(f"Your score is {score} out of 5");
    

def question6():
    my_list = [];
    print("A program to find the maximum and minimum numbers in a list.");
    print("Enter ten (10) numbers into a list.\n")

    for i in range(0, 10):
        num = int(input("Input a number: "));
        my_list.append(num);
    
    ceiling = my_list[0]; #temp variable for highest number
    floor = my_list[0]; #temp variable for lowest number

    for item in my_list:
        if item > ceiling:
            ceiling = item;
        if item < floor:
            floor = item;

    print(f"\n\nmy_list = {my_list}");
    print(f"\nMaximum Number: {ceiling}");
    print(f"Minimum Number: {floor}");


#question1()
#question2()
#question3()
#question4()
#question5()
#question6()
