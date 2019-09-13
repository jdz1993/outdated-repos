# -*- coding:utf-8 -*-

# 1、购买新建房屋的公积金贷款年限最长不超过30年。
# 2、购买二手房分为三种情况：
# （1）二手房房龄等于低于5年，公积金贷款年限最长不超过30年；
# （2）二手房房龄在6-19年之间，公积金贷款年限不超过35年与房龄之差；
# （3）二手房房龄等于大于20年，公积金贷款最长期限不超过15年。

from const.const import LogConst
from log.logger import Logger


class Loan(object):
	def __init__(self, loan_setting):
		self.loan_money = loan_setting.loan_money
		self.years = loan_setting.years
		self.year_percent = loan_setting.year_percent
		self.discount = loan_setting.discount
		self.tag_name = loan_setting.tag_name

	def repay_per_month(self):
		"""
		每月还款
		:return: 每月还款
		"""
		beta = self.year_percent * self.discount / 100 / 12
		m = self.years * 12
		repayment_per_month = self.loan_money * beta * (1 + beta) ** m / ((1 + beta) ** m - 1)
		return repayment_per_month

	def final_repayment(self):
		"""
		还款终值
		:return: 终值
		"""
		return self.repay_per_month() * 12 * self.years

	def print_details(self):
		msg = '{}: 总借{:.2f} 总还{:.2f} 每月还{:.2f} 年数{} 利率{} 折扣{}' \
			  ''.format(self.tag_name,
						self.loan_money,
						self.final_repayment(),
						self.repay_per_month(),
						self.years,
						self.year_percent,
						self.discount)
		Logger.log(msg, tag_name=LogConst.LOAN_LOG_NAME)