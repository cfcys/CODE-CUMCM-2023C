import pandas as pd
import numpy as np
from tqdm import tqdm
file1  = pd.read_excel("E:/CUMCM 2023/C题/附件1.xlsx")
file2  = pd.read_excel("E:/CUMCM 2023/C题/附件2.xlsx")
file3  = pd.read_excel("E:/CUMCM 2023/C题/附件3.xlsx")
file4  = pd.read_excel("E:/CUMCM 2023/C题/附件4.00.xlsx")
F1 = pd.DataFrame(file1)
F2 = pd.DataFrame(file2)
F3 = pd.DataFrame(file3)
F4 = pd.DataFrame(file4)
F2['类别'] = 0
F2['损耗率'] = 0
F2['单品名称'] = 0
F2['年份'] = F2['销售日期'].dt.year
F2['月份'] = F2['销售日期'].dt.month
for i in tqdm(range(F2.shape[0])):
    F2.loc[i,'类别'] = F1[F1["单品编码"] == F2.loc[i,"单品编码"]]['分类名称'].values
    F2.loc[i,'损耗率'] = F4[F4["单品编码"] == F2.loc[i,"单品编码"]]['损耗率'].values
    F2.loc[i,'单品名称'] = F1[F1["单品编码"] == F2.loc[i,"单品编码"]]['单品名称'].values
F2['类别'] = F2['类别'].str[0]
F2['单品名称'] = F2['单品名称'].str[0]
path = "E:/CUMCM 2023/C题/附件2全面2.0.xlsx"
F2.to_excel(path,index=False)

