import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller
from matplotlib.font_manager import FontProperties

# 设置中文字体名称
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 1. 读取数据
data = pd.read_excel("各种类按日期份全面.xlsx")
# data = pd.read_excel("不同种类每月销量Important.xlsx")

# 2. 可视化“花叶类”蔬菜的销售数据
plt.figure(figsize=(15, 6))
plt.plot(data['销售日期'], data['花叶类'], color='blue')
plt.title('花叶类蔬菜销售数据', fontsize=14, fontweight='bold')
plt.xlabel('销售日期')
plt.ylabel('销售量')
plt.grid(True)
plt.xticks(rotation=45, fontsize=10, ha="right")  # 旋转横坐标标签，设置字体大小，对齐方式
plt.tight_layout()

# 保存图形为PDF文件
plt.savefig("flower_leaves_sales.pdf", format="pdf")

# 3. 进行季节性分解
decomposition = sm.tsa.seasonal_decompose(data['花叶类'], model='additive', period=365)
fig, axes = plt.subplots(4, 1, figsize=(15, 10))
fig.suptitle('季节性分解', fontsize=14, fontweight='bold')
plt.tight_layout(pad=4.0)

# 绘制原始数据
axes[0].plot(data['销售日期'], decomposition.observed, color='green')
axes[0].set_title('原始数据', fontsize=12, fontweight='bold')
axes[0].set_ylabel('销售量')
axes[0].grid(True)
axes[0].tick_params(axis='x', rotation=45, labelsize=10)

# 绘制趋势
axes[1].plot(data['销售日期'], decomposition.trend, color='red')
axes[1].set_title('趋势', fontsize=12, fontweight='bold')
axes[1].set_ylabel('销售量')
axes[1].grid(True)
axes[1].tick_params(axis='x', rotation=45, labelsize=10)

# 绘制季节性
axes[2].plot(data['销售日期'], decomposition.seasonal, color='purple')
axes[2].set_title('季节性', fontsize=12, fontweight='bold')
axes[2].set_ylabel('销售量')
axes[2].grid(True)
axes[2].tick_params(axis='x', rotation=45, labelsize=10)

# 绘制残差的点状图
axes[3].scatter(data['销售日期'], decomposition.resid, color='orange', s=10)
axes[3].set_title('残差', fontsize=12, fontweight='bold')
axes[3].set_ylabel('销售量')
axes[3].grid(True)
axes[3].tick_params(axis='x', rotation=45, labelsize=10)

# 保存季节性分解图形为PDF文件
plt.savefig("seasonal_decomposition.pdf", format="pdf")

# 4. 绘制自相关函数 (ACF) 图
plt.figure(figsize=(15, 6))
plot_acf(data['花叶类'], lags=50, color='blue')
plt.title('自相关函数 (ACF)', fontsize=14, fontweight='bold')
plt.grid(True)  # 添加网格背景
plt.xticks(rotation=45, fontsize=10, ha="right")  # 旋转横坐标标签，设置字体大小，对齐方式

# 保存自相关函数图形为PDF文件
plt.savefig("autocorrelation_function.pdf", format="pdf")

# 5. 绘制单位根检验 (ADF) 图
plt.figure(figsize=(15, 6))
result = adfuller(data['花叶类'])
adf_statistic = result[0]
p_value = result[1]
plt.plot(0, adf_statistic, marker='o', markersize=5, color='red', label='ADF Statistic')
plt.title('单位根检验 (ADF)', fontsize=14, fontweight='bold')
plt.xlabel('检验统计量')
plt.ylabel('ADF Statistic')
plt.grid(True)

# 保存单位根检验图形为PDF文件
plt.savefig("adf_test.pdf", format="pdf")

# 显示所有图形
plt.show()
