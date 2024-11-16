class BankAccount:
    def __init__(self, account_number:str, balance, date_of_openning:str, customer_name:str):
        self.account_number = account_number
        self.balance = balance
        self.date_of_openning = date_of_openning
        self.customer_name = customer_name
    def deposit(self, amount):
        self.balance = self.balance + amount
    def withdraw(self, amount):
        self.balance = self.balance - amount
    def check_balance(self):
        return self.balance

if __name__ == '__main__':
    user = BankAccount('100012312', 1000000, '05/10/2024', 'Dang')
    user.deposit(500000)
    user.withdraw(200000)
    print(user.check_balance())