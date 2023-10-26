import random;

def question1():
    secret_num = random.randint(1, 200);
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

def question2():
    multiply = int(input("Which multiplication table would you like to print? "));
    length = int(input("How high would you like it to go? "));

    count = 0;
    while(count <= length):
        print(f"{count} times {multiply} = {count * multiply}");
        count += 1;

def question3():
    # imagine i is rows and j is columns
    i = 0;
    j = 1;
    final = "1";

    while(i < 5):
        while(j < 11):
            if(final[j-1] == '1'):
                final += '0';
                j += 1;
            else:
                final += '1';
                j += 1;
        
        final += "\n"
        j = 0;
        i += 1;
    
    print(final);

def question4():

    #got tired of alt-tabbing
    '''
    Celsius = (Fahrenheit - 32) * 5/9 
    Fahrenheit = (Celsius * 9/5) + 32
    '''

    print("Temperature Conversion Programme.\n[1] Convert Celsius to Fahrenheit.\n[2] Convert Fahrenheit to Celsius.")
    choice = input("\nEnter your selection, 1 or 2: ");

    while(choice != '1' and choice != '2'):
        print("ERROR: Invalid Selection!");
        errOpt = input("Do you want to run the program again? [Y/N]:").lower();

        if(errOpt == 'y'):
            print("\nTemperature Conversion Programme.\n[1] Convert Celsius to Fahrenheit.\n[2] Convert Fahrenheit to Celsius.")
            choice = input("\nEnter your selection, 1 or 2: ");
        else:
            print("\nEither you selected 'N' or something else. Too lazy to catch it, soooo Goodbye!");
            break;

    if(choice == '1'):
        print("\nCelsius (C) to Fahrenheit (F) Conversion\nEnter temperature in integer values only.")
        minTemp = input("Enter minimum temperature: ");
        maxTemp = input("Enter maximum temperature: ");

        if(not(minTemp.isdigit() and maxTemp.isdigit())):
            print("ERROR: Please Enter an Integer, walao");

            errOpt = input("Do you want to run the program again? [Y/N]:").lower();
            if(errOpt == 'y'):
                print("Rerunning Program...\n");
                question4();
            else:
                print("\nEither you selected 'N' or something else. Too lazy to catch it, soooo Goodbye!");
                return 0;
        else:
            minTemp = int(minTemp);
            maxTemp = int(maxTemp);

            if(minTemp > maxTemp):
                print("ERROR: Invalid Input.");
                errOpt = input("Do you want to run the program again? [Y/N]:").lower();

                if(errOpt == 'y'):
                    print("Rerunning Program...\n");
                    question4();
                else:
                    print("\nEither you selected 'N' or something else. Too lazy to catch it, soooo Goodbye!");
                    return 0;

        while(minTemp <= maxTemp):
            print(f"{minTemp}C = {((minTemp * 9/5) + 32)}F");
            minTemp += 1;
        print("Conversion Done!");

        if(input("Do you want to run the program again? [Y/N]").lower() == 'y'):
            print("Rerunning Program...\n");
            question4();
        else:
            print("Bye bye!");

    elif(choice == '2'):
        print("\nFahrenheit (F) to Celsius (C) Conversion\nEnter temperature in integer values only.")
        minTemp = input("Enter minimum temperature: ");
        maxTemp = input("Enter maximum temperature: ");

        if(not(minTemp.isdigit() and maxTemp.isdigit())): #De Morgan's Law coz I can
            print("ERROR: Please Enter an Integer, walao");

            errOpt = input("Do you want to run the program again? [Y/N]:").lower();
            if(errOpt == 'y'):
                print("Rerunning Program...\n");
                question4();
            else:
                print("\nEither you selected 'N' or something else. Too lazy to catch it, soooo Goodbye!");
                return 0;
        else:
            minTemp = int(minTemp);
            maxTemp = int(maxTemp);
            
            if(minTemp > maxTemp):
                print("ERROR: Invalid Input.");
                errOpt = input("Do you want to run the program again? [Y/N]:").lower();

                if(errOpt == 'y'):
                    print("Rerunning Program...\n");
                    question4();
                else:
                    print("\nEither you selected 'N' or something else. Too lazy to catch it, soooo Goodbye!");
                    return 0;

        while(minTemp <= maxTemp):
            print(f"{minTemp}F = {((minTemp - 32) * 5/9)}C");
            minTemp += 1;
        print("Conversion Done!");

        if(input("Do you want to run the program again? [Y/N]").lower() == 'y'):
            print("Rerunning Program...\n");
            question4();
        else:
            print("Bye bye!");


#question1();
#question2();
#question3();
#question4();