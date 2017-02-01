from win32com import client

instStockChart = client.Dispatch("CpSysDib.StockChart")

# with open('c:\\Users\\user\\PycharmProjects\\kospi.csv', 'r') as f:




instStockChart.SetInputValue(0, 'A000030')
instStockChart.SetInputValue(1, ord('2'))       # 아스키코드값으로 보내줘야함
instStockChart.SetInputValue(4, 100)
instStockChart.SetInputValue(5, 2)
instStockChart.SetInputValue(5, 5)
instStockChart.SetInputValue(6, ord('D'))
instStockChart.SetInputValue(9, ord('0'))

# 요청 보내는 부분
instStockChart.BlockRequest()


# 응답 받는 부분
numData = instStockChart.GetHeaderValue(3)

for i in range(numData):
    print(i, instStockChart.GetDataValue(0, i))
