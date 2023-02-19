import sys
sys.path.insert(0,'/Users/ernestmoney/ohmystock')
import numpy as np

import pipe.price_momentum as prm
from dao.selector_overview import Overview_Selector

import unittest

class Test_Price_Momentum(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.s = Overview_Selector()

    def test_get_benchmark_prices(self):
        ticker = 'nvda'
        data = self.s.select_daily_price(ticker, '2022-02-01', '2023-02-17')

        ws = 0
        ms = 0
        ss = 0
        pws = 0
        pms = 0
        pss = 0
        h1r = 0
        h2r = 0
        h3r = 0

        i = 0
        for i in range(0,len(data)):
            if i >=4 and i <len(data)-1:
                print('\n')
                if data[i][5] < data[i+1][5] :
                    p = prm.forcast_next_price(data, ticker, data[i][1], True,  5)
                else:
                    p = prm.forcast_next_price(data, ticker, data[i][1], False, 5)
                eav = round((data[i+1][5] - data[i][5])/data[i][5] * 100,2)
                
                abs_eav = np.abs(eav)
                if abs_eav <2.8:
                    ws = ws + 1
                    if (p[0][1]-data[i+1][5]) <=1.5:
                        pws = pws + 1
                    
                if abs_eav <=3.8 and abs_eav>=2.8:
                    ms = ms + 1
                    if (p[1][1]-data[i+1][5]) <=1.5:
                        pms = pms + 1
                    
                if abs_eav >3.8:
                    ss = ss + 1
                    if (p[2][1]-data[i+1][5]) <=1.5:
                        pss = pss + 1
                    


                print('eav=%s, ws=%s, ms=%s, ss=%s' %(eav, ws, ms, ss))
                print('Tomorrow : %s   |    Price : %s   |    EAV : %g%%   |    Distance (weak=%g, medium=%g, strong=%g)' %(data[i+1][1], data[i+1][5], eav, p[0][1]-data[i+1][5], p[1][1]-data[i+1][5], p[2][1]-data[i+1][5]))
                # print('Tomorrow : %s   |    Price : %s   |    Distance (Hit1=%g, Hit2=%g, Hit3=%g)' %(data[i+1][1], data[i+1][5], p[0][1]-data[i+1][5], p[1][1]-data[i+1][5], p[2][1]-data[i+1][5]))
            i = i + 1

        h1r = (pws/ws) * 100
        h2r = (pms/ms) * 100
        h3r = (pss/ss) * 100
        print('\n\nTotal tests: %s   |    Hit1 Rate: %g%%   |    Hit2 Rate: %g%%   |    Hit3 Rate: %g%%' %(i-5, h1r, h2r, h3r))
if __name__ == '__main__':
    unittest.main()