import pandas as pd
import statsmodels.api as sm

loansData = pd.read_csv('loansData_clean.csv')

for x in loansData['Interest.Rate']:
    loansData['IR_TF'] = (loansData['Interest.Rate'] >= 0.12).astype(int)

loansData['intercept'] = float(1.0)

#print loansData['intercept'][0:5]