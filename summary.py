import sys
from datetime import datetime
from datetime import date
from gui.profile import Profile


print("************ ooohmystock ************ ")

p = Profile()
s = p.get_summary(sys.argv[1])
print('TICKER : %s' %s['TICKER'])
print('SECTOR : %s' %s['SECTOR'])
print('INDUSTRY : %s' %s['INDUSTRY'])
print('FISCAL_YEAR_END : %s' %s['FISCAL_YEAR_END'])
print('LATEST_QUARTER : %s' %s['LATEST_QUARTER'])
print('DIVIDEND_PERSHARE : %s' %s['DIVIDEND_PERSHARE'])
print('PROFIT_MARGIN : %s' %s['PROFIT_MARGIN'])
print('OPERATING_MARGIN_TTM : %s' %s['OPERATING_MARGIN_TTM'])
print('ANALYST_TARGETPRICE : %s' %s['ANALYST_TARGETPRICE'])
print('RETURN_ON_ASSETS_TTM : %s' %s['RETURN_ON_ASSETS_TTM'])
print('RETURN_ON_EQUITY_TTM : %s' %s['RETURN_ON_EQUITY_TTM'])
# print(p.get_ma_support(sys.argv[1], '2022-01-10', '2022-02-06', 5))
# print(p.get_gap('M',27.2,'2023-02-01',date.today()))
# print(p.forcast_next_price('NVDA', '2023-01-10', '2023-02-17', 5))
# print(p.get_key_finance('M'))


print("************ End ************ \n\n")