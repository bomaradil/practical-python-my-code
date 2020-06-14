#ticker.py
#
#Exercise 6.10

from os import name
import types
from follow import Follow
import csv
import report, tableformat

def select_colomns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dict(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    rows = (row for row in rows if row['name'] in names)
    yield rows


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_colomns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, str, str])
    rows = make_dict(rows, ['name', 'price', 'shares'])
    return rows

def ticker(portfolio, logfile, fmt):
    portfolio = report.read_portfolio_4(portfolio)
    lines = Follow(logfile)
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['name', 'price', 'shares'])
    for rowdata in rows:
        formatter.row(rowdata.values())

if __name__ == "__main__":
    portfolio = report.read_portfolio_4('Data/portfolio.csv')
    lines = Follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row)