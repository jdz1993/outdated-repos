# -*- coding:utf-8 -*-

from const.const import LogConst

allow_tag_names = {
	LogConst.ACCOUNT_LOG_NAME:1,
	LogConst.MONTHLY_LOG_NAME:1,
	LogConst.LOAN_LOG_NAME :1,
	LogConst.MAIN_LOG_NAME :1,
	LogConst.YEAR_END_LOG_NAME :1,
	LogConst.YEAR_END_INCOME :1,
	LogConst.MONTHLY_INCOME :1,
	LogConst.HOUSE_LOAN_DETAIL :1,
	LogConst.MONTHLY_INVEST:1,
	LogConst.FLUCTUATION_RATE :1,
	LogConst.EXPECTATION_LOG_NAME :1,
}

class Logger(object):

	@classmethod
	def log(cls, msg,tag_name = 'log',has_tail = False):
		if tag_name in allow_tag_names:
			if allow_tag_names[tag_name]:
				msg = '<{}> {}'.format(tag_name,msg)
			else:
				msg = msg

			if has_tail:
				print msg,
			else:
				print msg

	@classmethod
	def tail_log(cls, msg,tag_name = 'log'):
		if tag_name in allow_tag_names:
			if allow_tag_names[tag_name]:
				msg = '<{}> {}'.format(tag_name,msg)
			else:
				msg = msg
			print msg,