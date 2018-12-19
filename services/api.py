from alpha_vantage.timeseries import TimeSeries
key = 'YRWRPB235341U6EM'
timeseries = TimeSeries(key)
timeseries_plotting = TimeSeries(key,output_format='pandas')