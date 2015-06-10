from sklearn import svm

X = [[0,0],[1,1]]
y = [0,1]
clf = svm.SVC() #support vector classifier
clf.fit(X,y)
print clf.predict([0,0])
print clf.predict([1,1])
print clf.predict([0,2])
print clf.predict([1,0])

clf = svm.SVR() #support vector regression
clf.fit(X,y)
print clf.predict([1,1])
print clf.predict([0,0])
print clf.predict([0.1,0.2])
