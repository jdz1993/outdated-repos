# -*- coding:utf-8 -*-

from const.const import Const,LogConst
from fluctuation_invest import FluctuationInvest
from naive_invest import NaiveInvest
from log.logger import Logger

class InvestManager(object):
	def __init__(self):
		self.invests = {
			Const.NAIVE_INVEST:NaiveInvest(),
			Const.FLUCTUATION_INVEST:FluctuationInvest(),
		}
		self.percents = {
			Const.NAIVE_INVEST:1,
			Const.FLUCTUATION_INVEST:0,
		}
		self.names = {
			Const.NAIVE_INVEST:'NAIVE_INVEST',
			Const.FLUCTUATION_INVEST:'FLUCTUATION_INVEST',
		}
		self.money_throwed = 0
		self.init()

	def init(self):
		pass

	def throw_money(self,cost):
		self.money_throwed += cost

	def check_curr_throwed_money(self):
		return self.money_throwed

	def take_out_money(self,takeout_cost):
		if self.money_throwed > takeout_cost:
			self.money_throwed -= takeout_cost
			return takeout_cost
		return 0

	def take_out_all(self):
		res = self.money_throwed
		self.money_throwed = 0
		return res

	def invest_process_month(self):
		res = 0
		for i,invest in self.invests.iteritems():
			percent = self.percents[i]
			if percent == 0:
				continue
			money = self.money_throwed * percent
			invest_money = invest.get_invest_month(money)
			msg = '{} invest_process_month {}'.format(self.names[i],invest_money)
			Logger.log(msg, tag_name=LogConst.MONTHLY_INVEST)
			res += invest_money
		self.money_throwed = res