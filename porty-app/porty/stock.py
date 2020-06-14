#stock.py
#
#exercise 7.7

from  . import typedproperty as type 

class Stock:
    name = type.String('name')
    shares = type.Integer('shares')
    price = type.Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def __repr__(self):
        return (f'Stock({self.name}, {self.shares}, {self.price})')
        #return (Stock({self.name}, {self.shares}, {self.price}))
    
    @property
    def cost(self):
        #getting the cost of shares * price 
        #stock.cost
        cost = self.shares * self.price
        return cost
    
    def sell(self, shares_to_sell):
        #getting the new shares value after deducting the sell shares
        self.shares -= shares_to_sell
        return self.shares

        