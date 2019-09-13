# -*- coding:utf-8 -*-

from manager.income.income_manager import IncomeManager
from config.init_config import InitConfig
from manager.invest.invest_manager import InvestManager
from manager.outcome.outcome_manager import OutcomeManager


class Decision(object):
	def __init__(self):
		pass

	@classmethod
	def decide_to_buy_house(cls):
		return InitConfig.decide_to_buy_house