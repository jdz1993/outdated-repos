# -*- coding:utf-8 -*-

from config.value_config import VauleConfig

class NaiveInvest(object):
	def __init__(self):
		pass

	def get_invest_month(self,cost):
		return cost * (1+VauleConfig.huoqi_rate_year / 12)