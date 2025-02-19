import pandas as pd
train=pd.read_csv('ahamed.csv')

train.loc[train['use [kW]']>=1,'use [kW]']=1
train.loc[train['use [kW]']<1,'use [kW]']=0
train['use [kW]'].unique()

spam = train[train['use [kW]'] == 0].shape
print('Spam Data     : ', spam)

non_spam = train[train['use [kW]'] == 1].shape
print('Non Spam Data : ', non_spam)
data_size=list(train.shape)
data_size=data_size[0]
print('\nSpam Data')
for i in range(0, data_size):
        train_ip1 = train.iloc[[i]]
        train_spam = train_ip1.loc[::, 'use [kW]']
        for spam in train_spam:
            if spam < 1:
                print('\nSpam\n', train_ip1)
print('\nNon Spam Data')
for j in range(0, data_size):
        train_ip2 = train.iloc[[j]]
        train_spam = train_ip2.loc[::, 'use [kW]']
        for spam in train_spam:
            if spam >= 1:
                print('\nNon Spam\n', train_ip2)