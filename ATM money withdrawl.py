#Lets code a program that effectively simulates in bank ATM in which we can:-
# Check Balance, Make Withdrawal, Pay-in, Return card

print('Welcome to Bank Of Boarda ATM')
restart=('Y')
chances= 3            # We will get only 3 chance to enter the correct ATM Pin.
balance= 125.50       # Balance in our Bank Account.
while chances >= 0:
    pin = int(input('Please Enter your 4 Digit Pin:'))
    if pin == (1234):    #This is our ATM PIN Code.
        print('You have entered your PIN Correctly\n')
        while restart not in ('n','NO','no','N'):
            print('Please Press 1 To Check Your Balance\n')
            print('Please Press 2 To Make a Withdrawal\n')
            print('Please Press 3 To Make a Pay in\n')
            print('Please Press 4 To Return Card\n')
            option = int(input('What Would You Like to Choose?:'))
            if option == 1:                                          # Press 1 to check Balance
                print('Your Balance is $',balance,'\n')
                restart = input('Would you like to go back?')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 2:                                        # Press 2 To Make a Withdrawal
                option2 =('y')
                withdrawl = float(input('How much would you like to withdraw? \n10Â$/$20/$40/$60/$80/$100' ))
                if withdrawl in [10,20,30,40,60,80,100]:
                    balance = balance - withdrawl
                    print('\nYour Balance is now $',balance)
                    restart = input('Would You like to go back?:')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif withdrawl != [10,20,40,60,80,100]:
                    print('Invalid Amount , Please Re-try\n')
                    restart =('y')
                elif withdrawl == 1:
                    withdrawl = float(input('Please Enter Desired Amount:'))
            elif option == 3:                                           # Press 3 To Make a Pay in
                pay_in = float (input('How Much Would You Like to Pay In:'))
                balance = balance + pay_in
                print ('\nYour Balance is now $', balance)
                restart = input('Would you like to go back?')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 4:                                           # Press 4 To Return Card
                print("Please Wait Until You Card is Returned....\n")
                print('Thank you for your Service')
                break
            else:
                print('Please Enter a correct Number. \n')
                restart = ('y')
    elif pin != ('1234'):
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print("\nNo more tries")
            break