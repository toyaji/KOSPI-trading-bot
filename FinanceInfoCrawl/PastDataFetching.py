from pandas_datareader import data, wb
from datetime import datetime, timedelta

# 기간 설정
start = datetime(2010, 1, 1)
end = datetime.now() - timedelta(1)
df = data.DataReader("078930.KS", "yahoo", start, end)
print(df)
# 전체 리스트 가져다가 테이블 만들기