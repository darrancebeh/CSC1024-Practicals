def extra1():
    a = int(input("Enter the First Term: "));
    d = int(input("Enter the Common Difference: "));
    n = int(input("Enter the Number of Terms: "));

    sum = (a + (n - 1) * d);

    #display each term and determine the sum of the arithmetic series
    while(a != sum):
        print(a, end=' ');
        a += d;
    print(sum);

def extra2():
    #question states gravity to be 32 feet/s; but allowing input allows for other values, eg; 9.81ms^-2
    gravity = float(input("Enter the Gravitational Constant: "));
    time = int(input("Enter the Time, in seconds: "));

    formula = (0.5 * gravity * time ** 2);

    flag = 0;
    total = 0;
    print("Time\tInterval Distance\tTotal Distance");
    while(flag != time):
        total += (0.5 * gravity * flag ** 2);
        print(f"{flag}\t\t{0.5 * gravity * flag ** 2}\t\t{total}");
        flag += 1;

def extra3():
    #create a program that prompts user to input lengths of a rectangle and outputs a drawing of it with asterisks and blanks
    length = int(input("Enter the Length of the Rectangle: "));
    width = int(input("Enter the Width of the Rectangle: "));

    #good luck understanding this code coz im not gonna explain it
    if(length <= 0 or width <= 0):
        print("*");
    else:
        if(length == 1 or width == 1):
            flag = 0;
            while(flag != length):
                print("*", end=' ');
                flag += 1;
        else:
            flag = 0;
            while(flag != width):
                print("*", end=' ');
                flag += 1;
            print();
            flag = 0;
            while(flag != length - 2):
                print("*", end=' ');
                flag2 = 0;
                while(flag2 != width - 2):
                    print(" ", end=' ');
                    flag2 += 1;
                print("*");
                flag += 1;
            flag = 0;
            while(flag != width):
                print("*", end=' ');
                flag += 1;

#extra1();
#extra2();
#extra3()