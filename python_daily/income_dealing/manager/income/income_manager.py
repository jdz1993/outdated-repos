# -*- coding:utf-8 -*-

from salary_income import SalaryIncome
from data_class.salary_setting import SalarySetting
from util.decorator import show_log
from config.init_config import InitConfig

class IncomeManager(object):
	def __init__(self):
		self.incomes = []
		self.init()

	def init(self):
		people_salary = InitConfig.people_salary
		for i in people_salary:
			ss = SalarySetting(*i)
			salary_income = SalaryIncome(ss)
			self.incomes.append(salary_income)

	#@show_log()
	def calc_income_month(self):
		return sum([income.income_month() for income in self.incomes])

	#@show_log()
	def calc_income_year_end(self):
		return sum([income.income_year_end() for income in self.incomes])

	def calc_income_ggj(self):
		return sum([income.income_gjj_month() for income in self.incomes])