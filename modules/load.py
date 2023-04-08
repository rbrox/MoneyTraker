
import pandas as pd

def main():
    load()
    print('Load module executed')


def load():
    file_path = r'data/transactions.csv'
    print('Loading transactions from file: ' + file_path)
    data = pd.read_csv(file_path)
    print('Transactions loaded: ' + str(len(data)))
    print('Transactions columns: ' + str(data.columns))
    print('Transactions head: ' + str(data.head()))
    print('Transactions tail: ' + str(data.tail()))
    print('Transactions info: ' + str(data.info()))
    
    
if __name__ == '__main__':
    main()