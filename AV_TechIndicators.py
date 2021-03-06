from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt
from Environment_Settings import settings

class AlphaVantageAPI() :
    
    def __init__(self, symbol):
        self.symbol = symbol

    def techIndicator_get_bbands(self, timePeriod, format):
        #outputting data in JSON format in the below line
        ti = TechIndicators(key= settings.API_KEY, output_format=format)
        data, meta_data = ti.get_bbands(symbol=self.symbol, interval='daily', time_period=timePeriod)
        return data, meta_data
    
    def techIndicator_get_RSI(self, timePeriod, format):
        ti = TechIndicators(key= settings.API_KEY, output_format=format)
        data, meta_data = ti.get_rsi(symbol=self.symbol, interval='daily', time_period=timePeriod)
        return data, meta_data

    def techIndicator_get_MACD(self, format, macd_interval, series):
        ti = TechIndicators(key= settings.API_KEY, output_format=format)
        data, meta_data = ti.get_macd(symbol=self.symbol, interval=macd_interval, series_type=series)
        return data, meta_data

    def techIndicator_get_VWAP(self, timePeriod,format):
        ti = TechIndicators(key= settings.API_KEY, output_format=format)
        data, meta_data = ti.get_vwap(symbol=self.symbol, interval=timePeriod)
        return data, meta_data

    def techIndicator_get_OBV(self, timePeriod, format):
        ti = TechIndicators(key= settings.API_KEY, output_format=format)
        data, meta_data = ti.get_obv(symbol=self.symbol, interval=timePeriod)
        return data, meta_data    