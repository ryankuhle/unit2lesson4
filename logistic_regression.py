import pandas as pd
import statsmodels.api as sm
import math

loansData = pd.read_csv('loansData_clean.csv')

for x in loansData['Interest.Rate']:
    loansData['IR_TF'] = (loansData['Interest.Rate'] <= 0.12).astype(int)

loansData['Intercept'] = float(1.0)

ind_vars = ['Amount.Requested', 'FICO.Score', 'Intercept']

logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])

result = logit.fit()

coeff = result.params

def logistic_function(coef, FICO, AMT):
    p = 1 / (1 + math.e ** -(coef['Intercept'] +
                             coef['FICO.Score'] * FICO +
                             coef['Amount.Requested'] * AMT))
    return p


p = logistic_function(coeff, 750, 10000)
print p