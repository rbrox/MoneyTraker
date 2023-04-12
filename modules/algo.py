# we are to include herin a fraud tracing algorithm 
# some particular ideas which we have thought of are as follows:
# We shall use a bayesian model which will be trained on a dataset of fraudulent transactions
# the bayesian model will be used to predict whether a transaction is fraudulent or not
# heirachical bayesian model diagram below

'''
        Fraudulent Transaction (FT)
               |
        ----------------
        |              |
Transaction Amount   Transaction Location
(TA)                (TL)
        |              |
        ----------------
        |              |
Cardholder Information  Cardholder Account History
(CI)                    (CAH)
        |              |
        ----------------
        |              |
    Merchant Information       Transaction Time
    (MI)                         (TT)
        |              |
        ----------------
        |
    IP Address (IPA)


'''

def main():
    ...
    
def is_fraud(transaction_id: int) -> bool :
    import pandas as pd
import numpy as np
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator

# Load transaction data from database into a Pandas DataFrame
transaction_data = pd.read_sql_query('SELECT transaction_id, transaction_amount, transaction_location, cardholder_information, cardholder_account_history, merchant_information, transaction_time, ip_address, is_fraudulent FROM transactions', db_connection)

# Prepare data for Bayesian network learning
# Drop irrelevant columns and convert categorical columns to numerical codes
data = transaction_data.drop(columns=['transaction_id'])
data['transaction_location'] = data['transaction_location'].astype('category').cat.codes
data['cardholder_information'] = data['cardholder_information'].astype('category').cat.codes
data['cardholder_account_history'] = data['cardholder_account_history'].astype('category').cat.codes
data['merchant_information'] = data['merchant_information'].astype('category').cat.codes
data['transaction_time'] = data['transaction_time'].astype('category').cat.codes
data['ip_address'] = data['ip_address'].astype('category').cat.codes

# Split data into features (X) and target variable (y)
X = data.drop(columns=['is_fraudulent'])
y = data['is_fraudulent']

# Create BayesianModel
model = BayesianModel()

# Define edges in the BayesianModel
model.add_edges_from([
    ('transaction_amount', 'is_fraudulent'),
    ('transaction_location', 'is_fraudulent'),
    ('cardholder_information', 'is_fraudulent'),
    ('cardholder_account_history', 'is_fraudulent'),
    ('merchant_information', 'is_fraudulent'),
    ('transaction_time', 'is_fraudulent'),
    ('ip_address', 'is_fraudulent')
])

# Learn the Bayesian network structure using Maximum Likelihood Estimation
model.fit(X, estimator=MaximumLikelihoodEstimator)

# Print the learned edges in the BayesianModel
print("Learned Bayesian Network Structure:")
print(model.edges())

# Predict the likelihood of fraud for a new transaction
new_transaction = {'transaction_amount': 1000, 'transaction_location': 1, 'cardholder_information': 0, 'cardholder_account_history': 1, 'merchant_information': 2, 'transaction_time': 3, 'ip_address': 5}
fraud_likelihood = model.predict_probability([new_transaction])['is_fraudulent'].values[0]
print("Likelihood of Fraud for the New Transaction:", fraud_likelihood)

    
    
if __name__ == '__main__':
    main()