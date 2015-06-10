import pandas as pd
import numpy as np
import statsmodels.formula.api as sm
from sklearn.linear_model import LinearRegression

#Initialize your dataframe
df = pd.DataFrame()

#add data to the dataframe
for i in xrange(10):
    data = {
        "A":np.random.poisson(5,10000000)[0],
        "B":np.random.chisquare(5,100000)[0],
        "C":np.random.negative_binomial(1000,0.02)
        
    }
    df = df.append(data,ignore_index=True)

#making use of statsmodels
result = sm.ols(formula="A ~ B + C", data=df).fit()
print result.params
print result.summary()

#making use of sklearn
data = np.asarray(df)
lin_reg = LinearRegression()
X,y = data[:,1:],data[:,0]
lin_reg.fit(X,y)
print "coefficients,intercept",lin_reg.coef_,lin_reg.intercept_
