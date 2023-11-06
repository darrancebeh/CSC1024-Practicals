def question1():
    myList = [];
    i = 0;
    while(i != 5):
        num = float(input("Enter a number: "));
        myList.append(num);
    
        myList.sort();
        i +=1 ;
    print(f"my_list = {myList}")

def question2():
    myList = [];
    total = 0;

    i = 0;
    while(i != 5):
        num = float(input("Enter a number: "));

        myList.sort();
        myList.append(num);
        i += 1;
    print(f"my_list = {myList}")

    for i in myList:
        total += i;

    print(f"Total = {total}");
    print(f"Average = {total/len(myList)}")


def question3():
    temp = [];
    temp2 = [];

    i = 0;
    while(i != 5):
        num = float(input("Enter a number: "));
        temp.append(num);
        temp2.append(num);
        i += 1;

    temp.sort();

    temp2.sort(reverse=True);

    print(f"Forward List = {temp}");
    print(f"Backward List = {temp2}");

def question4():
    myList = [];

    i = 0;
    while(i != 5):
        num = float(input("Enter a number: "));
        myList.append(num);
        i += 1;

    for i in range(5):
        print(f"my_list = {myList}");
        myList.pop();
    print(f"my_list = {myList}");

def question5():
    myList = [];

    i = 0;
    while(i != 5):
        data = input("Enter a data: ");
        myList.append(data);
        i += 1;

    for i in range(5):
        print(f"my_list = {myList}");
        myList.pop();
    print(f"my_list = {myList}");

def question6():
    # OUTPUT DOES NOT FIT WITH GIVEN SAMPLE OUTPUT
    # EITHER I UNDERSTOOD THE QUESTION WRONGLY OR THE QUESTION IS WRONG
    myList = [];
    popList = [];
    flag = 0;

    i = 0;
    while(i != 5):
        data = input("Enter a data: ");
        myList.append(data);
        i += 1;

    for i in myList:
        if(myList.index(i) % 2 == 0):
            popList.append(myList.index(i));
    popList.sort(reverse=True);

    print(f"my_list = {myList}");

    for i in popList:
        myList.pop(i);
        print(f"my_list = {myList}");



#question1();
#question2();
#question3();
#question4();
#question5();
#question6();
