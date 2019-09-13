# -*- coding:utf-8 -*-

from util.tax import do_tax,year_end_tax,get_company_gongjijin
import copy

class SalaryIncome(object):
	def __init__(self,salary_setting):
		self.salary_setting = copy.deepcopy(salary_setting)

	def income_month(self):
		return do_tax(self.salary_setting.month,gongjijin_rate=self.salary_setting.gongjijin_rate)

	def income_twelfth(self):
		return do_tax(self.salary_setting.twelfth,gongjijin_rate=self.salary_setting.gongjijin_rate)

	def income_year_end(self):
		return year_end_tax(self.salary_setting.year_end)

	def income_gjj_month(self):
		"""个人+公司的公积金，按不主动提取计，只用作还loan"""
		return get_company_gongjijin(self.salary_setting.month,gongjijin_rate=self.salary_setting.gongjijin_rate) * 2