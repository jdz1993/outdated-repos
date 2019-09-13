# -*- coding:utf-8 -*-

from config.init_config import InitConfig
from const.const import LogConst
from decision import Decision
from log.logger import Logger
from manager.income.income_manager import IncomeManager
from manager.invest.invest_manager import InvestManager
from manager.outcome.outcome_manager import OutcomeManager


class Account(object):
    def __init__(self):
        self.current = InitConfig.current_benji
        self._gjj_account = InitConfig.current_gongjijin
        self.income_manager = IncomeManager()
        self.invest_manager = InvestManager()
        self.outcome_manager = OutcomeManager()
        self.invest_manager.throw_money(self.current)

    def process_all(self):
        # self.process_year_end(working_month=9)
        for i in xrange(5):
            self.process_single_year(i + 1)

        for i in xrange(0):
            self.process_month(2, i + 1)

    def all_assets_value(self):
        return self.current + self.invest_manager.check_curr_throwed_money()

    def process_single_year(self, year_index):
        for i in xrange(12):
            self.process_month(year_index, i + 1)
        self.process_year_end(working_month=12)

    def process_month(self, year_index, month_index):
        Logger.tail_log('第{}年'.format(year_index), tag_name=LogConst.MONTHLY_LOG_NAME)
        Logger.log('第{}月'.format(month_index), tag_name=LogConst.MONTHLY_LOG_NAME)
        income = self.income_manager.calc_income_month()
        gongjijin = self.income_manager.calc_income_ggj()
        gjj_debt = self.outcome_manager.calc_outcome_month_debt_gjj()
        other_outcome = self.outcome_manager.calc_outcome_month_debt_except_gjj()
        gjj_tiqu = 0

        if gjj_debt > gongjijin:
            invest = income + gongjijin - gjj_debt - other_outcome
        else:
            invest = income - other_outcome
            self._gjj_account += gongjijin - gjj_debt

        if month_index % 3 == 0 and not Decision.decide_to_buy_house():
            gjj_tiqu_max = 6000 * 2
            gjj_tiqu = gjj_tiqu_max if self._gjj_account > gjj_tiqu_max else self._gjj_account
            self._gjj_account -= gjj_tiqu
            invest += gjj_tiqu

        msg = '[income]{} [gongjijin]{} [gjj_debt]{} [other_outcome]{} [gjj_tiqu]{} [invest]{}' \
              ''.format(income, gongjijin, gjj_debt, other_outcome, gjj_tiqu, invest)
        Logger.log(msg, tag_name=LogConst.MONTHLY_LOG_NAME)

        self.invest_manager.invest_process_month()
        self.invest_manager.throw_money(invest)
        self.print_account()

    def process_year_end(self, working_month):
        income = self.income_manager.calc_income_year_end() * working_month / 12.0
        outcome = self.outcome_manager.calc_outcome_year_end()
        invest = income - outcome

        msg = '[income]{} [outcome]{} [invest]{}'.format(income, outcome, invest)
        Logger.log(msg, tag_name=LogConst.YEAR_END_LOG_NAME)

        self.invest_manager.throw_money(income)
        self.print_account()

    def print_account(self):
        msg = '[cash_account]{} [investing_account]{} [gongjijin_account]{}' \
              ''.format(self.cash_account, self.invest_account, self.gjj_account)
        Logger.log(msg, tag_name=LogConst.ACCOUNT_LOG_NAME)

    @property
    def cash_account(self):
        return self.current

    @property
    def invest_account(self):
        return self.invest_manager.check_curr_throwed_money()

    @property
    def gjj_account(self):
        return self._gjj_account
