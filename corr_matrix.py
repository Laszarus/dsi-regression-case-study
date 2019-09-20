import numpy as np 
import sklearn as sk 
import matplotlib.pyplot as plt 
import pandas as pd 
plt.style.use('fivethirtyeight')
import os
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df_clean = pd.read_csv('predict_auction_price/data/CleanTrainData.csv')

plt.figure(figsize=(12,10))
cor = df_clean.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
plt.show()
plt.savefig('heatmap.png')