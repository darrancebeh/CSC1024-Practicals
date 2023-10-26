def extra1():

    #question didnt ask for error handling so haha yay

    principal = int(input("Enter the initial principal: RM"));
    interest = float(input("Enter the interest rate: "));
    years = int(input("Enter the number of years: "));

    print("\n\nCompound Interest Calculation");
    print("Initial Principal: RM", principal);
    print("Interest Rate: ", interest);
    print("Number of Years: ", years);

    flag = 0;
    print("\n")
    while(flag <= years):
        print(f"Year {flag}: RM{round(principal * (1 + interest) ** flag, 2)}");
        flag += 1;

def extra2():
    #only using lower case letters for code simplicity and time efficiency :)

    a = "abcdefghijklmnopqrstuvwxyz";

    opt = input("Encrypt or Decrypt? [E/D]: ").lower();

    if(opt == 'e'):
        encText = input("Enter text to encrypt: ");
        encKey = int(input("Enter shift number: "));

        encText = encText.lower();
        encText = encText.replace(" ", "");
        
        encText = [a.index(i) for i in encText];
        encText = [i + encKey for i in encText];
        encText = [i - 26 if i > 25 else i for i in encText];
        encText = [a[i] for i in encText];
        encText = "".join(encText);

        print(f"Encrypted Text: {encText}");
    
    elif(opt == 'd'):
        decText = input("Enter text to decrypt: ");
        decKey = int(input("Enter shift number: "));

        decText = decText.lower();
        decText = decText.replace(" ", "");

        decText = [a.index(i) for i in decText];
        decText = [i - decKey for i in decText];
        decText = [i + 26 if i < 0 else i for i in decText];
        decText = [a[i] for i in decText];
        decText = "".join(decText);

        print(f"Decrypted Text: {decText}");
    
    else:
        print("\nERROR: Invalid Selection!");
        print("Imma Just Abruptly End The Program Now. Bye! :))))")

#extra1();
#extra2();
