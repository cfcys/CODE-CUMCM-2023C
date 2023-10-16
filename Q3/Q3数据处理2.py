import pandas as pd

# 读取Excel文件
file_path = 'Q3最近一周所有交易记录.xlsx'
df = pd.read_excel(file_path)

# 计算每个单品名称的总销售额、总成本、总盈利额、平均损耗率和购买次数
result = df.groupby('单品名称').agg({
    '销售额': 'sum',
    '成本': 'sum',
    '盈利额': 'sum',
    '损耗率': 'mean',
    '销量(千克)': 'sum'
}).reset_index()

# 保留"类别"列
result['类别'] = df.groupby('单品名称')['类别'].first().values

# 计算每个单品的购买次数
purchase_counts = df['单品名称'].value_counts().reset_index()
purchase_counts.columns = ['单品名称', '购买次数']

# 合并购买次数列到结果DataFrame
result = pd.merge(result, purchase_counts, on='单品名称')

# 将结果保存到Excel文件
result.to_excel('蔬菜销售统计带次数.xlsx', index=False)

df = pd.read_excel('Q3最近一周所有交易记录.xlsx')

# 使用pivot_table函数创建透视表格
pivot_table = df.pivot_table(values='销量(千克)', index='单品名称', columns='销售日期', aggfunc='sum', fill_value=0)

# 打印透视表格
print(pivot_table)
pivot_table.to_excel('Q3销量7天变化.xlsx')
# 使用pivot_table函数创建透视表格
pivot_table2 = df.pivot_table(values='进价', index='单品名称', columns='销售日期', aggfunc='first')

print(pivot_table2)
pivot_table2.to_excel('Q3进价7天变化.xlsx')
pivot_table2 = df.pivot_table(values='定价-进价', index='单品名称', columns='销售日期', aggfunc='first')

print(pivot_table2)
pivot_table2.to_excel('Q3定价-进价7天变化.xlsx')
pivot_table2 = df.pivot_table(values='利率', index='单品名称', columns='销售日期', aggfunc='first')

print(pivot_table2)
pivot_table2.to_excel('Q3利率7天变化.xlsx')
pivot_table2 = df.pivot_table(values='销售单价(元/千克)', index='单品名称', columns='销售日期', aggfunc='first')

print(pivot_table2)
pivot_table2.to_excel('Q3定价7天变化.xlsx')