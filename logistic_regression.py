import pandas as pd
import statsmodels.api as sm

loansData = pd.read_csv('loansData_clean.csv')

for x in loansData['Interest.Rate']:
    loansData['IR_TF'] = (loansData['Interest.Rate'] >= 0.12).astype(int)

#print loansData['IR_TF'][0:5]