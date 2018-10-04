import pandas as pd


def testme():
    df=pd.read_csv('sample.txt',sep='|',header=None)
    print(df.shape)



