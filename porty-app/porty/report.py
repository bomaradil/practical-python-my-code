# report.py
#
# Exercise 2.4

import sys, csv
import types
from . import parse_csv 
from . import Stock
from . import tableformat
from . import Portfolio

portfolio = []
prices = {}
report = []

def read_portfolio(filename):
    '''
    create a dictionary inside a list from a csv file using a loop 
    '''
    
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            #share = {'name' : row[0], 'shares' : int(row[1]), 'price' : float(row[2])}
            share = dict(zip(headers, row))
            portfolio.append(share)
    return portfolio

def read_portfolio_2(filename):
    '''
    create a dictionary inside a list from a csv file using a loop in one line
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        select = ['name', 'shares', 'price']
        indices = [ headers.index(colname) for colname in select ]
        portfolio = [ { colname: row[index] for colname, index in zip(select, indices) } for row in rows ]
    return portfolio


def read_portfolio_3(filename):
    '''
    create dic using class Stock in stock.py
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        portfolio = [Stock(i[0], i[1], i[2]) for i in rows]
    return portfolio

def read_portfolio_4(filename, **opts):
    '''
    Read portfolio using the class Portfolio in portfolio.py
    '''
    with open(filename) as f:
        portdicts = parse_csv(f,
                              select=['name', 'shares', 'price'],
                              types=[str, int, float], 
                              **opts)
    #portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
    portfolio = [ Stock(**d) for d in portdicts]
    return Portfolio(portfolio)

def read_portfolio_5(file_name):
    '''
    read portfolio using class Portfolio in portfolio_2.py
    '''
    with open(file_name) as f:
        portfolio = Portfolio.from_csv(f)
    return portfolio


  
def read_prices(filename):
    '''
    create a list from a csv file
    '''
    with open(filename) as f:
        for row in csv.reader(f):
           # try:
           #     prices[row[0]] = float(row[1])
           # except IndexError as err:
           #     print('warning empty block', err)
           if row:
               prices[row[0]] = float(row[1])
        return prices
        
def loss_gain():
    '''
    comparing the share price with the portfolio price and return if we make a gain or loss
    '''
    total_price = 0
    price_share = 0
    #for i in portfolio:
    total_price = sum([prices[i['name']] * i['shares']] for i in portfolio)
    price_share = sum([i['shares'] * i['price']] for i in portfolio)
        
    if total_price > price_share:
        print('Your losses is: ', round(total_price - price_share, 2))
    else:
        print('your gain is: ', round(price_share - total_price, 2))

def loss_gain_2():
    '''
    comparing the share price with the portfolio price and return if we make a gain or loss
    using the read_porflio_3 class Stock
    '''
    total_price = 0
    price_share = 0
    #for i in portfolio:
    total_price = sum(prices[s.name] * s.shares for s in portfolio)
    price_share = sum(s.shares * s.price for s in portfolio)
        
    if total_price > price_share:
        print('Your losses is: ', round(total_price - price_share, 2))
    else:
        print('your gain is: ', round(price_share - total_price, 2))

def make_report(portfolio, prices):
    '''
    combining the info in the csv portfolio and price file 
    and making a list report for the name, total, price and change of the share 
    '''
    for i in portfolio:
        change = float(prices[i['name']]) - float(i['price'])
        report.append((i['name'], int(i['shares']), prices[i['name']], round(change, 2)))
    return report

def make_report_2(portfolio, prices):
    '''
    combining the info in the csv portfolio and price file using Class Stock
    and making a list report for the name, total, price and change of the share 
    ''' 
    for s in portfolio:
        change = float(prices[s.name]) - s.price
        #print(change)
        report.append((s.name, s.shares, s.price, round(change, 2)))
    return report

def print_report(report):
    '''
    printing the report 
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)      #f'{headers:>10s}', end=' '
    print('---------- ----------- ----------- -----------') # ('-'*10 + ' ')*len(headers)
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {"$":>6s}{price:<7.2f} {change:>10.2f}')

#from tableformat import TableFormatter as formatter

def print_report_2(reportdata, formatter):
    '''
    print report using class TableFormtter from the tableformat.py
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)


def portfolio_report(portfolio_filename, price_filename, fmt='txt'):
    '''
    operating the script
    '''
    #portfolio = parse_csv(portfolio_filename, select=['name', 'shares', 'price'], types=[str, int, float])
    portfolio = read_portfolio_4(portfolio_filename)
    #prices = dict(parse_csv(price_filename, types=[str, float], has_headers=False))
    read_prices(price_filename)
    make_report_2(portfolio, prices)
    formatter = tableformat.create_formatter(fmt)
    print_report_2(report, formatter)

def main(argv):
    if len(argv) != 4:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile format')
    portfolio_report(argv[1], argv[2], argv[3])
    import logging
    logging.basicConfig(
        filename = 'app.log',         #Name of the log file (omit use stderr)
        filemode = 'w',             #file mode (use 'a' to append)
        level = logging.WARNING,    #Loggin lvl (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
    )

if __name__ == '__main__':
    main(sys.argv)

