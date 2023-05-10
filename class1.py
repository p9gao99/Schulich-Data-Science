import numpy as np
import pandas as pd
df=pd.read_csv('/Users/pengbogao/Desktop/messy_data.csv')
df.info()

df.describe(include='all')
