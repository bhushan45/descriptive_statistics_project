# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]


# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    mean=float(sale_price.mean())
    median = float(sale_price.median())
    mode=np.int64(sale_price.mode())
    return mean,median,mode
