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
    newlist = list(listfetching())
    file = './Listnow.csv'

    # 기존 파일에서 리스트 가져오기
    df = pd.read_csv(file, sep='\n', names=['oldlist'])
    # todo fix comparison " 둘이 비교하면 길이 달라서 에러남"
    df['newlist'] = newlist
    print(df.head())

    # 이전내역하고 현재 내역 비교하기
    mask = df['oldlist'] != df['newlist']
    extract1 = df['newlist'][mask]
    extract2 = df['oldlist'][mask]

    # 서로 비교해서 입력하기
    if len(np.array(extract1)) != 0 & len(np.array(extract2)) != 0:
        with open(file, 'w') as f:
            for code in np.array(df['newlist']):
                f.write(code + '\n')





if __name__ == '__main__':
    newStock()