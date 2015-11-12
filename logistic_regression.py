import pandas as pd
import statsmodels.api as sm

loansData = pd.read_csv('loansData_clean.csv')

for x in loansData['Interest.Rate']:
    loansData['IR_TF'] = (loansData['Interest.Rate'] >= 0.12).astype(int)

loansData['Intercept'] = float(1.0)

ind_vars = ['Amount.Requested', 'FICO.Score', 'Intercept']

logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])

#2 - Fit the model
result = logit.fit()

#3 - Get coefficients from results
coeff = result.params
print coeff

def logistic_function(ficoscore, loanamount):
    #p = #?
    return p

#logistic_function(750, 10000)