# -*- coding:utf-8 -*-

from config.init_config import InitConfig
from util.loan import Loan
from config.value_config import VauleConfig
from const.const import Const

class DebtOutcome(object):
	'''等额本息贷款'''
	def __init__(self,loan_setting):
		self.load_setting = loan_setting
		self.loan = Loan(loan_setting)
		self.loan.print_details()

	def outcome_month(self):
		return self.loan.repay_per_month()

	def outcome_year_end(self):
		return 0

	def outcome_month_mood(self):
		return 0