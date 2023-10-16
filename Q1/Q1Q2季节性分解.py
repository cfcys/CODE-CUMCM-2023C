import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller
from matplotlib.font_manager import FontProperties
from matplotlib.dates import MonthLocator, DateFormatter


# 设置中文字体名称
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体

veg = ['花菜类','花叶类','茄类','辣椒类','水生根茎类','食用菌']
vegetable = pd.DataFrame()
for i in veg:
    # 1. 读取数据
    data = pd.read_excel(i+"modifiedtime.xlsx")



    # 2. 可视化“花叶类”蔬菜的销售数据
    plt.figure(figsize=(15, 6))
    plt.plot(data['销售日期'], data['销售单价(元/千克)'], color='blue')
    plt.title(i+'销量单价关系', fontsize=14, fontweight='bold')
    plt.xlabel('销售日期')
    plt.ylabel('销售量')
    plt.grid(True)

    # 保存图形为PDF文件
    plt.savefig("flower_leaves_sales.pdf", format="pdf")

    # 3. 进行季节性分解
    decomposition1 = sm.tsa.seasonal_decompose(data['销售单价(元/千克)'], model='additive', period=365)
    fig, axes = plt.subplots(1, 1, figsize=(15, 5))
    fig.suptitle('季节性分解', fontsize=14, fontweight='bold')
    plt.tight_layout(pad=4.0)


    # 绘制原始数据
    axes[0].plot(data['销售日期'], decomposition1.observed, color='green')
    axes[0].set_title('原始数据', fontsize=12, fontweight='bold')
    axes[0].set_ylabel('销售量')
    axes[0].grid(True)

    # 绘制趋势
    axes.plot(data['销售日期'], decomposition1.trend, color='red')
    axes.set_title('趋势', fontsize=12, fontweight='bold')
    axes.set_ylabel('销售量')
    axes.grid(True)

    # 绘制季节性
    axes[2].plot(data['销售日期'], decomposition1.seasonal, color='purple')
    axes[2].set_title('季节性', fontsize=12, fontweight='bold')
    axes[2].set_ylabel('销售量')
    axes[2].grid(True)

    # 绘制残差的点状图
    axes[3].scatter(data['销售日期'], decomposition1.resid, color='orange', s=10)
    axes[3].set_title('残差', fontsize=12, fontweight='bold')
    axes[3].set_ylabel('销售量')
    axes[3].grid(True)

    # 保存季节性分解图形为PDF文件
    plt.savefig(i+"seasonal_decomposition单价.pdf", format="pdf")

    # 4. 绘制自相关函数 (ACF) 图
    plt.figure(figsize=(15, 6))
    plot_acf(data['销售单价(元/千克)'], lags=50, color='blue')
    plt.title('自相关函数 (ACF)', fontsize=14, fontweight='bold')
    plt.grid(True)  # 添加网格背景

    plt.gca().xaxis.set_major_locator(months)
    plt.gca().xaxis.set_major_formatter(date_format)
    plt.xticks(rotation=45, fontsize=10, ha="right") 

    # 保存自相关函数图形为PDF文件
    plt.savefig("autocorrelation_function.pdf", format="pdf")

    #2. 可视化“花叶类”蔬菜的销售数据
    plt.figure(figsize=(15, 6))
    plt.plot(data['销售日期'], data['销量(千克)'], color='blue')
    plt.title('辣椒类销量单价关系', fontsize=14, fontweight='bold')
    plt.xlabel('销售日期')
    plt.ylabel('销售量')
    plt.grid(True)

    plt.savefig("flower_leaves_sales.pdf", format="pdf")

    # 3. 进行季节性分解
    decomposition2 = sm.tsa.seasonal_decompose(data['销量(千克)'], model='additive', period=365)
    fig, axes = plt.subplots(1, 1, figsize=(15, 5))
    fig.suptitle('季节性分解', fontsize=14, fontweight='bold')
    plt.tight_layout(pad=4.0)
    # 绘制趋势
    axes.plot(data['销售日期'], decomposition2.trend, color='red')
    axes.set_title('趋势', fontsize=12, fontweight='bold')
    axes.set_ylabel('销售量')
    axes.grid(True)
    # 保存季节性分解图形为PDF文件
    plt.savefig(i+"seasonal_decomposition销量.pdf", format="pdf")
    plt.show()
    vegetable=pd.concat([vegetable,decomposition1.trend],axis=1)
    vegetable=pd.concat([vegetable,decomposition2.trend],axis=1)