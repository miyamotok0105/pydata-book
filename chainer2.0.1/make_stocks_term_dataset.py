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
import numpy as np
import argparse

import pandas as pd

class stocks_datasest(object):
	def __init__(self):
		print("init")

	def get_stocks(self):
		#784次元
		pic_dim = 784

		pd_stocks_term = pd.read_csv('stocks_datasest.csv', delimiter=',')
		print(len(pd_stocks_term))

		x_train_stocks_term = []
		y_train_stocks_term = []

		for pd_stocks_term_ix in range(0, len(pd_stocks_term)-1000):
			# print(pd_stocks_term_ix)
			# print(pd_stocks_term.iloc[pd_stocks_term_ix:pd_stocks_term_ix+pic_dim,1].values)

			last_value = pd_stocks_term.iloc[pd_stocks_term_ix+pic_dim,1]
			next_value = pd_stocks_term.iloc[pd_stocks_term_ix+pic_dim+1,1]
			# print("last value:", last_value)
			# print("next value:", next_value)
			if last_value < next_value:
				# print("up")
				y_train_stocks_term.append(1)
			else:
				# print("down")
				y_train_stocks_term.append(0)

			# print(pd_stocks_term.iloc[pd_stocks_term_ix:pd_stocks_term_ix+pic_dim,1].values.reshape(784,1).shape)
			x_train_stocks_term.append(pd_stocks_term.iloc[pd_stocks_term_ix:pd_stocks_term_ix+pic_dim,1].values)

			#ちょっと回りくどい
			# query_str = " %s < index & index < %s "%(pd_stocks_term_ix, pd_stocks_term_ix+pic_dim+1)
			# print(pd_stocks_term.iloc[1:10,:])
			# print(pd_stocks_term.query(query_str).values)
			# print(pd_stocks_term.query(query_str).values.shape)

			# break
		return np.asarray(x_train_stocks_term, dtype=np.float32), np.asarray(y_train_stocks_term, dtype=np.int32)


