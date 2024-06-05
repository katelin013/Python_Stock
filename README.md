# 投資組合回測腳本設置指南

## 1. 安裝所需的Python庫

首先，確保你已經安裝了Python和pip。如果沒有，請安裝Python（[下載鏈接](https://www.python.org/downloads/)）。

然後打開命令行或終端，並運行以下命令來安裝所需的Python庫：

```sh
pip install numpy yfinance
pip install tabulate
pip install pandas
```

## 2. 創建Python腳本

在你新建立的`stock`資料夾中創建一個Python腳本文件，例如 `portfolio_backtest.py`。你可以使用任何文本編輯器或IDE（例如VS Code、PyCharm）。

## 3. 編寫並保存以下Python代碼到`portfolio_backtest.py`文件中

```sh
python portfolio_backtest.py # 執行 portfolio 回測
```

## 4. 運行Python腳本

在命令行或終端中導航到你創建的 `stock` 資料夾，並運行 `portfolio_backtest.py`：

```sh
python portfolio_backtest.py
```

## 結果

運行腳本後，你會看到年化平均回報率的計算結果顯示在命令行或終端中。這將告訴你不同投資組合的年化回報率。

