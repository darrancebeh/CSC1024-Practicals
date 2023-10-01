'''
Exercises are done in functional formatting.
This is done for better visibility and so that all solutions can be compiled into a single Python file.
To run solutions, insert "{function_name}()", where function_name is x in the lines "def x():" at the start of every function; eg: question_1().
Thank you :)
'''

def question_1():
#Optimal solution prompts for use of Dictionaries but to conform to the syllabus, I will instead code it in the "traditional" form.
    newVideos = int(input("Number of New Videos Rented: "));
    newVideosTime = int(input("Number of Days of New Videos Rented: "));

    oldies = int(input("Number of Oldies Rented: "));
    oldiesTime = int(input("Number of Days of Oldies Rented: "));

    print(f"The Total Cost for Rental is: ${(newVideos * newVideosTime * 3) + (oldies * oldiesTime * 2)}.");

def question_2():
#Just a Math Question :)
    seconds = int(input("Enter the number of seconds: "));
    hours = seconds // 3600;
    minutes = (seconds % 3600) // 60;
    seconds = (seconds % 3600) % 60;
    print(f"{hours}:{minutes}:{seconds}.");

def question_3():
#Woohoo Conditional Statementssss
    income = int(input("Please Input your Income in RM: "));
    if income <= 2500:
        tax = 0;
    
    elif income <= 10000:
        tax = income*0.05;
    
    elif income <= 50000:
        tax = income*0.15;

    else:
        tax = income*0.25;

    print(f"Your Income is RM{income}. Your Total Taxes Would Be RM{tax}.");

def question_4():
#Just buy unlimited data lah
    dataUsage = int(input("Please Input your Monthly Data Usage in GB: "));
    if dataUsage <= 10:
        dataCharge = dataUsage * 15;
    else:
        dataCharge = dataUsage * 30;

    print(f"Your Monthly Data Usage is {dataUsage}GB. Your Total Data Charges This Month Would Be RM{dataCharge}.");

def question_5():
#This type of question again walao

    #Pro tip - add .lower() to the end of input() to make it case-insensitive :) ( helps with the if statements A LOT )
    choice = input("Please Input your Choice of Polygon Area to Calculate\n('R' or 'r' for Rectangle; 'C' or 'c' for Circle.): ").lower();

    if choice == 'r':
        length = int(input("Please Input the Length of the Rectangle: "));
        width = int(input("Please Input the Width of the Rectangle: "));
        print(f"The Area of the Rectangle is {length*width}.");

    elif choice == 'c':
        radius = int(input("Please Input the Radius of the Circle: "));
        print(f"The Area of the Circle is {3.14159*radius**2}.");


def question_6():
#wtf is this question
# if you're getting errors, please update python to 3.10.0 or above :)
# fyi, you dont need "break" statements for switch cases in python; you need it for most other languages though :)
    day = int(input("Input the Day of the Week (1-7): "));

    match day:
        case 1:
            print("Today's Drink of the Day is Peppermint Mocha.");
        case 2:
            print("Today's Drink of the Day is Candy Bar Latte.");
        case 3:
            print("Today's Drink of the Day is Caramel Coffee.");
        case 4:
            print("Today's Drink of the Day is Chocolate Almond Cafe Au Lait.");
        case 5:
            print("Today's Drink of the Day is Pumpkin-Chai Latte.");
        case 6:
            print("Today's Drink of the Day is Vanilla Chai Tea.");
        case 7:
            print("Today's Drink of the Day is Gingerbread Latte.");
        case _:
            print("I am too lazy to error check this. Please input a number between 1 and 7. :)")
    #no caramel macchiato :(

#Simply remove the '#' in front of the function name to run the solution for the respective question.

#question_1();
#question_2();
#question_3();
#question_4();
#question_5();
#question_6();

# - DARRANCE BEH HENG SHEK :)