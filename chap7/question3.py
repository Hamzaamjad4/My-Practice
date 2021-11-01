class account:
      def __init__(self, id , balance , annualInterestRate):
        self.__id = int(id)
        self.__balance = float(balance)
        self.__annualInterestRate = float(annualInterestRate)


      def getId(self):
        return self.__id

      def getBalance(self):
        return self.__balance

      def getAnnualInterestRate(self):
        return self.__annualInterestRate

      def setId(self, id):
        self.__id = int(id)

      def setBalance(self, balance):
        self.__balance = float(balance)

      def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate=float(annualInterestRate)

      def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 12

      def getMonthlyInterest(self):
       return self.__balance * self.getMonthlyInterestRate()


p1=account(1,20.5,20.35)
print("id=",p1.getId())
print("balance=",p1.getBalance())
print("monthly_intrest=",p1.getMonthlyInterest())
print("monthly_intrest_rate=",p1.getMonthlyInterestRate())
print("annual_intrest_rate=",p1.getAnnualInterestRate())