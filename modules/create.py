import pandas as pd
import numpy as np


def main():
    # Define color codes for text color using ANSI escape sequences
    

    data = initialise(param())


def param()-> dict:
    
    c = color()
    print(c['COLOR_GREEN'] + 'Param module executed' + c['COLOR_RESET'])
    param = {
        'Transaction_ID_range': [1, 100],
        'Account_Balance_range': [1000, 1000000],
        'Account_Number_range': [1, 9],
    }
    
    return param


def initialise(param: dict)-> dict:
   
    c = color()
    print(c['COLOR_GREEN'] + 'Initialise module executed' + c['COLOR_RESET'])

    #Define the data using a dictionary
    data = {
        'Transaction_ID': [],
        'Account Balance': [],
        'Account Number': [],
    }
    
     
    id_range = param['Transaction_ID_range']
    acc_bal_range = param['Account_Balance_range']
    acc_num_range = param['Account_Number_range']
    
    
    for id in range(id_range[0], id_range[1]):
        bal = np.random.randint(acc_bal_range[0], acc_bal_range[1])
        acc = np.random.randint(acc_num_range[0], acc_num_range[1])
        data['Transaction_ID'].append(id)
        data['Account Balance'].append(bal)
        data['Account Number'].append(acc)

    
    
# Create a DataFrame from the dictionary
#df = pd.DataFrame(data)

# Perform data cleaning and preprocessing if necessary
# For example, fill missing values with a default value
#df['Age'].fillna(0, inplace=True)

# Explore and manipulate the data
# For example, filter data based on a condition
#filtered_df = df[df['Age'] > 30]

# Visualize the data
# For example, create a bar chart of ages
#df['Age'].plot(kind='bar', title='Ages')

# Export the data to a CSV file
#df.to_csv('data.csv', index=False)


    # Define color codes for text color using ANSI escape sequences

def color():
    color = {
        'COLOR_RED' : '\033[31m',
        'COLOR_GREEN' : '\033[32m',
        'COLOR_YELLOW' : '\033[33m',
        'COLOR_BLUE' : '\033[34m',
        'COLOR_MAGENTA' : '\033[35m',
        'COLOR_RESET' : '\033[0m',
    }
    
    return color


if __name__ == '__main__':
    main()