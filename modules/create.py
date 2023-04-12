import pandas as pd
import numpy as np


def main():
    # Define color codes for text color using ANSI escape sequences
    data = initialise(param())
    df = create_df(data)
    #later_info(df)

def param()-> dict:
    
    c = color()
    print(c['COLOR_GREEN'] + 'Param module executed' + c['COLOR_RESET'])
    param = {
        'Transaction_ID_range': [1, 1000],
        'Account_Balance_range': [1000, 1000000],
        'Transaction_Type': ['Debit', 'Credit'],
        'Transaction_Amount_range': [100, 1000000],
        'Account_Number_range': [1, 10001],
    }
    
    return param


def initialise(param: dict)-> dict:
   
    c = color()
    print(c['COLOR_GREEN'] + 'Initialise module executed' + c['COLOR_RESET'])

    #Define the data using a dictionary
    data = {
        'Transaction_ID': [],
        'Account Balance': [],
        'Transaction Type': [],
        'Transaction Amount': [],
        'Average Transaction Amount': [],
        'Account Number': [],
    }
    
     
    id_range = param['Transaction_ID_range']
    acc_bal_range = param['Account_Balance_range']
    acc_num_range = param['Account_Number_range']
    
    numbers = np.array(range(acc_num_range[0], acc_num_range[1]))

    random_indices = np.random.choice(len(numbers), size=(acc_num_range[1] - acc_num_range[0]), replace=False)
    acc_num = numbers[random_indices]
        
    
    i = 0
    
    for id in range(acc_num_range[0], acc_num_range[1]):
        
        
        acc = acc_num[i]
        bal = np.random.randint(acc_bal_range[0], acc_bal_range[1])
        amt = np.random.randint(10, bal * 0.15)
        avg_amt = np.random.randint(10, bal * 0.10)
        
        if (bal - amt) < 0:
            amt = bal * 0.75
        bal= bal - amt
        
        rand = np.random.randint(0, 2)
        data['Transaction_ID'].append(id)
        data['Transaction Amount'].append(amt)
        data['Transaction Type'].append(rand)
        data['Average Transaction Amount'].append(avg_amt)
        data['Account Balance'].append(bal)
        data['Account Number'].append(acc)
        
        i += 1

    
    return data 
# Create a DataFrame from the dictionary

def create_df(data: dict)-> pd.DataFrame:
    c = color()
    print(c['COLOR_GREEN'] + 'Create_df module executed' + c['COLOR_RESET'])
    df = pd.DataFrame(data)
    
    df['isFraud'] = 'Unknown'
    
    print(c['COLOR_YELLOW'])
    print(df)
    print(c['COLOR_RESET'])
    return df


def later_info(df: pd.DataFrame)-> pd.DataFrame:
    c = color()
    print(c['COLOR_GREEN'] + 'Later_info module executed' + c['COLOR_RESET'])
    
    
    df['isFraud'] = 'Unknown'
    print(c['COLOR_BLUE'])
    print(df)
    print(c['COLOR_RESET'])
    return df



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