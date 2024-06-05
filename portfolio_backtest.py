import yfinance as yf
import pandas as pd
from tabulate import tabulate

# 定義你想下載數據的ETF代碼
tickers = ['IEF', 'QQQ', 'TQQQ', 'VOO']

# 下載從 2013 年 1 月 1 日到 2023 年 12 月 31 日的數據
data = yf.download(tickers, start='2013-01-01', end='2023-12-31')['Adj Close']

# 定義資產配置比例
weights = {
    'IEF': 0.7,
    'QQQ': 0.3,
    'TQQQ': 0.3,
    'VOO': 0.3
}

# 將數據標準化為起始點為100
normalized_data = data / data.iloc[0] * 100

# 計算每日回報率
returns = normalized_data.pct_change().dropna()

# 計算投資組合回報率
portfolio_returns = pd.DataFrame()
portfolio_returns['IEF_70_QQQ_30'] = returns['IEF'] * weights['IEF'] + returns['QQQ'] * weights['QQQ']
portfolio_returns['IEF_70_TQQQ_30'] = returns['IEF'] * weights['IEF'] + returns['TQQQ'] * weights['TQQQ']
portfolio_returns['IEF_70_VOO_30'] = returns['IEF'] * weights['IEF'] + returns['VOO'] * weights['VOO']

# 計算累積回報率
cumulative_returns = (1 + portfolio_returns).cumprod()

# 計算年化回報率
annualized_returns = cumulative_returns.iloc[-1] ** (1 / 10) - 1

# 將結果轉換為百分比格式
annualized_returns = (annualized_returns * 100).round(2)

# 添加描述欄位
descriptions = [
    '70% 美國國債（IEF）和 30% 納斯達克指數ETF（QQQ）',
    '70% 美國國債（IEF）和 30% 納斯達克反向槓桿ETF（TQQQ）',
    '70% 美國國債（IEF）和 30% 標普500指數ETF（VOO）'
]

# 打印結果表格
result_table = pd.DataFrame({
    '投資組合': annualized_returns.index,
    '描述': descriptions,
    '年化平均回報率': annualized_returns.values
})

# 將結果轉換為Markdown格式並對齊
print(tabulate(result_table, headers='keys', tablefmt='pipe', showindex=False))
