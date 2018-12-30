from alpha_vantage.timeseries import TimeSeries

class ApiService:
    key = 'YRWRPB235341U6EM'
    symbol=''

    symbol_search = "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=ad&apikey=YRWRPB235341U6EM"
    def getKey(self):
        return self.key

    def symbolSearch(self, symbol, key):
        if symbol or symbol == ""  and key or key =="":
            url = "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=" + symbol + "&apikey=" + key
            return url
        else:
            print ("symbol atau key ada masalah")
            return print("bermasalah")