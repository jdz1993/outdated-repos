# -*- coding:utf-8 -*-

from config.init_config import InitConfig

class RentHouseOutcome(object):
	def __init__(self):
		pass

	def outcome_month(self):
		return InitConfig.rent_house_month

	def outcome_year_end(self):
		return 0

	def outcome_month_mood(self):
		return 0