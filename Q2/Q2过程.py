# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from tqdm import tqdm
import warnings
from sklearn.preprocessing import MinMaxScaler
warnings.filterwarnings('ignore')
import time
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf  # Import ACF and PACF plotting functions
from statsmodels.tsa.stattools import adfuller


from Utils import *

# %%
data = pd.read_excel("E:/CUMCM 2023/C题/Q2/Q2TimeSeries数据/茄类.xlsx")

# %%
BAAACK = 1
Item1 = "销量(千克)"
Item2 = "进价(千克)"
Judge(data,Item1,BAAACK)
Judge(data,Item2,BAAACK)

# %%
PlotACFAndPACF_WihthOut(data,Item1,BAAACK)
PlotACFAndPACF_WihthOut(data,Item2,BAAACK)

# %%
PlotACFAndPACF_WihthSeason(data,Item1,BAAACK)
PlotACFAndPACF_WihthSeason(data,Item2,BAAACK)

# %%
# printWhite(data,BAAACK)

# %%
d1 = 1
d2 = 0
p1,q1 = Find_pq(data,Item1,d1,BAAACK)
p2,q2 = Find_pq(data,Item2,d2,BAAACK)

# %%

Get_ResultAndAic(data,Item1,p1,d1,q1,BAAACK)
Get_ResultAndAic(data,Item2,p2,d2,q2,BAAACK)


# %%


# %%


# %%



