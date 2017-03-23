from time import sleep
import pandas as pd
from sqlalchemy import create_engine
from matplotlib import pyplot as plt
import plotly as pl
from plotly import graph_objs as go


def select_all_gener(db):
    """ 사용할 db 명을 인자값으로 받으면 db 돌면서 전체 테이블에서 데이터 끌어옴"""
    engine = create_engine('mysql+pymysql://root:1234@localhost:3306/%s' % db)

    with engine.connect() as con:
        # 메타데이터에서 테이블 리스트 가져와서 하나씩 돌면서 데이터 끌어오기

        for stock in engine.table_names():
            df = pd.read_sql_table(stock, con)
            yield (stock, df)

def volume_price_ration(df):
    # 볼륨이랑 당일 가격 움직을 비율로 해서 반환
    df['VP_Ratio'] = (df['Close'] - df['Open']) / df['Volume']
    return df


if __name__ == '__main__':
    gener = select_all_gener('kospi')


    for _ in gener:
        stock, df = gener.__next__()
        df = volume_price_ration(df)
        graph1 = go.Scatter(x=df.date, y=(df['Close'] - df['Open'])/df['Close']*100)
        graph2 = go.Scatter(x=df.date, y=df['Volume'])
        go.Layout(title=stock)
        pl.offline.init_notebook_mode(connected=True)
        pl.offline.plot([graph1, graph2], filename='Vol_Price_Ratio.html')
        sleep(50)