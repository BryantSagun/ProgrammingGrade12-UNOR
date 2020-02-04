import sys

# START OF VERIFICATION
pin = 1013
attempts = 0
enterPin = int(input("Enter PIN: "))
while enterPin != pin:
    attempts += 1
    print("Incorrect Pin.")
    if attempts < 3:
        enterPin = int(input("Enter PIN: "))
    else:
        print("Card blocked. Please contact your branch. Thank you.")
        sys.exit()
# END OF VERIFICATION

# START OF TRANSACTION PROPER
savings = 0
current = 0
withdrawalAmt = 0
depositAmt = 0
transCount = 1
transact = True
while transact:
    amount = 0
    transType = int(input("Select [1] to Withdraw, [2] to Deposit, [3] to Inquire: "))

    if transType == 1:
        amount = int(input("Enter amount to withdraw: "))
        withdrawalAmt += amount
        if amount > 20000 or withdrawalAmt > 20000:
            print("Withdrawal limit exceeded.")
            withdrawalAmt -= amount
        else:
            savOrCurr = int(input("Select [1] for Savings, [2] for Current: "))
            if savOrCurr == 1:
                if amount > savings:
                    print("Insufficient balance.")
                elif savings > amount:
                    savings -= amount
            if savOrCurr == 2:
                if amount > current:
                    print("Insufficient balance.")
                elif current > amount:
                    current -= amount

    elif transType == 2:
        amount = int(input("Enter amount to deposit: "))
        depositAmt += amount
        if amount > 500000 or depositAmt > 500000:
            print("Deposit limit exceeded.")
            depositAmt -= amount
        else:
            savOrCurr = int(input("Select [1] for Savings, [2] for Current: "))
            if savOrCurr == 1:
                savings += amount
                depositAmt += amount
            elif savOrCurr == 2:
                current += amount
                depositAmt += amount

    elif transType == 3:
        savOrCurr = int(input("Select [1] for Savings, [2] for Current: "))
        if savOrCurr == 1:
            print("Your savings balance is: ", savings)
            transCount -= 1
        elif savOrCurr == 2:
            print("Your current balance is: ", current)
            transCount -= 1

    print("Your balance is: ", savings+current)
    transCount += 1
    if transCount <= 6:
        transactAgain = int(input("Would you like another transaction? [1] Yes [2] No: "))
        if transactAgain == 1:
            transact = True
        else:
            transact = False
    else:
        print("Transaction limit for the day reached.")
        break
print("Thank you for banking with us.")
# END OF TRANSACTION PROPER
