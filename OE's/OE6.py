class BankAccount:
    def __init__(self, account_number, balance):
       
        self.__account_number = account_number
        self.__balance = balance

 
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def display_account_info(self):
        print(f"Account Number: {self.__account_number}, Balance: {self.__balance}")

  
    def __display_balance(self):
        print(f"Balance: {self.__balance}")

  
    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if isinstance(balance, (int, float)) and balance >= 0:
            self.__balance = balance
            print(f"New balance set: {self.__balance}")
        else:
            print("Invalid balance value. Balance must be a non-negative number.")


if __name__ == "__main__":
   
    account = BankAccount("123456789", 1000.0)

  
    account.deposit(500)

 
    account.withdraw(300)

    account.set_balance(-100)

    account.display_account_info()
