import numpy as np
from sklearn import neighbors
import pandas as pd

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

data = np.asarray(df)
X,y = data[:,1:],data[:,0]
clf = neighbors.KNeighborsClassifier()
nbr_listing = []
for k in xrange(10):
    nbrs = neighbors.NearestNeighbors(n_neighbors=k,algorithm="ball_tree").fit(X)
    nbr_listing.append([nbrs.kneighbors(X),k])
clf.fit(X, y)
Z = clf.predict(X)
accuracy=clf.score(X,y)
print ("Predicted model accuracy: "+ str(accuracy))
for i in nbr_listing:
    print "distances,indices,k":i
