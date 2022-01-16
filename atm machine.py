#PROJECT MADE BY ASAD GHAFFAR (FA21-BCS-015)
#number module import
#from numpy import number


#DATABASE account holders
customerNames = ['ASAD', 'ZEESHAN', 'ARSALAN', 'IBRAHIM', 'HASSAAN', 'ARMUGHAN', 'ABDULLAH', 'UMER']
customerAge = [18, 17, 19, 18, 19, 18, 18, 19]
customerPins = ['0123', '2575', '7275', '5049', '3453', '2533', '4363', '5334']
customerPhNumber = ['31787382', '3242223', '23223232', '32323222', '54532242', '22433537', '434343366', '64764644']
customerBalances = [10000, 20000, 40000, 10000, 23003, 20000, 90000, 23000]
adminID = ['ASAD771878', 'ZEESHAN785879']
adminPassword = ['CUII', 'IAmPro']
deposition = 0
withdrawal = 0
balance = 0
i = 0


# This statement below helps the program to run continuously.
while True:
    # Welcome Note for our banking system
    print("  *****   ")
    print("<<WELCOME TO COMSATS BANKING SYSTEM SIR/MAM>> ")
    print("  ***** \n")
    print("<===========================>")
    print("1. OPEN A NEW ACCOUNT        ")
    print("2. WITHDRAW MONEY            ")
    print("3. DEPOSIT MONEY            ")
    print("4. CHECK CUSTOMERS & BALANCE ")
    print("5. EXIT/QUIT/END             ")
    print("<===========================>")
    # The below statement takes the choice number from the user.
    choiceNumber = input("KINDLY SELECT YOUR CHOICE SIR/MAM ")


    #for Opening Account
    if choiceNumber == "1":
        print("GREETINGS!!CUSTOMER WANTS TO OPEN A NEW ACCOUNT!.\n")
        print("\nPLEASE ENTER YOUR DETAILS TO OPEN A NEW ACCOUNT")
        
        # These few lines will take information from customer and then append them to the list.
        name = input("KINDLY ENTER YOUR FULL NAME: ")
        customerNames.append(name)
        age = eval(input("KINDLY ENTER YOUR AGE: "))
        customerAge.append(age)
        phNumber = eval(input("KINDLY ENTER YOUR PH.No: "))
        customerPhNumber.append(phNumber)
        pin = str(input("CREATE A PIN OF YOUR ACCOUNT: "))
        customerPins.append(pin)
        balance = 0
        deposition = eval(input("ENTER AMOUNT(>= 500-/Rs) TO DEPOSIT: "))
        if deposition < 500:
            print("KINDLY ENTER AMOUNT >= 500.")
        else:
            balance = balance + deposition
            customerBalances.append(balance)
            print("\nNAME =", name, end=" ")
            print("Ph. NUMBER = ", phNumber, ",", end="")
            print("Pin =", str(pin), ",", end=" ")
            print("BALANCE =", str(balance), ",", end=" ")
            print("-/Rs")
            
            #print("New account created successfully!")
            print("CONGRATS!YOUR ACCOUNT HAS BEEN CREATED. CUSTOMER DETAILS ARE ADDED TO THE SYSTEM!")
            print("\n")
            print("NOTE!!PLEASE REMEMBER THE NAME AND PIN")
            print("<=====================================>")
        # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Enter any Key to Continue to Main Menu...")


    #For Withdrawing Money
    elif choiceNumber == "2":
        j = 0
        print("SIR/MAM!! YOU WANT TO WITHDRAW MONEY?.")
        # This while loop will prevent the user using the account if the username or pin is wrong.
        while j < 1:
            k = -1
            name = input("PLEASE ENTER THE ACCOUNT OWNER NAME: ")
            pin = input("PLEASE ENTER ACCOUNT PIN SIR/MAM: ")
            # This while loop will keep the function running when variable k is smaller than length of the
            # customerNames list.
            while k < len(customerNames) - 1:
                k = k + 1
                # These two if conditions find where both the name and pin matches.
                if name.upper() == customerNames[k]:
                    if pin == customerPins[k]:
                        j = j + 1
                        # These few statement would show the balance taken from the list.
                        print("SIR/MAM YOUR CURRENT BALANCE:", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs\n")
                        balance = (customerBalances[k])
                        # Statement below would take the amount to withdraw from user.
                        withdrawal = eval(input("KINDLY INPUT AMOUNT YOU WOULD LIKE TO WITHDRAW: "))
                        # The if condition below would look whether the withdraw is greater than the balance.
                        if withdrawal > balance:
                            # This statement below would take a deposition from the customer.
                            deposition = eval(input(
                                "PLEASE ENTER A VALID AMOUNT SIR/MAM: "))
                            # These few statements would update the value and show the balance to user.
                            balance = balance + deposition
                            print("SIR/MAM YOUR CURRENT BALANCE:", end=" ")
                            print(balance, end=" ")
                            print("-/Rs\n")
                            balance = balance - withdrawal
                            print("-\n")
                            print("<<<**WITHDRAW SUCCESSFUL**>>>")
                            customerBalances[k] = balance
                            print("SIR/MAM YOUR NEW BALANCE IS: ", balance, end=" ")
                            print("-/Rs\n")
                        else:
                            # Else condition mentioned above is to do withdrawal if the balance is greater than the
                            # withdraw amount.
                            balance = balance - withdrawal
                            # These few statement would update the values in the list and show it to the customer.
                            print("\n")
                            print("<<<*WITHDRAW SUCCESSFUL*>>>")
                            customerBalances[k] = balance
                            print("SIR/MAM YOUR NEW BALANCE IS: ", balance, end=" ")
                            print("-/Rs\n")
            if j < 1:
                # The if condition above would work when the pin or the name is wrong.
                print("ACCOUNT OWNER NAME DOESN'T MATCH. PLEASE SIR/MAM! TRY AGAIN>>\n")
                break
            # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Enter any Key to Continue to Main Menu...")


    #For Depositing Money
    elif choiceNumber == "3":
        print("SIR/MAM YOU WANT TO DEPOSIT AMOUNT!")
        n = 0
        # The while loop below would work when the pin or the username is wrong.
        while n < 1:
            k = -1
            name = input("PLEASE ENTER ACCOUNT OWNER NAME: ")
            pin = input("KINDLY ENTER ACCOUNT PIN: ")
            # The while loop below will keep the function running to find the correct user.
            while k < len(customerNames) - 1:
                k = k + 1
                # The two if conditions below would find whether both the pin and the name is correct.
                if name.upper() == customerNames[k]:
                    if pin == customerPins[k]:
                        n = n + 1
                        # These statements below would show the customer balance and update list values according to
                        # the deposition made.
                        print("SIR/MAM YOUR CURRENT BALANCE IS: ", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs")
                        balance = (customerBalances[k])
                        # This statement below takes the depositionn from the customer.
                        deposition = eval(input("ENTER THE AMOUNT YOU WANT TO DEPOSIT SIR/MAM: "))
                        balance = balance + deposition
                        customerBalances[k] = balance
                        print("\n")
                        print("<<<*CONGRATS AMOUNT DEPOSITED SUCCESSFULLY*>>>")
                        print("SIR/MAM YOUR NEW BALANCE IS: ", balance, end=" ")
                        print("-/Rs\n")
            if n < 1:
                print("ACCOUNT OWNER NAME AND PIN DOESN'T MATCH PLEASE! TRY AGAIN>>\n")
                break
            # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Enter any Key to Continue to Main Menu...")


    #For customers List
    elif choiceNumber == "4":
        print()
        print("THIS PANEL IS ONLY FOR ADMINISTRATION!")
        print("\n")
        admin_name_admin = input("KINDLY ENTER ADMIN ID: ")
        admin_pin_admin = input("PLEASE ENTER ADMIN PASSCODE/PIN: ")
        if admin_name_admin in adminID and admin_pin_admin in adminPassword:
            # The while loop below will keeping running until all the customers and balances are shown.
            print("CUSTOMER NAMES AND BALANCE: ")
            k = 0
            while k <= len(customerNames) :
                print("->CUSTOMER =", customerNames[k])
                print("->BALANCE =", customerBalances[k], end=" ")
                print("-/Rs")
                print("\n")
                k = k + 1
        else:
            print("\nYOU ENTERED A WRONG ADMIN ID OR PASSCODE!")
            print("SORRY! SYSTEM CLOSED!")
            print("\n")
            mainMenu = input("Enter any Key to Continue to Main Menu...") #Menu code


    #For closing/Quiting system
    elif choiceNumber == "5":
        # These statements would be just showed to the customer.
        print("THANKYOU SIR/MAM FOR USING COMSATS BANKING SYSTEM!!!")
        print("HOPE TO SEE YOU SOON. HAVE A NICE DAY AHEAD!!:)")
        print("")
        break
    else:
        # This else function above would work when a wrong function is chosen.
        print("WRONG OPTION SELECTED!!!")
        print("KINDLY TRY AGAIN!!!")
        # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu =input("Enter any Key to Continue to Main Menu...")