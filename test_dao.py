from datetime import datetime
from datetime import date
from dao.alphavantage.json_to_sqlite import Converter
from dao.alphavantage.downloader import Downloader
from gui.profile import Profile

#tested
# d = Downloader()
# d.download('cm','OVERVIEW')
# d.download('nvda','BALANCE_SHEET')
# d.download('nvda','INCOME_STATEMENT')
# d.download('nvda','CASH_FLOW')
# d.download('nvda','EARNINGS')
# d.download('nvda','TIME_SERIES_DAILY_ADJUSTED')

#tested
# c = Converter('dvn')
# c.write_balance()
# c.write_income()
# c.write_cashflow()
# c.write_profile()
# c.write_eps()
# c.write_daily_price()

#tested
# p = Profile()
# print(p.get_ma_support('M', '2023-01-10', '2023-02-06', 5))
# print(p.get_gap('M',27.2,'2023-02-01',date.today()))
# print(p.forcast_next_price('NVDA', '2023-01-10', '2023-02-17', 5))
# print(p.get_key_finance('M'))


