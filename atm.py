class Bank:
    def __init__(self):
        self.closingBal = 0  # Initialize closing balance to 0

    def display(self):
        while True:
            print("\nEnter your options:")
            print("1 for deposit\n2 for withdraw\n3 to exit")

            getOption = input("Choose an option: ")

            if getOption == "1":
                self.deposit()
            elif getOption == "2":
                self.withdraw()
            elif getOption == "3":
                print("Thanks for visiting our bank!")
                break
            else:
                print("Invalid option, please try again.")

    def deposit(self):
        try:
            depositAmount = int(input("Enter your deposit amount: "))
            if depositAmount > 0:
                self.closingBal += depositAmount
                print(f"Deposit successful! Your new balance is: {self.closingBal}")
            else:
                print("Please enter a positive amount.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def withdraw(self):
        try:
            withdrawAmount = int(input("Enter your withdrawal amount: "))
            if withdrawAmount > 0:
                if self.closingBal >= withdrawAmount:
                    self.closingBal -= withdrawAmount
                    print(f"Withdrawal successful! Your new balance is: {self.closingBal}")
                else:
                    print("Insufficient balance!")
            else:
                print("Please enter a positive amount.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Create an instance of the Bank class and start the application
bankObj = Bank()
bankObj.display()
