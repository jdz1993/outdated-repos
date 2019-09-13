# -*- coding:utf-8 -*-

from util.tax import do_tax,year_end_tax
import copy

class SalarySetting(object):
	def __init__(self,month,gongjijin_rate,twelfth,year_end,tag_name = 'default'):
		self.month = month
		self.gongjijin_rate = gongjijin_rate
		self.twelfth = twelfth
		self.year_end = year_end
		self.tag_name = tag_name