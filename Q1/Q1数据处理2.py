
import pandas as pd
import numpy as np


file = pd.read_excel("E:/CUMCM 2023/C题/附件2全面2.0.xlsx")
F = pd.DataFrame(file)

total = F.groupby(['年份','月份','类别']).sum()

path = "E:/CUMCM 2023/C题/附件2按月份分布.xlsx"
total.to_excel(path)

total = F.groupby(['类别','销售日期']).sum()
path = "E:/CUMCM 2023/C题/附件2按种类分布日期.xlsx"

total.to_excel(path)


