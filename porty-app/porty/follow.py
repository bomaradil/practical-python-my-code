# follow.py
import os 
from sys import argv
import time
import .report

def Follow(filename):
    with open(filename , 'r') as f:
        f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file
        while True:
            for line in f:
                if line == '':
                    time.sleep(0.1)   # Sleep briefly and retry
                    continue
                yield line
                
if __name__ == "__main__":
    
    portfolio = report.read_portfolio_4('Data/portfolio.csv')

    for line in Follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
                    
