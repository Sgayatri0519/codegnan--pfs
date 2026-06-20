# Simple ATM Machine Program

balance = 10000
pin = 8919

print("===== WELCOME TO ATM =====")

entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:

    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        # Check Balance
        if choice == 1:
            print(f"Your balance is: ₹{balance}")

        # Deposit Money
        elif choice == 2:
            deposit = int(input("Enter amount to deposit: ₹"))
            balance += deposit
            print(f"₹{deposit} deposited successfully")
            print(f"Available balance: ₹{balance}")

        # Withdraw Money
        elif choice == 3:
            withdraw = int(input("Enter amount to withdraw: ₹"))

            if withdraw <= balance:
                balance -= withdraw
                print(f"₹{withdraw} withdrawn successfully")
                print(f"Remaining balance: ₹{balance}")
            else:
                print("Insufficient balance")

        # Exit
        elif choice == 4:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")

else:
    print("Wrong PIN")
