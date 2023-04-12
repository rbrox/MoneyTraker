import pandas as pd
import numpy as np


# Define the data using a dictionary
data = {
    'Transaction_ID': [],
    'Account Balance': []
}

# Append data points to the dictionary

for id in range(1, 1000):
    bal = np.random.randint(1000, 1000000)
    data['Transaction_ID'].append(id)
    data['Account Balance'].append(bal)

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
