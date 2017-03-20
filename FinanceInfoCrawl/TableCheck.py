import win32com.client
import os

def tablecheck():
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

    # 테이블 접속상태 확인하기
    tab = [stock for stock in codeList]


    from FinanceInfoCrawl.TableCreateMysql import create_tables
    for i in tab:
        # if i in
        create_tables(i)