def userInput():
    my_list = [];
    print("A program to find the maximum and minimum numbers in a list.");
    listSize = int(input("Enter how many numbers you want to read into a list: "));

    for i in range(0, listSize):
        num = int(input("Input a number: "));
        my_list.append(num);

    return my_list;

def findMaxNumber(my_list):
    ceiling = my_list[0]; #temp variable for highest number

    for item in my_list:
        if item > ceiling:
            ceiling = item;

    return ceiling;

def findMinNumber(my_list):
    floor = my_list[0]; #temp variable for lowest number

    for item in my_list:
        if item < floor:
            floor = item;

    return floor;

def main():
    my_list = userInput();
    maxNum = findMaxNumber(my_list);
    minNum = findMinNumber(my_list);

    print(f"\n\nmy_list = {my_list}");
    print(f"Maximum number in the list is {maxNum}");
    print(f"Minimum number in the list is {minNum}");

main();