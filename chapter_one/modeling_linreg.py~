import pandas as pd
import random as rand


#Initialize your dataframe
df = pd.DataFrame()

#add data to the dataframe
for i in xrange(10):
    data = {
        "column_one":rand.randint(0,500),
        "column two":rand.randint(0,500)
    }
    df = df.append(data,ignore_index=True)

df.to_csv("first.csv")
