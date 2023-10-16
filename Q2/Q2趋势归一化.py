import pandas as pd

df = pd.read_excel("output_销量和售价trend.xlsx")

def min_max_normalize(column):
    min_value = column.min()
    max_value = column.max()
    normalized_column = (column - min_value) / (max_value - min_value)
    return normalized_column


columns_to_normalize = df.columns[1:13]


df[columns_to_normalize] = df[columns_to_normalize].apply(min_max_normalize)

df.to_excel("maxmin_销量和售价trend.xlsx")
