from services.api import ApiService as api
from alpha_vantage.timeseries import TimeSeries

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

# ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
# data, meta_data = ts.get_intraday(symbol='ADHI.JKT',interval='5min', outputsize='full')
# data['4. close'].plot()
# plt.title('Intraday Times Series for the MSFT stock (1 min)')
# plt.show()


# from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
# data, meta_data = ts.get_daily(symbol='ADHI.JKT', outputsize='full')
# pprint(data)
# print(meta_data)


print('Masukkan kode saham: ')
simbol=input()
print('kode saham: ' +simbol)

data, metadata = ts.get_batch_stock_quotes(simbol)
# data, meta_data = ts.get_daily(symbol=simbol+'.JKT', outputsize='full')
# pprint(data)
# print(meta_data)
# pprint(meta_data)
# result = []
# for line in open(data):
#     fields = line.split(",")
#     name = fields[0]
#     shares = int(fields[1])
#     prices = float(fields[2])
#     stock = (name,shares, prices)
#     result.append(stock)
pprint(data)
pprint(metadata)
# print(result)
# print (functionKey)
print( metadata)

# class Testing:
#     def test(self):
#         print('ok')
#
#
#
#     def getData(self):
#         ts = TimeSeries(key=api.getKey(self))
#         data, meta_data = ts.get_daily('MFST',outputsize='full')
#         print(data)
#         print(meta_data)
#
# if __name__ == '__main__':
#     tes = Testing()
#     tes.test()
#     data = tes.getData()