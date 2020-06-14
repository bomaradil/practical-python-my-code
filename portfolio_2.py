#portfolio_2.py
#
#Exercise 7.11

import stock_2
from porty import fileparse

class Portfolio:
    '''
    a class Portfolio to parse the csv file using classmethode
    '''
    def __init__(self):
        self.holdings = []
    
    def append(self, holding):
        if not isinstance(holding, stock_2.Stock):
            raise TypeError('Expected a Stock instance')
        self.holdings.append(holding)
    
    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        pordicts = fileparse.parse_csv(lines,
                                        select=['names', 'shares', 'price'],
                                        **opts)
        for d in pordicts:
            self.append(stock_2.Stock(**d))
        return self