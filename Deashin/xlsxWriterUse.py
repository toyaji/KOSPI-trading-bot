import win32com.client
import pandas
import xlsxwriter

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")

# 시장의 전체 코드를 리스트로 저장
codeList = instCpCodeMgr.GetStockListByMarket(1)

# 현재가, per, eps, 최근리포팅일자에 대항 request 값 설정
instMarketEye.SetInputValue(0, (4, 67, 70, 111))

workbook = xlsxwriter.Workbook('c:\\Users\\paul\\PycharmProjects\\kospi.xlsx')
worksheet = workbook.add_worksheet()


# 코드 리스트 돌면서 관련 값 끌어오는 iter 작성
for i, code in enumerate(codeList):
    secondCode = instCpCodeMgr.GetStockSectionKind(code)
    name = instCpCodeMgr.CodeToName(code)
    instMarketEye.SetInputValue(1, code)
    instMarketEye.BlockRequest()
    pricenow = instMarketEye.GetDataValue(0, 0)
    per = instMarketEye.GetDataValue(1, 0)
    eps = instMarketEye.GetDataValue(2, 0)
    recentreport = instMarketEye.GetDataValue(3, 0)

    worksheet.write(i, 0, i)
    worksheet.write(i, 1, code)
    worksheet.write(i, 2, secondCode)
    worksheet.write(i, 3, name)
    worksheet.write(i, 4, pricenow)
    worksheet.write(i, 5, per)
    worksheet.write(i, 6, eps)
    worksheet.write(i, 7, recentreport)


workbook.close()

