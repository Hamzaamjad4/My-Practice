class Stock:
    def __init__(self,symbol,name,previousClosingPrice,currentPrice):
        self.symbol = symbol
        self.name = name
        self.previousClosingPrice = previousClosingPrice
        self.currentPrice = currentPrice
        print("constructor")
        print(self.symbol)
        print(self.name)
        print(self.previousClosingPrice)
        print(self.currentPrice)


    def stockSymbol(self):
        return self.symbol
    def stockname(self):
        return self.name
    def stockPreviousClosingPrice(self):
        return self.previousClosingPrice
    def stockCurrentPrice(self):
        return self.currentPrice
    def stockCurrentPrice(self):
        return self.currentPrice
    def percentage(self):
        if self.currentPrice == self.previousClosingPrice:
            return 100.0
        try:
            persentage=(abs(self.currentPrice - self.previousClosingPrice) / self.previousClosingPrice) * 100.0
            print(persentage)
        except ZeroDivisionError:
            return 0

p1=Stock("clothes","cotton",20.5,20.35)
# p1.percentage()
print("hello")