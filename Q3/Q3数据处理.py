# %%
import pandas as pd
import numpy as np
import warnings
from sklearn.preprocessing import MinMaxScaler
warnings.filterwarnings('ignore')

# %%
file1 = pd.read_excel("E:/CUMCM 2023/C题/Q3/Q3所需数据/Q3定价7天变化.xlsx")
file2 = pd.read_excel("E:/CUMCM 2023/C题/Q3/Q3所需数据/Q3定价-进价7天变化.xlsx")
file3 = pd.read_excel("E:/CUMCM 2023/C题/Q3/Q3所需数据/Q3利率7天变化.xlsx")
file4 = pd.read_excel("E:/CUMCM 2023/C题/Q3/Q3所需数据/Q3销量7天变化.xlsx")
file5 = pd.read_excel("E:/CUMCM 2023/C题/Q3/Q3所需数据/Q3进价7天变化.xlsx")

# %%
定价 = pd.DataFrame(file1)
定价减进价 = pd.DataFrame(file2)
利率 = pd.DataFrame(file3)
销量 = pd.DataFrame(file4)
进价 = pd.DataFrame(file5)

# %%
进价['进价均值'] = 进价.mean(axis = 1)
销量['销量均值'] = 销量.mean(axis = 1)
定价['定价均值'] = 定价.mean(axis = 1)

# %%
数据汇总 = pd.DataFrame()
数据汇总['单品名称'] = 定价['单品名称']

# %%
数据汇总['进价预测值'] = 进价['进价均值']
数据汇总['销量预测值'] = 销量['销量均值']
数据汇总['定价预测值'] = 定价['定价均值']

# %%
# 创建一个StandardScaler对象
scaler = MinMaxScaler()

# 使用StandardScaler对象拟合并转换列1
数据汇总['销量预测值_normalized'] = scaler.fit_transform(数据汇总[['销量预测值']])

# %%
random_numbers = np.random.normal(1, 5, len(数据汇总))
a = 0.3
数据汇总['七月一日前的剩货量'] = random_numbers * 数据汇总['销量预测值_normalized']

# 数据汇总['进货率'] = 0.15*(1 - a*数据汇总['七月一日前的剩货量'])
数据汇总

# %%
for i in range(数据汇总.shape[0]):
    if 数据汇总.loc[i,'七月一日前的剩货量'] < 0.05:
        数据汇总.loc[i,'七月一日前的剩货量'] = 0

# %%
a = 0.1
数据汇总['进货率'] = 0.15*(1 - a*数据汇总['七月一日前的剩货量'])

# %%
数据汇总['补货量'] = (数据汇总['进货率'] + 1) * 数据汇总['销量预测值'] - 数据汇总['七月一日前的剩货量']

# %%
数据汇总

# %%
Top = pd.read_csv("topsis结果.csv")
Top = pd.DataFrame(Top)
Results = pd.DataFrame()
Results['单品名称'] = Top['索引']

# %%
from tqdm import tqdm
for i in tqdm(range(Top.shape[0])):
    Results.loc[i,'进价预测值'] = 数据汇总[数据汇总["单品名称"] == Results.loc[i,'单品名称']]['进价预测值'].values
    Results.loc[i,'销量预测值'] = 数据汇总[数据汇总["单品名称"] == Results.loc[i,'单品名称']]['销量预测值'].values
    Results.loc[i,'销量预测值_01标准化'] = 数据汇总[数据汇总["单品名称"] == Results.loc[i,'单品名称']]['销量预测值_normalized'].values
    Results.loc[i,'七月一日前的剩货量'] = 数据汇总[数据汇总["单品名称"] == Results.loc[i,'单品名称']]['七月一日前的剩货量'].values
    Results.loc[i,'定价预测值'] = 数据汇总[数据汇总["单品名称"] == Results.loc[i,'单品名称']]['定价预测值'].values
    Results.loc[i,'补货量'] = 数据汇总[数据汇总["单品名称"] == Results.loc[i,'单品名称']]['补货量'].values
    Results.loc[i,'进货率'] = 数据汇总[数据汇总["单品名称"] == Results.loc[i,'单品名称']]['进货率'].values

# %%
损耗率结果 = pd.read_excel("蔬菜销售统计带次数.xlsx")
a = pd.DataFrame(损耗率结果)


# %%
from tqdm import tqdm
for i in tqdm(range(Top.shape[0])):
    Results.loc[i,'损耗率'] = a[a["单品名称"] == Results.loc[i,'单品名称']]['损耗率'].values*0.01


# %%
Results['现货量'] = Results['七月一日前的剩货量']*Results['损耗率'] + Results['补货量']

# %%
Results['盈利额'] = (Results['定价预测值'] - Results['进价预测值']) * Results['销量预测值']

# %%
Results.to_excel('E:/CUMCM 2023/C题/Q3/Q3结果一.xlsx')

# %%



