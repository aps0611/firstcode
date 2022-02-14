class BankAccount:
  def __init__(self, accountHolder):
    #bank account method can access self._balance but code outside of this class should not:
    self._balance = 0
    self._name = accountHolder
    with open(self._name + 'Ledger.txt', 'w') as ledgerFile:
      ledgerFile.write('Balance is 0\n')

  def deposit(self, amount):
    if amount <= 0:
      return #Dont allow negative deposits
    self._balance += amount
    with open(self._name + 'Ledger.txt', 'a') as ledgerFile:
      ledgerFile.write('Deposit' + str(amount)+ '\n')
      ledgerFile.write('Balance is ' + str(self._balance) + '\n') 

  def withdraw(self,amount):
    if self._balance < amount or amount < 0:
      return #Not enough in account
    self._balance -= amount
    with open(self._name + 'Ledger.txt', 'a') as ledgerFile:
      ledgerFile.write('Withdraw' + str(amount) + '\n')
      ledgerFile.write('Balance is ' + str(self._balance) + '/n')


acct = BankAccount('Alice') #we create an account for alice
acct.deposit(2000)
acct.withdraw(100)


#Python basic convention is to start private attribute name with _ letter
#private enforcement doesn't exists in python. Here everything has a 'Public access' and thus can be changed outside the class
#we can change the deposit withdraw but its advisable not to do it that way.