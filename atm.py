class Atm(object):
    
    def _init_(self,CardNumber,PinNumber):
        self.CardNumber = CardNumber
        self.PinNumber = PinNumber

        CardNumber = input("CardNumber :- ")
        PinNumber = input("PinNumber :- ")

    def _init_(self,CashWithdrawl,BalanceEnquiry):      
        self.CashWithdrawl = CashWithdrawl
        self.BalanceEnquiry = BalanceEnquiry

    def BalanceEnquiry(self):
        print("The balance in your account is :- " BalanceEnquiry)

     def CashWithdrawl(self):
         input("Please tell the amount you want to withdraw :- ")