import win32com.client
import pandas

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
instCpStock = win32com.client.Dispatch("CpDib.StockMst")
codeList = instCpCodeMgr.GetStockListByMarket(1)

kospi = {}
for code in codeList:
    name = instCpCodeMgr.CodeToName(code)
    kospi[code] = {name}

    priceunit = instCpStock.GetPriceUnit(code)
    kospi[code].append(code)

f = open('c:\\Users\\user\\Desktop\\바울\\kospi.csv', 'w')
for key, value in kospi.items():
    f.write("%s,%s\n" % (key, value))
f.close()

ko = pandas.read_csv(f)
print(ko)
