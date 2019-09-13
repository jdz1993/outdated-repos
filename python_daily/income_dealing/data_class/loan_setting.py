# -*- coding:utf-8 -*-

# 1、购买新建房屋的公积金贷款年限最长不超过30年。
# 2、购买二手房分为三种情况：
# （1）二手房房龄等于低于5年，公积金贷款年限最长不超过30年；
# （2）二手房房龄在6-19年之间，公积金贷款年限不超过35年与房龄之差；
# （3）二手房房龄等于大于20年，公积金贷款最长期限不超过15年。

class LoanSetting2(object):
    def __init__(self, gjj_loan, gjj_years, gjj_percent, sd_loan, sd_years, sd_percent, sd_discount):
        # 公积金贷配置
        self.gjj_loan = gjj_loan
        self.gjj_years = gjj_years
        self.gjj_percent = gjj_percent
        # 商贷配置
        self.sd_loan = sd_loan
        self.sd_years = sd_years
        self.sd_percent = sd_percent
        self.sd_discount = sd_discount



class LoanSetting(object):
    def __init__(self, loan_money, years, year_percent, tag_name = 'default_loan', discount = 1):
        self.loan_money = loan_money
        self.years = years
        self.year_percent = year_percent
        self.discount = discount
        self.tag_name = tag_name