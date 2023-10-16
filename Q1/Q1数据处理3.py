import pandas as pd
import numpy as np
import math
from tqdm import tqdm

file = pd.read_excel("E:/CUMCM 2023/C题/附件2按种类分布日期.xlsx")

F = pd.DataFrame(file)

a = 'dddd'
for i in range(F.shape[0]):
    if pd.isnull((F.loc[i,'类别'])):
        F.loc[i,'类别'] = a
    else:
        a = F.loc[i,'类别']

Df1 = pd.DataFrame()
Df1['销售日期'] = 0
Df1['销量'] = 0
Df2 = pd.DataFrame()
Df2['销售日期'] = 0
Df2['销量'] = 0
Df3 = pd.DataFrame()
Df3['销售日期'] = 0
Df3['销量'] = 0
Df4 = pd.DataFrame()
Df4['销售日期'] = 0
Df4['销量'] = 0
Df5 = pd.DataFrame()
Df5['销售日期'] = 0
Df5['销量'] = 0
Df6 = pd.DataFrame()
Df6['销售日期'] = 0
Df6['销量'] = 0

i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
i6 = 0
for i in range(F.shape[0]):
    if F.loc[i,'类别'] == '水生根茎类':
        Df1.loc[i1,'销售日期'] = F.loc[i,'销售日期']
        Df1.loc[i1,'销量'] = F.loc[i,'销量']
        i1 += 1
    elif F.loc[i,'类别'] == '花叶类':
        Df2.loc[i2,'销售日期'] = F.loc[i,'销售日期']
        Df2.loc[i2,'销量'] = F.loc[i,'销量']
        i2 += 1
    elif F.loc[i,'类别'] == '花菜类':
        Df3.loc[i3,'销售日期'] = F.loc[i,'销售日期']
        Df3.loc[i3,'销量'] = F.loc[i,'销量']
        i3 += 1
    elif F.loc[i,'类别'] == '茄类':
        Df4.loc[i4,'销售日期'] = F.loc[i,'销售日期']
        Df4.loc[i4,'销量'] = F.loc[i,'销量']
        i4 += 1
    elif F.loc[i,'类别'] == '辣椒类':
        Df5.loc[i5,'销售日期'] = F.loc[i,'销售日期']
        Df5.loc[i5,'销量'] = F.loc[i,'销量']
        i5 += 1
    else:
        Df6.loc[i6,'销售日期'] = F.loc[i,'销售日期']
        Df6.loc[i6,'销量'] = F.loc[i,'销量']
        i6 += 1

path1 = "E:/CUMCM 2023/C题/按日期分种类/水生根茎类.xlsx"
path2 = "E:/CUMCM 2023/C题/按日期分种类/花叶类.xlsx"
path3 = "E:/CUMCM 2023/C题/按日期分种类/花菜类.xlsx"
path4 = "E:/CUMCM 2023/C题/按日期分种类/茄类.xlsx"
path5 = "E:/CUMCM 2023/C题/按日期分种类/辣椒类.xlsx"
path6 = "E:/CUMCM 2023/C题/按日期分种类/食用菌.xlsx"
Df1.to_excel(path1,index=False)
Df2.to_excel(path2,index=False)
Df3.to_excel(path3,index=False)
Df4.to_excel(path4,index=False)
Df5.to_excel(path5,index=False)
Df6.to_excel(path6,index=False)

# 将没有日期补上0
Df3['销售日期'] = pd.to_datetime(Df3['销售日期'])
# Df3.set_index('销售日期', inplace=True)
start_date = Df3['销售日期'].min()
end_date = Df3['销售日期'].max()
date_range = pd.date_range(start=start_date, end=end_date, freq='D')
new_df1 = pd.DataFrame({'销售日期': date_range})

for i in tqdm(range(new_df1.shape[0])):
    try:
        new_df1.loc[i,'水生根茎类'] = Df1[Df1['销售日期'] == new_df1.loc[i,'销售日期']]['销量'].values
    except Exception as e:
        new_df1.loc[i,'水生根茎类'] = 0
for i in tqdm(range(new_df1.shape[0])):
    try:
        new_df1.loc[i,'花叶类'] = Df2[Df2['销售日期'] == new_df1.loc[i,'销售日期']]['销量'].values
    except Exception as e:
        new_df1.loc[i,'花叶类'] = 0
for i in tqdm(range(new_df1.shape[0])):
    try:
        new_df1.loc[i,'花菜类'] = Df3[Df3['销售日期'] == new_df1.loc[i,'销售日期']]['销量'].values
    except Exception as e:
        new_df1.loc[i,'花菜类'] = 0
for i in tqdm(range(new_df1.shape[0])):
    try:
        new_df1.loc[i,'茄类'] = Df4[Df4['销售日期'] == new_df1.loc[i,'销售日期']]['销量'].values
    except Exception as e:
        new_df1.loc[i,'茄类'] = 0
for i in tqdm(range(new_df1.shape[0])):
    try:
        new_df1.loc[i,'辣椒类'] = Df5[Df5['销售日期'] == new_df1.loc[i,'销售日期']]['销量'].values
    except Exception as e:
        new_df1.loc[i,'辣椒类'] = 0
for i in tqdm(range(new_df1.shape[0])):
    try:
        new_df1.loc[i,'食用菌'] = Df6[Df6['销售日期'] == new_df1.loc[i,'销售日期']]['销量'].values
    except Exception as e:
        new_df1.loc[i,'食用菌'] = 0
new_df1.to_excel("E:/CUMCM 2023/C题/按日期分种类/各种类按日期份补全0.xlsx",index=False)


Df3[Df3['销售日期'] == new_df.loc[1,'销售日期']]['销量'].values

Df3[Df3['销售日期'] == new_df.loc[225,'销售日期']]['销量'].values

new_df.to_excel(path3,index=False)



