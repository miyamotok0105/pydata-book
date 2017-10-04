# -*- coding: utf-8 -*-
#!/usr/bin/env python

from __future__ import print_function

try:
    import matplotlib
    matplotlib.use('Agg')
except ImportError:
    pass

import os
import glob
import argparse

import pandas as pd
_pd_dates = pd.date_range('2007-01-13',periods=3900,freq='D')
print(type(_pd_dates))
dates = [str(_pd_date)[:10] for _pd_date in _pd_dates]
print(type(dates[0]))
print((dates[0]))

stocks_file_path = "/Users/user/Downloads/stocksFile/"
stocks_files = [x for x in os.listdir(stocks_file_path) if x.endswith(".csv")]
stocks_dates = [stocks_file[7:17] for stocks_file in stocks_files]
# print(type(stocks_dates[0]))
# print((stocks_dates[0]))

stocks_datasest = []
for stocks_file in stocks_files:

	df = pd.read_csv(os.path.join(stocks_file_path, stocks_file), encoding="shift-jis")
	# print(df.head())
	# print(df.query('コード == "1308-T"'))
	# print(df.query('コード == "1308-T"')["終値"].values[0])
	stocks_datasest.append(df.query('コード == "1308-T"')["終値"].values[0])
	# break

print(stocks_datasest)
pd_stocks_datasest = pd.DataFrame.from_dict(stocks_datasest)
pd_stocks_datasest.to_csv('stocks_datasest.csv')
