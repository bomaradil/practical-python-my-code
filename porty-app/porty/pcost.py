# pcost.py
#
# Exercise 1.27
import csv, sys
from sys import argv

def portfolio_cost(filename):
    """
    calculate the cost of a portfolio file
    """
    with open(filename) as f:
        #opening the file 
        headers = next(f) #getting the headers of the file
        cost = 0

        for lineno, line in enumerate(csv.reader(f), start=1):
            #line = line.split(',')
            _record = dict(zip(headers, line))
            try:
                #calculating the cost of the portfolio (shares * prices)
                #while taking into account the bad lines
                cost += float(line[-1]) * int(line[-2])
            except ValueError as err:
                print(f'Warning : Line {lineno}: Bad line: {line}: ', err)
        
    return cost

from fileparse import parse_csv     #import the parse_csv methode

def portfolio_cost2(filename):
    '''
    calculating the cost of a portfolio using the parse_csv mehode in the fileparse.py
    '''
    cost = 0
    for i in parse_csv(filename, select=['shares', 'price'], types=[int, float]):
        cost += i['price'] * i['shares']
    return cost

from stock import Stock

def portfolio_cost3(filename):
    '''
    calculating the cost using class Stock in stock.py
    '''
    portdict = parse_csv(filename, select=['name','shares', 'price'], types=[str, int, float])
    portfolio = [Stock(i['name'], i['shares'], i['price']) for i in portdict]
    cost = sum([s.cost for s in portfolio])
    return cost

from report import read_portfolio_4

def portfolio_cost_4(filename):
    '''
    compute the cost using the class Portfolio in portfolio.py
    '''
    portfolio = read_portfolio_4(filename)
    return portfolio.total_cost


def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost2(filename)
    print('Total cost: ', cost)

if __name__ == '__main__':
    main(sys.argv)
    
