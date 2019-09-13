# -*- coding:utf-8 -*-

import random

from config.value_config import VauleConfig
from const.const import LogConst
from log.logger import Logger


class FluctuationInvest(object):
	def __init__(self):
		pass

	def get_invest_month(self,cost):
		bottom = VauleConfig.fluctuation_bottom
		top = VauleConfig.fluctuation_top
		rate = random.uniform(bottom,top)
		msg = '[fluctuation_rate]{}'.format(rate)
		Logger.log(msg, tag_name=LogConst.FLUCTUATION_RATE)
		return cost * (1+rate)