from datetime import datetime
from datetime import date
from dao.alphavantage.json_to_sqlite import Converter
from dao.alphavantage.downloader import Downloader
from gui.profile import Profile

#tested
# d = Downloader()
# d.download('nvda','OVERVIEW')
# d.download('nvda','BALANCE_SHEET')
# d.download('nvda','INCOME_STATEMENT')
# d.download('nvda','CASH_FLOW')
# d.download('nvda','EARNINGS')
# d.download('nvda','TIME_SERIES_DAILY_ADJUSTED')

#tested
# c = Converter('nvda')
# c.write_balance()
# c.write_income()
# c.write_cashflow()
# c.write_profile()
# c.write_eps()

#tested
# p = Profile()
# print(p.get_ma_support('M', '2023-01-10', '2023-02-06', 5))
# print(p.get_gap('M',27.2,'2023-02-01',date.today()))
# print(p.forcast_next_price('', '2023-01-10', '2023-02-06', 'ma5'))
# print(p.get_key_finance('M'))


