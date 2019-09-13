# -*- coding:utf-8 -*-

from config.init_config import InitConfig

class NaiveOutcome(object):
	def __init__(self):
		pass

	def outcome_month(self):
		return InitConfig.naive_outcome_month

	def outcome_year_end(self):
		return InitConfig.naive_outcome_year_end

	def outcome_month_mood(self):
		return InitConfig.naive_mood_cost_month