
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


def Judge(data,Item,Back):
    # 创建时间的序列
    start_date = "2020-07-01"
    end_date = "2023-06-30"
    date_range = pd.date_range(start=start_date, end=end_date, freq='M')
    # 创建一个包含月份的DataFrame
    month_df = pd.DataFrame({'销售月': date_range})
    data['年月'] = month_df['销售月']
    data['年月'] = pd.to_datetime(data['年月'])
    data.set_index('年月', inplace=True)

    # 4. 计算一阶差分和季节性差分
    data_diff = data[Item].diff(1)
    seasonal_diff = data_diff.diff(12)

    # 进行ADF检验
    result = adfuller(seasonal_diff[13:])
    # 打印ADF检验结果
    print('ADF统计量:', result[0])
    print('P-值:', result[1])
    print('滞后阶数:', result[2])
    print('观测数:', result[3])
    print('临界值:', result[4])
    print('经过一阶季节差分之后是否拒绝原假设（数据平稳）:', result[1] <= 0.05)

    # 进行ADF检验
    result = adfuller(data_diff[1:])
    # 打印ADF检验结果
    print('ADF统计量:', result[0])
    print('P-值:', result[1])
    print('滞后阶数:', result[2])
    print('观测数:', result[3])
    print('临界值:', result[4])
    print('经过'+str(Back)+'阶差分之后是否拒绝原假设（数据平稳）:', result[1] <= 0.05)

     # 进行ADF检验
    result = adfuller(data[Item])
    # 打印ADF检验结果
    print('ADF统计量:', result[0])
    print('P-值:', result[1])
    print('滞后阶数:', result[2])
    print('观测数:', result[3])
    print('临界值:', result[4])
    print('原始数据是否拒绝原假设（数据平稳）:', result[1] <= 0.05)
    return 

def PlotTimeSeries(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['销量(千克)'])
    plt.title('辣椒销量时间序列')
    plt.xlabel('销售日期')
    plt.ylabel('销量(千克)')
    plt.show()

def PlotACFAndPACF_WihthOut(data,Item,Back):
    # Plot ACF and PACF for the seasonal_diff data
    data_diff = data[Item].diff(Back)
    # seasonal_diff = data_diff.diff(12)
    
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plot_acf(data_diff.dropna(), lags=34, ax=plt.gca())
    plt.title('ACF of Seasonal Differenced Data')

    plt.subplot(2, 1, 2)
    plot_pacf(data_diff.dropna(), lags=16, ax=plt.gca())
    plt.title('PACF of Seasonal Differenced Data')

def PlotACFAndPACF_WihthSeason(data,Item,Back):
    # Plot ACF and PACF for the seasonal_diff data
    data_diff = data[Item].diff(Back)
    seasonal_diff = data_diff.diff(12)
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plot_acf(seasonal_diff.dropna(), lags=22, ax=plt.gca())
    plt.title('ACF of Seasonal Differenced Data')

    plt.subplot(2, 1, 2)
    plot_pacf(seasonal_diff.dropna(), lags=10, ax=plt.gca())
    plt.title('PACF of Seasonal Differenced Data')

def printWhite(data,Back):
    data_diff = data['销量(千克)'].diff(Back)
    seasonal_diff = data_diff.diff(12)
    res = acorr_ljungbox(data['销量(千克)'], lags=[6,12,24], boxpierce=True, return_df=True)
    print("销量/千克的白噪声情况是")
    print(res)
    data_diff = data['进价(元/每千克)'].diff(1)
    seasonal_diff = data_diff.diff(12)
    res = acorr_ljungbox(data['进价(元/每千克)'], lags=[6,12,24], boxpierce=True, return_df=True)
    print("进价(元/每千克)的白噪声情况是")
    print(res)

def Find_pq(data,Item,d,Back):
    min_aic = float('237189372193')  
    minq = 0
    minp = 0
    
    for p in range(0,5):
        for q in range(0,5):
            # print(p,q)
            model = SARIMAX(data[Item], order=(1, Back, 1), seasonal_order=(p, d, q, 12),enforce_stationarity=False)
            results = model.fit()
            a = results.aic
            if results.aic < min_aic:
                min_aic = results.aic
                minq = q
                minp = p
    print('最小的AIC值:',min_aic)
    print('合适的P', minp)
    print('合适的Q', minq)
    return minp,minq

def Get_ResultAndAic(data,Item,p,d,q,Back):
    model = SARIMAX(data[Item], order=(1, Back, 1), seasonal_order=(p,d,q , 12))
    start_time = time.time()  # 开始计时
    results = model.fit()
    end_time = time.time()  # 结束计时
    elapsed_time = end_time - start_time  # 计算所需时间（秒）
    # print("模型拟合所需时间：", elapsed_time, "秒")
    forecast = results.get_forecast(steps=1)
    forecast_mean = forecast.predicted_mean
    print("预测的销量/进价为")
    print(forecast_mean)
    print("当前的Aic值为")
    print(results.aic)
