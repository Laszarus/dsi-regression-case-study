# Heavy Equipment Predictive Linear Regression
## Goals
1. Clean the heavy equipment dataset 
2. Select releveant features
3. Create and test model that predicts auction sale price (<.7 RMSE)

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

**Which features are the most significant?**
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

