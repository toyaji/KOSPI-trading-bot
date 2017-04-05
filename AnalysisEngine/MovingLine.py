import pandas as pd
from os.path import expanduser as us
import plotly.graph_objs as go
import plotly as pl

# 데이터 읽어오고 오름차순으로 정렬하기
lg = pd.read_csv(us(r'~\downloads\table.csv'), date_parser=True)
lg = lg.set_index('Date').sort_index(ascending=True)

# 이평선 4개 데이터에 더해주기
moving = [5, 20, 60, 120]
for i in moving:
    lg['ma%s' % i] = lg['Adj Close'].rolling(window=i).mean()

lg.dropna(inplace=True)
lg = lg.loc['2016-04-10':'2017-01-10']
print(lg.head())

# 데이터 뿌릴 값 정해주고 세부 설정해주기
origin = go.Scatter(y=lg['Adj Close'], x=lg.index, mode='lines', name='Origin',
                    line=dict(color='#292C33', width=3))
mean5 = go.Scatter(y=lg['ma5'], x=lg.index, mode='lines', name='Mean5',
                   line=dict(color='#555763', dash='dot'))
mean20 = go.Scatter(y=lg['ma20'], x=lg.index, mode='lines', name='Mean20',
                    line=dict(color='#B2AEAB', dash='dot'))
mean60 = go.Scatter(y=lg['ma60'], x=lg.index, mode='lines', name='Mean60',
                    line=dict(color='#9C8D86', dash='dash'))
mean120 = go.Scatter(y=lg['ma120'], x=lg.index, mode='lines', name='Mean120',
                     line=dict(color='#E4E0D7', dash='dash'))

# 레이아웃 세팅하기
layout = dict(title='LG Display stock price 2016.4.10 - 2017.1.10',
              xaxis=dict(title='Date'), yaxis=dict(title='Price'))


data = [origin, mean5, mean20, mean60, mean120]
#pl.offline.init_notebook_mode(connected=True)
pl.offline.plot({'data':data, 'layout':layout}, filename='LG_Display_Stock_Price.html')