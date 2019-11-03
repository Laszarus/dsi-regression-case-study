# Heavy Equipment Predictive Linear Regression
## Goals
1. Clean the heavy equipment dataset 
2. Create and test model that predicts auction sale price (<.7 RMSE)

## The Data
```
Data columns (total 53 columns):
```
```
            SalesID      SalePrice     MachineID        ModelID  \
count  4.011250e+05  401125.000000  4.011250e+05  401125.000000   
mean   1.919713e+06   31099.712848  1.217903e+06    6889.702980   
std    9.090215e+05   23036.898502  4.409920e+05    6221.777842   
min    1.139246e+06    4750.000000  0.000000e+00      28.000000   
25%    1.418371e+06   14500.000000  1.088697e+06    3259.000000   
50%    1.639422e+06   24000.000000  1.279490e+06    4604.000000   
75%    2.242707e+06   40000.000000  1.468067e+06    8724.000000   
max    6.333342e+06  142000.000000  2.486330e+06   37198.000000   

          datasource   auctioneerID       YearMade  MachineHoursCurrentMeter  
count  401125.000000  380989.000000  401125.000000              1.427650e+05  
mean      134.665810       6.556040    1899.156901              3.457955e+03  
std         8.962237      16.976779     291.797469              2.759026e+04  
min       121.000000       0.000000    1000.000000              0.000000e+00  
25%       132.000000       1.000000    1985.000000              0.000000e+00  
50%       132.000000       2.000000    1995.000000              0.000000e+00  
75%       136.000000       4.000000    2000.000000              3.025000e+03  
max       172.000000      99.000000    2013.000000              2.483300e+06  
```

**Which features are the most significant (that are somewhat complete)?**
- *The dictionary was helpful*
![](predict_auction_price/images/dontknow.png)

1. SalePrice
2. Age (YearMade - saleyear)
3. ProductGroup
    - WL (Wheel Loader)
    - SSL (Skid Steer Loaders)
    - TEX (Track Excavators)
    - BL (Backhoe Loaders)
    - TTT (Track Type Tractors)
    - MG (Motor Graders)
4. Turbocharge
5. Enclosure (Enclosed, enclosed with A/C, open)

**Cleaned data**
```
nnamed: 0 	SalePrice 	YearMade 	saleyear 	age 	Turbo_binary 	PrGrp_BL 	PrGrp_MG 	PrGrp_SSL 	PrGrp_TEX 	PrGrp_TTT 	PrGrp_WL 	Enc_EROPS 	Enc_EROPS w AC 	Enc_OROPS
count 	362794.000000 	362794.000000 	362794.000000 	362794.000000 	362794.000000 	362794.000000 	362794.000000 	362794.000000 	362794.000000 	362794.000000 	362794.000000 	362794.000000 	362794.000000 	362794.000000 	362794.000000
mean 	196994.315154 	32224.879659 	1993.787039 	2003.979435 	10.192396 	0.010535 	0.205657 	0.062407 	0.108819 	0.243954 	0.202217 	0.176946 	0.335143 	0.226167 	0.437987
std 	116081.058855 	23428.172346 	9.571299 	5.841061 	7.437785 	0.102098 	0.404181 	0.241894 	0.311413 	0.429466 	0.401654 	0.381624 	0.472041 	0.418349 	0.496140
min 	0.000000 	4750.000000 	1937.000000 	1989.000000 	-12.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000
25% 	96841.250000 	15000.000000 	1988.000000 	2000.000000 	5.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000
50% 	189053.500000 	25000.000000 	1996.000000 	2006.000000 	8.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000
75% 	299852.750000 	42000.000000 	2001.000000 	2009.000000 	13.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	1.000000 	0.000000 	1.000000
max 	401124.000000 	142000.000000 	2013.000000 	2011.000000 	62.000000 	1.000000 	1.000000 	1.000000 	1.000000 	1.000000 	1.000000 	1.000000 	1.000000 	1.000000 	1.000000
```

**Cleaned Data Heatmap**
![](predict_auction_price/images/heatmapv2.png)
Top 3 correlated with SalePrice: 
- A/C (.48)
- SSL (Skid Steer Loaders) (-.32)
- Age (-.25)

**Scatter plot**
![](predict_auction_price/images/scatter.png)

## Results
```
In [2]: run clean_data.py
[0.5289684696650094]
```

## Future steps
- K-folds
- Remove excess dimensions (colinear)
- Attempt inductive model