def getMean(my_list):
    sum = 0;
    for item in my_list:
        sum += item;
    mean = sum / len(my_list);

    return mean;

def getSD(my_list, mean):
    sum = 0;
    for item in my_list:
        sum += (item - mean) ** 2;
    sd = (sum / len(my_list)) ** 0.5;
    
    return sd;

print("Please input 5 numbers.\n");

my_list = [];

for i in range(0,5):
    num = int(input("Input a number: "));
    my_list.append(num);

mean = getMean(my_list);
sd = getSD(my_list, mean)

print(f"\n\nmy_list = {my_list}");
print(f"Mean = {mean}");
print(f"Standard Deviation = {sd}")
