import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.metrics import f1_score

LINEpath = "../preprocess/metapath.txt"

line = pd.read_csv(LINEpath, header=None, delim_whitespace=True)

GroupPath = "../preprocess/group.txt"

group = pd.read_csv(GroupPath, names=[1,0], delim_whitespace=True).drop(1, axis=1)

group = group-1


X = np.array(line)
y = np.array(group)
y = np.ravel(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

avg_micro=0
avg_macro=0
for i in range(0,5):

    clf = LinearSVC()
    clf.fit(X_train,y_train)

    y_pred = clf.predict(X_test)

    micro = f1_score(y_test,y_pred,average='micro')
    macro = f1_score(y_test,y_pred,average='macro')

    avg_micro = avg_micro + micro
    avg_macro = avg_macro + macro

avg_micro = avg_micro / 5 
avg_macro = avg_macro / 5
print("0.1: avg_micro: %f --- avg_macro: %f" % (avg_micro, avg_macro))
