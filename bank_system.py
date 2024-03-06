from database import *

Kamogelo = BankAccount(1000, "Kamogelo")
Sarah = BankAccount(2000, "Sarah")

Kamogelo.get_balance()
Sarah.get_balance()

Sarah.deposit(500)

Kamogelo.withdraw(10000)
Kamogelo.withdraw(10)

Sarah.transfer(10000, Sarah)
Sarah.transfer(100, Sarah)

Jim = InterestRewardsAcct(1000, "Jim")

Jim.get_balance()

Jim.deposit(100)

Jim.transfer(100, Dave)

Blaze = SavingsAcct(1000, "Blaze")

Blaze.get_balance()

Blaze.deposit(100)

Blaze.transfer(10000, Sarah)
Blaze.transfer(1000, Sarah)