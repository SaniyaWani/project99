class Atm (object):
     def _init_(self, debit_card_nos, pinNumber):
          self.debit_card_nos = debit_card_nos
          self.pinNumber = pinNumber
     
     def cashWithdrawl(self, amountOfWithdrawlMoney):
          self.amountOfWithdrawlMoney=amountOfWithdrawlMoney
          print(self.amountOfWithdrawlMoney + "as been widrawled from count" )

     def BalanceEnquire(self):
          print("__balance is there in your account")
atm = Atm(1234567890, 1234)          
