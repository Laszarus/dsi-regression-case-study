import pandas as pd
import matplotlib.pyplot as plt
from clean_data import clean
from pandas.plotting import scatter_matrix
plt.style.use('ggplot')

df = clean()

df2 = df.sample(frac = 0.05)

colors = {'WL':'red', 'SSL':'blue', 'TEX':'green', 'BL':'black', 'TTT':'orange', 'MG': 'cyan'}

fig, ax = plt.subplots(1,1)
# plt.figure(figsize=(20,8))
ax.scatter(df2['age'], df2['SalePrice'], c=df2['ProductGroup'].apply(lambda x: colors[x]), alpha = 0.3)
ax.set_xlabel('Age of Equipment (years)')
ax.set_ylabel('Sale Price (USD)')
ax.set_xlim(0,60)
ax.set_title('Age vs Price (colored by Product Group)')
ax.legend()

plt.show()





