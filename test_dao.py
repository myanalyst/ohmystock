from datetime import datetime
from datetime import date
from dao.alphavantage.json_to_sqlite import Converter
from dao.alphavantage.downloader import Downloader
from gui.profile import Profile

#tested
# d = Downloader()
# d.download('cvs','OVERVIEW')
# d.download('cvs','BALANCE_SHEET')
# d.download('cvs','INCOME_STATEMENT')
# d.download('cvs','CASH_FLOW')
# d.download('cvs','EARNINGS')
# d.download('cvs','TIME_SERIES_DAILY_ADJUSTED')

#tested
# c = Converter('cvs')
# c.write_balance()
# c.write_income()
# c.write_cashflow()
# c.write_profile()
# c.write_eps()

#tested
p = Profile()
# print(p.get_ma_support('M', '2023-01-10', '2023-02-06', 5))
# print(p.get_gap('M',27.2,'2023-02-01',date.today()))
print(p.get_momentum_price('M', '2023-01-10', '2023-02-06', 5, 'ma5'))
# print(p.get_key_finance('M'))


