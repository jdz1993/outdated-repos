# -*- coding:utf-8 -*-

from income.income_manager import IncomeManager
from config.init_config import InitConfig
from invest.invest_manager import InvestManager
from outcome.outcome_manager import OutcomeManager
from const.const import Const,LogConst
from log.logger import Logger

class Expectation(object):
	def __init__(self):
		self.current = InitConfig.current_benji
		self.income_manager = IncomeManager()
		self.invest_manager = InvestManager()
		self.outcome_manager = OutcomeManager()

	def process_all(self):
		for i in xrange(1):
			self.process_single_year()

	def all_assets_value(self):
		return self.current + self.invest_manager.check_curr_throwed_money()

	def process_single_year(self):
		for i in xrange(12):
			self.process_month()
		self.process_year_end()

	def process_month(self):
		income = self.income_manager.calc_income_month()
		outcome = self.outcome_manager.calc_outcome_month()
		invest = income - outcome
		msg = '[income]{} [outcome]{} [invest]{}'.format(income,outcome,invest)
		Logger.log(msg, tag_name=LogConst.EXPECTATION_LOG_NAME)
		self.invest_manager.invest_process_month()
		self.invest_manager.throw_money(invest)
		self.print_account()

	def process_year_end(self):
		income = self.income_manager.calc_income_year_end()
		outcome = self.outcome_manager.calc_outcome_year_end()
		invest = income - outcome
		msg = '[income]{} [outcome]{} [invest]{}'.format(income, outcome, invest)
		Logger.log(msg, tag_name=LogConst.EXPECTATION_LOG_NAME)
		self.invest_manager.throw_money(income)
		self.print_account()

	def print_account(self):
		cash = self.current
		invest_account = self.invest_manager.check_curr_throwed_money()
		msg = '[cash]{} [investing_account]{}'.format(cash,invest_account)
		Logger.log(msg, tag_name=LogConst.EXPECTATION_LOG_NAME)