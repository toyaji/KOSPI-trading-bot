from datetime import datetime, timedelta
from pandas_datareader import data, wb

start = datetime(2010, 1, 1)
end = datetime.now() - timedelta(1)

# 현재 리스트 가져오기
from FinanceInfoCrawl.StockListNow import listfetching
codelist = listfetching()
code = [x for x in codelist]

df = data.DataReader(code[1] + ".KS", "yahoo", start, end)

print(df.head())

