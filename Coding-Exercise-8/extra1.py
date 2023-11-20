def reverseInt(userInput):
    reverse = 0;
    while(userInput > 0):
        remainder = userInput % 10;
        reverse = (reverse * 10) + remainder;
        userInput = userInput // 10;
    return reverse;


userInput = int(input("Enter a 3 digit number: "));
reverse = reverseInt(userInput);
print(reverse)