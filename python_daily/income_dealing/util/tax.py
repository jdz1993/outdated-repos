# -*- coding:utf-8 -*-
from log.logger import Logger
from const.const import LogConst

def year_end_tax(salary):
	taxRates = {36000: 0.03, 144000: 0.1, 300000: 0.2, 420000: 0.25, 660000: 0.3, 960000: 0.35, 99999999999: 0.45}
	START = 0 * 12

	temp = salary - START
	idvTax = 0
	preBar = 0
	for bar, rate in taxRates.items():
		if temp <= 0:
			break
		if temp - (bar - preBar) <= 0:
			idvTax += rate * temp
			break
		else:
			idvTax += rate * (bar - preBar)
		temp -= bar - preBar
		preBar = bar

	msg = "税前年收入: {} 年纳税额: {} 税后年收入: {}".format(salary, idvTax, salary - idvTax)
	Logger.log(msg, tag_name=LogConst.YEAR_END_INCOME)

	return salary - idvTax

def table(Taxable_Income):
	if 3000 >= Taxable_Income:
		return 0, 0
	elif 12000 >= Taxable_Income > 3000:
		return 0.1, 210
	elif 25000 >= Taxable_Income > 12000:
		return 0.2, 1410
	elif 35000 >= Taxable_Income > 25000:
		return 0.25, 2660
	elif 55000 >= Taxable_Income > 35000:
		return 0.3, 4410
	elif 80000 >= Taxable_Income > 55000:
		return 0.35, 7160
	elif Taxable_Income > 80000:
		return 0.45, 15160

def after_tax(money):
	if money <= 0:  # 工资负数直接不计算
		return
	Taxable_Income = money - 5000   # 应纳税额
	if Taxable_Income <= 0:  # 如果应纳税所得额为负则不需要纳税.应纳税所得额=0
		Taxable_Income = 0.00
	tax_rate, take_out = table(Taxable_Income)  # 计算税率和速扣
	Tax_payable = Taxable_Income * tax_rate - take_out
	finally_money = money - Tax_payable
	return finally_money

def after_insurance(salary,gongjijin_rate = 0.07):
	'''
	养老保险：8%
	医疗保险：2%
	失业保险：0.5%
	工伤保险：0%
	生育保险：0%
	公积金：7% or 12%
	'''
	all_rate = 0.105 + gongjijin_rate
	return salary * (1 - all_rate)

def do_tax(salary,gongjijin_rate = 0.07):
	res_insuranced = after_insurance(salary,gongjijin_rate=gongjijin_rate)
	res = after_tax(res_insuranced)
	msg = 'salary {} after_insurance {} after tax {}'.format(salary,res_insuranced,res)
	Logger.log(msg, tag_name=LogConst.MONTHLY_INCOME)
	return res

def get_company_gongjijin(salary,gongjijin_rate = 0.07):
	return salary * gongjijin_rate