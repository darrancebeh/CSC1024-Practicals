import random;

def addition():
    num1 = random.randint(5, 20);
    num2 = random.randint(5, 20);

    addInput = int(input(f"Enter the sum of {num1} + {num2}: "));

    ans = num1 + num2;

    return addInput, ans;

def subtraction():
    num1 = random.randint(25, 50);
    num2 = random.randint(5, 20);

    subInput = int(input(f"Enter the subtraction of {num1} - {num2}: "));

    ans = num1 - num2;

    return subInput, ans;

def ansCheck(UserInput, ans):
    if UserInput == ans:
        return True, ans;
    else:
        return False, ans;

def main():
    option = int(input("[1] Addition\n[2] Subtraction\nEnter 1 or 2: "));

    if(option == 1):
        userInp, ans = addition();
        flag, ans = ansCheck(userInp, ans);

        if(flag == True):
            print("Correct!");
        else:
            print("Wrong!");
            print(f"The answer is {ans}");

    elif(option == 2):
        userInp, ans = subtraction();
        flag, ans = ansCheck(userInp, ans);
    
        if(flag == True):
            print("Correct!");
        else:
            print("Wrong!");
            print(f"The answer is {ans}");

    else:
        print("Invalid option!");

main();