import sqlite3

class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\n Account '{self.name}' created.\nBalance R{self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance  R{self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\n Deposit Complete")

    def possible_transact(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\n Sorry, account '{self.name}' only has a balance of R{self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.possible_transact(amount)
            self.balance = self.balance - amount
            print("Transaction Complete. ")
            self.get_balance()
        except BalanceException as error:
            print(f'\nWithdraw error: {error}')

    def transfer(self, amount, account):
        try: 
            print('\n**********\n\nBeginning Transfer.. ')
            self.possible_transact(amount) 
            self.withdraw(amount) 
            account.deposit(amount) 
            print('\nTransfer complete! \n\n**********')
        except BalanceException as error: 
            print(f'\nTransfer interrupted.  {error}')

class InterestRewardsAcct(BankAccount): 
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.get_balance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, acct_name): 
        super().__init__(initial_amount, acct_name)
        self.fee = 5

    def withdraw(self, amount): 
        try: 
            self.possible_transact(amount + self.fee)
            self.balance = self.balance - (amount + self.fee) 
            print("\nWithdraw completed.")
            self.get_balance() 
        except BalanceException as error: 
            print(f'\nWithdraw interrupted: {error}')

def load_accounts_from_database():
    conn = sqlite3.connect('bank_accounts.db')
    c = conn.cursor()
    accounts = []
    c.execute("SELECT * FROM BankAccount")
    rows = c.fetchall()
    for row in rows:
        account_id, initial_amount, acct_name = row
        account = BankAccount(account_id, initial_amount, acct_name)
        accounts.append(account)
    conn.close()
    return accounts
