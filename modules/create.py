import pandas as pd
import numpy as np


def main():
    data = initialise(param())

def param()-> dict:
    print('Param module executed')
    param = {
        'Transaction_ID_range': [1, 100],
        'Account_Balance_range': [1000, 1000000],
        'Account_Number_range': [1, 9],
    }
    
    return param


def initialise(param: dict)-> dict:
    print('Initialise module executed')

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

    print(data)
    
    
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


if __name__ == '__main__':
    main()