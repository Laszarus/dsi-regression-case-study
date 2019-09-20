import pandas as pd
import matplotlib.pyplot as plt
from clean_data import clean
from pandas.plotting import scatter_matrix
plt.style.use('ggplot')

from sklearn.model_selection import train_test_split

df = clean()

df2 = df.head(10)
scatter_matrix(df[['SalePrice', 'YearMade']], figsize=(15,15))
plt.show()
# g = sns.PairGrid(df2)
# g.map_diag(plt.hist)
# g.map_offdiag(plt.scatter)


