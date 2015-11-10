'''
Add a column to your dataframe indicating whether the interest rate is < 12%. This would be a derived column that you create from the interest rate column. You name it IR_TF. It would contain binary values, i.e.'0' when interest rate < 12% or '1' when interest rate is >= 12%
Do some spot checks to make sure that it worked.
'''

import pandas as pd
import statsmodels.api as sm

loansData = pd.read_csv('loansData_clean.csv')
