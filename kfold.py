import numpy as np
#import pandas
from sklearn.model_selection import KFold

with open('wbc.txt') as f:
    content = f.readlines()
kf = KFold(n_splits=3)
k=0;
irr=1;
for train, test in kf.split(content):
    if(irr==1):
        print("iteration:", irr)
        print("number:",test.shape[0])
        print("%s \n" % (test))
        text_file = open("training.txt", "w")
        for k in range(test.shape[0]):
            id=test[k]
            #print(id)
            text_file.write("%s"% content[id] )
        text_file.close()
    else:
        print("iteration:", irr)
        print("number:", test.shape[0])
        print("%s \n" % (test))
        text_file = open("testing.txt", "w")
        for k in range(test.shape[0]):
            id=test[k]
            #print(id)
            text_file.write("%s"% content[id] )
        text_file.close()
    irr += 1;
    #print( "Train",train.shape[0])
    #print("%s \n" % (train))
