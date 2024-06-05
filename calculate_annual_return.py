import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def get_stock_code(input_value):
    # 如果輸入的是數字，假設是股票代碼，添加 .TW
    if input_value.isdigit():
        return f"{input_value}.TW"
    else:
        return input_value

def get_investment_return(stock_code, start_date, end_date, monthly_investment):
    # 下載股票數據
    data = yf.download(stock_code, start=start_date, end=end_date, interval='1mo')['Adj Close']
    
    if data.empty:
        return None

    # 確保所有月末都有交易數據
    data = data.asfreq('M', method='ffill')

    # 計算定期定額投資的結果
    total_investment = 0
    shares_accumulated = 0
    for date in data.index:
        total_investment += monthly_investment
        shares_accumulated += monthly_investment / data.loc[date]
    
    final_value = shares_accumulated * data.iloc[-1]
    total_gain = final_value - total_investment
    total_return = (final_value / total_investment - 1) * 100

    return {
        "total_investment": total_investment,
        "final_value": final_value,
        "total_gain": total_gain,
        "total_return": total_return
    }

# 設置參數
stock_input = "2359"
months = 6
monthly_investment = 1000.0

# 計算日期範圍
end_date = datetime.now()
start_date = end_date - timedelta(days=months*30)

# 獲取股票代碼
stock_code = get_stock_code(stock_input)

# 獲取計算結果
results = get_investment_return(stock_code, start_date, end_date, monthly_investment)

if results:
    print(f"股票代碼: {stock_code}")
    print(f"總投資金額: {results['total_investment']:.2f} 元")
    print(f"最終投資價值: {results['final_value']:.2f} 元")
    print(f"總收益: {results['total_gain']:.2f} 元")
    print(f"總回報率: {results['total_return']:.2f}%")
else:
    print(f"無法下載股票代碼為 {stock_code} 的數據。請檢查股票代碼是否正確。")
