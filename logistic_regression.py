import pandas as pd
import statsmodels.api as sm
import math

def logistic_function(coef, FICO, AMT):
    p = 1 / (1 + math.e ** -(coef['Intercept'] +
                             coef['FICO.Score'] * FICO +
                             coef['Amount.Requested'] * AMT))
    return p

def approval(p):
    if p >= 0.7:
        msg = 'approved'
    else:
        msg = 'denied'
    return msg

loansData = pd.read_csv('loansData_clean.csv')

for x in loansData['Interest.Rate']:
    loansData['IR_TF'] = (loansData['Interest.Rate'] <= 0.12).astype(int)

loansData['Intercept'] = float(1.0)

ind_vars = ['Amount.Requested', 'FICO.Score', 'Intercept']

logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])

result = logit.fit()

coeff = result.params

p = logistic_function(coeff, 750, 10000) #Find probability based on FICO Score and Loan Request
msg = approval(p) #Check approval status based on probability

print 'The loan is {} based on a probability of {:.2%}'.format(msg, p)