# %%
import pandas as pd
import numpy as np
from tqdm import tqdm
from sklearn.preprocessing import StandardScaler
import warnings
from sklearn.preprocessing import MinMaxScaler
warnings.filterwarnings('ignore')

# %%
file =  pd.read_excel("E:/CUMCM 2023/C题/Q2/销售日期类别初步统计4正确思路.xlsx")

# %%
F = pd.DataFrame(file)

# %%
for i in tqdm(range(F.shape[0])):
    if pd.isnull(F.loc[i,'销售日期']):
        F.loc[i,'销售日期'] = a
    else:
        a = F.loc[i,'销售日期']

# %%
水生根茎类 = pd.DataFrame()
花叶类 = pd.DataFrame()
花菜类 = pd.DataFrame()
茄类 = pd.DataFrame()
辣椒类 = pd.DataFrame()
食用菌	= pd.DataFrame()

# %%
F

# %%
for i in tqdm(range(F.shape[0])):
    if F.loc[i,'类别'] == '水生根茎类':
        水生根茎类 = 水生根茎类.append(F.loc[i])
    elif F.loc[i,'类别'] == '花叶类':
        花叶类 = 花叶类.append(F.loc[i])
    elif F.loc[i,'类别'] == '花菜类':
        花菜类 = 花菜类.append(F.loc[i])
    elif F.loc[i,'类别'] == '茄类':
        茄类 = 茄类.append(F.loc[i])
    elif F.loc[i,'类别'] == '辣椒类':
        辣椒类 = 辣椒类.append(F.loc[i])
    else :
        食用菌 = 食用菌.append(F.loc[i])

# %%
辣椒类

# %%
def get_Loss(data):
    return data['总损耗值(千克)'].sum() / data['销量(千克)'].sum()
def get_Profit(data):
    return data['平均利率乘以销量'].sum() / data['销量(千克)'].sum()

# %%
get_Loss(食用菌)

# %%
scaler = MinMaxScaler(feature_range=(0, 1))
水生根茎类['销量(千克)'] = scaler.fit_transform(水生根茎类[['销量(千克)']].values)
水生根茎类['销售单价(元/千克)'] = scaler.fit_transform(水生根茎类[['销售单价(元/千克)']].values)

# %%
scaler = MinMaxScaler(feature_range=(0, 1))
花叶类['销量(千克)'] = scaler.fit_transform(花叶类[['销量(千克)']].values)
花叶类['销售单价(元/千克)'] = scaler.fit_transform(花叶类[['销售单价(元/千克)']].values)

# %%
scaler = MinMaxScaler(feature_range=(0, 1))
花菜类['销量(千克)'] = scaler.fit_transform(花菜类[['销量(千克)']].values)
花菜类['销售单价(元/千克)'] = scaler.fit_transform(花菜类[['销售单价(元/千克)']].values)

# %%
scaler = MinMaxScaler(feature_range=(0, 1))
茄类['销量(千克)'] = scaler.fit_transform(茄类[['销量(千克)']].values)
茄类['销售单价(元/千克)'] = scaler.fit_transform(茄类[['销售单价(元/千克)']].values)

# %%
scaler = MinMaxScaler(feature_range=(0, 1))
辣椒类['销量(千克)'] = scaler.fit_transform(辣椒类[['销量(千克)']].values)
辣椒类['销售单价(元/千克)'] = scaler.fit_transform(辣椒类[['销售单价(元/千克)']].values)

# %%
scaler = MinMaxScaler(feature_range=(0, 1))
食用菌['销量(千克)'] = scaler.fit_transform(食用菌[['销量(千克)']].values)
食用菌['销售单价(元/千克)'] = scaler.fit_transform(食用菌[['销售单价(元/千克)']].values)

# %%
水生根茎类.to_excel("E:/CUMCM 2023/C题/Q2/水生根茎类销量单价关系2.xlsx",index=False)
花叶类.to_excel("E:/CUMCM 2023/C题/Q2/花叶类销量单价关系2.xlsx",index=False)
花菜类.to_excel("E:/CUMCM 2023/C题/Q2/花菜类销量单价关系2.xlsx",index=False)
茄类.to_excel("E:/CUMCM 2023/C题/Q2/茄类销量单价关系2.xlsx",index=False)
辣椒类.to_excel("E:/CUMCM 2023/C题/Q2/辣椒类销量单价关系2.xlsx",index=False)
食用菌.to_excel("E:/CUMCM 2023/C题/Q2/食用菌销量单价关系2.xlsx",index=False)

# %%
def getGroup(data):
    data['销售日期'] = pd.to_datetime(data['销售日期'])
    data['年份'] = data['销售日期'].dt.year
    data['月份'] = data['销售日期'].dt.month
    data['年月'] = data['年份'] + data['月份']*0.01
    data = data.groupby(['年月']).agg({'销量(千克)':'sum','总进价':'sum'})
    data['进价(千克)'] = data['总进价'] / data['销量(千克)']
    return data

# %%
path = "E:/CUMCM 2023/C题/Q2/Q2TimeSeries数据/"
getGroup(食用菌).to_excel(path + "食用菌.xlsx")

# %%
path = "E:/CUMCM 2023/C题/Q2/"
辣椒月.to_excel(path+'辣椒月.xlsx')

# %%
path = "E:/CUMCM 2023/C题/Q2/"
# 辣椒月.to_excel(path+'辣椒月.xlsx')
水生根茎类.to_excel(path+'水生根茎月.xlsx')
花叶类.to_excel(path+'花叶月.xlsx')
花菜类.to_excel(path+'花菜月.xlsx')
茄类.to_excel(path+'茄月.xlsx')
食用菌.to_excel(path+'食用菌月.xlsx')

# %%
水生根茎类

# %%



