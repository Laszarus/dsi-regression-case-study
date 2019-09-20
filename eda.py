import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')

from sklearn.model_selection import train_test_split

df = pd.read_csv('predict_auction_price/data/Train.csv')
df = df[df.YearMade != 1000]
df
df.age = df.YearMade

print(df.info())

y = df['SalePrice']
X = df.drop(['SalePrice'], axis = 1)

# column_list = df.columns
# for column in column_list:
#     print(column, len(df[column].unique()))

# ### Looking at prices (our target)
# print(y.describe())

# plt.hist(y)
g = sns.PairGrid(df[['YearMade', 'UsageBand', 'ProductGroup','datasource', 'Drive_System']])
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter)

df = df[df.YearMade != 1000]

df['saleyear'] = df['saledate'].str[-9:-4].astype('int32')
df['age'] = df['saleyear'] - df['YearMade']