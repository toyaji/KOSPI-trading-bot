import win32com.client
import pandas as pd
import numpy as np

def listfetching():
    # 현재 로그인 상태 확인하고 리스트 가져오는 시도하기
    instCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
    if instCpCybos.IsConnect == 1:
        # 시장 전체 종목 리스트로 가져오기
        try:
            instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
            codeList = instCpCodeMgr.GetStockListByMarket(1)
        except Exception:
            print("연결상태 확인바람")
            exit()
    return codeList


def newStock():
    """기존 종목 리스트 csv 로 보관하고 있다가
    대신증권 종목 리스트와 비교해서 새로운 종목 있으면 테이블 추가
    사라진 종목 있으면 테이블 삭제하는 기능"""

    # 신규 리스트 접속해서 가져오기
    newlist = list(listfetching())
    newset = set(newlist)
    # 기존 파일에서 리스트 가져오기
    file = './Listnow.csv'
    df = pd.read_csv(file, sep='\n', names=['oldlist'])
    oldset = set(df['oldlist'])

    print('기존 종목 수 : %d  //  현재 종목 수 : %d' % (len(df), len(newlist)))
    change = {}

    # 뭐가 없어 졌는지 찾기
    add = newset - oldset
    sub = oldset - newset
    print('신규종목 : %s  //  폐지종목 : %s' % (add, sub))

    # 테이블 만들고 삭제하기
    from FinanceInfoCrawl.TableCreateMysql import create_tables, table_drop
    for code in add: create_tables(code)
    for code in sub: table_drop(code)

    # 변경 사항 파일에 쓰기
    with open(file, 'w') as f:
        for code in newlist:
            f.write(code + '\n')



if __name__ == '__main__':
    newStock()