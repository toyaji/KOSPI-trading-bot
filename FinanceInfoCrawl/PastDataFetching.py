from pandas_datareader import data, wb
from datetime import datetime, timedelta


def insert_Data():
    # 기간 설정
    start = datetime(2010, 1, 1)
    end = datetime.now() - timedelta(1)

    # 현재 리스트 가져오기
    from FinanceInfoCrawl.StockListNow import listfetching
    codelist = listfetching()

    # SQL 커넥팅
    from sqlalchemy import create_engine, engine
    engine = create_engine('mysql+pymysql://root:1234@localhost:3306/kospi')
    conn = engine.connect()

    # 리스트 돌면서 데이터 집어넣기
    for code in codelist:
        # 해당 리스트의 주가 데이터 끌어오기
        df = data.DataReader(code[1:] + ".KS", "yahoo", start, end)
        df = df.rename(columns={'Adj Close': 'Adj_Close'})
        print(df.head())
        df.to_sql(code, conn, if_exists='append')

if __name__ == '__main__':
    insert_Data()

    # todo A016710 까지 받고 끊어졌음... 아마도 야후에서 막는듯함