#tableformat.py
#
#Exercise 4.5

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()

    #def __getattribute__(self, headers, rowdata):
    #    for h in headers:


class TextTableFormatter(TableFormatter):
    '''
    emit a table in plai-text format
    '''

    def headings(self, headers):
        for h in headers:
            print(f'{h:>10}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    '''
    output portfolio data in CSV format.
    '''

    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    '''
    output portfolio data in html format
    '''

    def headings(self, headers):
        print('<tr><th>', '</th><th>'.join(headers), '</th></tr>', sep='')

    def row(self, rowdata):
        print('<tr><td>', '</td><td>'.join(rowdata), '</td></tr>', sep='')


def create_formatter(fmt):
    '''
    a function to print the result depending at the format
    "txt, html, csv"
    '''
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    else:
        #raise RuntimeError(f'UKNOWN format {fmt}')
        raise FormatError('Unknown table format %s' % fmt)

def print_table(portfolio, headers, formatter):
    '''
    a function to print a part of the portfolio depending at the headers
    '''
    formatter.headings(headers)
    for p in portfolio:
        rowdata = (getattr(p, h) for h in headers)
        formatter.row(rowdata)

class FormatError(Exception):
    pass

