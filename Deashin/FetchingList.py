import win32com.client
import pandas

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")

# 시장의 전체 코드를 리스트로 저장
codeList = instCpCodeMgr.GetStockListByMarket(1)

# 현재가, per, eps, 최근리포팅일자에 대항 request 값 설정
instMarketEye.SetInputValue(0, (4, 67, 70, 111))


kospi = []

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

    kospi.append([i, code, secondCode, name, pricenow, per, eps, recentreport])


f = open('c:\\Users\\user\\PycharmProjects\\kospi.csv', "w")
for i in kospi:
    f.write("%d,%s,%s,%s,%d,%d,%d,%s\n" % (int(i[0]), str(i[1]),  str(i[2]), str(i[3]), int(i[4]), int(i[5]), int(i[6]), str(i[7])))
f.close()

ko = pandas.read_csv('c:\\Users\\user\\PycharmProjects\\kospi.csv', encoding = "ISO-8859-1")
print(ko)
