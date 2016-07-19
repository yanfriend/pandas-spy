# https://www.datarobot.com/blog/multiple-regression-using-statsmodels/

import pandas as pd
import numpy as np
import statsmodels.api as sm

df_adv = pd.read_csv('./data/Advertising.csv', index_col=0)
X = df_adv[['TV', 'Radio']]
y = df_adv['Sales']
print df_adv.head()

X = df_adv[['TV', 'Radio']]
y = df_adv['Sales']

## fit a OLS model with intercept on TV and Radio
X = sm.add_constant(X)
est = sm.OLS(y, X).fit()

print est.summary()

import statsmodels.formula.api as smf

""" should get same results
# formula: response ~ predictor + predictor
est = smf.ols(formula='Sales ~ TV + Radio', data=df_adv).fit()
print est.summary()
"""




