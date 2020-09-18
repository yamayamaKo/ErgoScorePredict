from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn import svm
from sklearn import linear_model
import numpy as np
import sklearn

print(sklearn.__version__)
def make_response(s):
    response = ""
    s = s[0]

    q, mod = divmod(s,60)
    if(mod<10):
        mod = "0" + str(mod)
    response += str(int(q))+":"+str(mod)[:4]
    return response


def predict(own,pred,input_min,sec,minisec):
    datapath = "data/20test.dat"

    onek = []
    twok = []
    twenty = []
    response = ""

    with open(datapath) as file:
        for s in file:
            l = list(map(float,s.strip().split()))
            tki = l[0]
            twi = l[1]
            oki = l[2]
            onek.append(oki)
            twok.append(tki)
            twenty.append(twi)

    onek = np.array(onek)
    twok = np.array(twok)
    twenty = np.array(twenty)

    onek = np.reshape(onek,(-1,1))
    twok = np.reshape(twok,(-1,1))
    twenty = np.reshape(twenty,(-1,1))

    arrays = {
        "onek":onek,
        "twok":twok,
        "twenty":twenty
    }

    clf = linear_model.LinearRegression()
    clf.fit(arrays[own],np.ravel(arrays[pred]))
    
    if(own == "twenty"):
        score = clf.predict([[input_min]])
        response = make_response(score)
    else:
        score = clf.predict([[input_min*60+sec+minisec*0.1]])
        if(pred == "twenty"):
            response = int(score[0])
        else:
            response = make_response(score)

    return response  



    
"""
clf = linear_model.LinearRegression()
clf.fit(twok,np.ravel(onek))
print(clf.score(twok,onek))

print(clf.predict([[400]]))

clf2 = linear_model.LinearRegression()
clf2.fit(onek,np.ravel(twok))
print(clf2.score(onek,twok))

clf3 = linear_model.LinearRegression()
clf3.fit(onek,np.ravel(twenty))
print(clf3.score(onek,twenty))

clf4 = linear_model.LinearRegression()
clf4.fit(twok,np.ravel(twenty))
print(clf4.score(twok,twenty))

clf5 = linear_model.LinearRegression()
clf5.fit(twenty,np.ravel(onek))
print(clf5.score(twenty,onek))

clf6 = linear_model.LinearRegression()
clf6.fit(twenty,np.ravel(twok))
print(clf6.score(twenty,twok))

import matplotlib.pyplot as plt

plt.scatter(onek,twok)
plt.plot(onek,clf2.predict(onek))
print(clf2.predict([[181.00]]))
"""