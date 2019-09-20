import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.plotting import scatter_matrix
from statistics import mean

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.base import clone


import matplotlib.pyplot as plt
from predict_auction_price.score_model import rmsle

plt.style.use("ggplot")

# def rmsle(actual, predictions):
#     log_diff = np.log(predictions+1) - np.log(actual+1)
#     return np.sqrt(np.mean(log_diff**2))

df = pd.read_csv('predict_auction_price/data/Train.csv', low_memory=False)

df = df[['SalePrice', 'YearMade', 'saledate', 
        'Enclosure','Turbocharged', 'ProductGroup', ]]

#Eliminate rows with YearMade = 1000 and calculate age column
df = df[df.YearMade != 1000]
df['saleyear'] = df['saledate'].str[-9:-4].astype('int32')
df['age'] = df['saleyear'] - df['YearMade']

# Create binary turbo column
df['Turbo_binary'] = df['Turbocharged'].map(lambda x: 1.0 if x == "Yes" else 0.0)

#product group dummies
prod_group_dummies = pd.get_dummies(df['ProductGroup'], prefix='PrGrp')
df = pd.concat([df, prod_group_dummies], axis = 1)


# will leave us with three options: OROPS, EROPS, EROPS w AC
df['Enclosure'] = df['Enclosure'].map(lambda x: 'EROPS w AC' if x == 'EROPS AC' else x)
df['Enclosure'] = df['Enclosure'].map(lambda x: 'OROPS' if x == 'NO ROPS' else x)
df = df[df.Enclosure != 'None or Unspecified']

#enclosure group dummies
enc_dummies = pd.get_dummies(df['Enclosure'], prefix='Enc')
df = pd.concat([df, enc_dummies], axis = 1)

df.dropna(subset=['SalePrice','age','Enclosure','ProductGroup',],inplace=True)


df.drop(['Turbocharged'],axis = 1, inplace=True)
target_column='SalePrice'

X=df.drop(['SalePrice','YearMade','saleyear','saledate','Enclosure','ProductGroup'],axis=1)
y=df['SalePrice']

X_train, X_test, y_train, y_test = train_test_split(X, y)

#casting df to arrays
# X = np.array(X)
# y = np.array(y)

# kf = KFold(n_splits=10, random_state=42)
# for train_index, test_index in kf.split(X):
        
#         X_train, X_test = X[train_index], X[test_index]
#         y_train, y_test = y[train_index], y[test_index]

#for train_index, test_index in kfold.split(X_train):
model = LinearRegression()

model.fit(X_train, y_train)
y_predict = model.predict(X_test)

# print(f"y_test: {type(y_test)}, y_predict: {type(y_predict)}")

rmsles = [rmsle(y_test, y_predict)]
# meanrmlse=mean(rmsles)
print(rmsles)