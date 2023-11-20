def Userinput():
    num = int(input("Enter a number: "));
    return num;

def countUp(num):
    for i in range(1, num+1):
        print(i);

def main():
    num = Userinput();
    print("\n");
    countUp(num);

main();
