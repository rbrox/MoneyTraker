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
    ...
    
    
if __name__ == '__main__':
    main()