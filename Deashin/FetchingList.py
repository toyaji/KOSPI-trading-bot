import win32com.client
import pandas

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")
codeList = instCpCodeMgr.GetStockListByMarket(1)
instMarketEye.SetInputValue(0, (4, 67, 70, 111))


kospi = []
for code in codeList:
    name = instCpCodeMgr.CodeToName(code)
    instMarketEye.SetInputValue(1, code)
    instMarketEye.BlockRequest()
    pricenow = instMarketEye.GetDataValue(0, 0)
    per = instMarketEye.GetDataValue(1, 0)
    eps = instMarketEye.GetDataValue(2, 0)
    recentreport = instMarketEye.GetDataValue(3, 0)

    kospi.append([code, name, pricenow, per, eps, recentreport])


f = open('c:\\Users\\Paul\\PycharmProjects\\kospi.csv', "w")
for i in kospi:
    f.write("%s,%s,%d,%d,%d,%s\n" % (str(i[0]),  str(i[1]), int(i[2]), int(i[3]), int(i[4]), str(i[5])))
f.close()

ko = pandas.read_csv('c:\\Users\\Paul\\PycharmProjects\\kospi.csv', encoding = "ISO-8859-1")
print(ko)
