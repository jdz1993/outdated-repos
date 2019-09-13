# -*- coding:utf-8 -*-

from config.init_config import InitConfig
from config.value_config import VauleConfig
from const.const import Const, LogConst
from data_class.loan_setting import LoanSetting
from debt_outcome import DebtOutcome
from log.logger import Logger
from naive_outcome import NaiveOutcome
from rent_house_outcome import RentHouseOutcome


class OutcomeManager(object):
    def __init__(self):
        self.outcomes = []
        self.debt = 0
        self.init()

    def init(self):
        self.outcomes.append(NaiveOutcome())
        if InitConfig.decide_to_buy_house:
            self._buy_house()
        else:
            self._rent_house()

    def _rent_house(self):
        self.outcomes.append(RentHouseOutcome())

    def _buy_house(self):
        total_loan = 130 * 10000
        gjj_loan = 50 * 10000
        sd_loan = total_loan - gjj_loan
        gjj_loan_setting = LoanSetting(loan_money=gjj_loan,
                                       years=20,
                                       year_percent=VauleConfig.gjj_percent,
                                       discount=1,
                                       tag_name=Const.GJJ_TAG_NAME)
        self.outcomes.append(DebtOutcome(gjj_loan_setting))
        sd_loan_setting = LoanSetting(loan_money=sd_loan,
                                      years=20,
                                      year_percent=VauleConfig.sd_percent,
                                      discount=0.95,
                                      tag_name=Const.SD_TAG_NAME)
        self.outcomes.append(DebtOutcome(sd_loan_setting))
        self.house_loan_details(gjj_loan, sd_loan)

    def calc_outcome_month(self):
        return sum([outcome.outcome_month() + outcome.outcome_month_mood() for outcome in self.outcomes])

    def calc_outcome_year_end(self):
        return sum([outcome.outcome_year_end() for outcome in self.outcomes])

    def calc_outcome_month_by_predicate(self, predicate):
        res = 0
        for outcome in self.outcomes:
            if predicate(outcome):
                res += outcome.outcome_month()
        return res

    def calc_outcome_month_debt_gjj(self):
        def predicate(x):
            return type(x) is DebtOutcome and x.load_setting.tag_name == Const.GJJ_TAG_NAME

        return self.calc_outcome_month_by_predicate(lambda x: predicate(x))

    def calc_outcome_month_debt_except_gjj(self):
        return self.calc_outcome_month() - self.calc_outcome_month_debt_gjj()

    def house_loan_details(self, gjj_loan, sd_loan):
        loan_money = gjj_loan + sd_loan
        house_money = loan_money / 0.65
        msg = "公积金贷款：{} 商贷：{}" \
              "\n对应首付:{:.2f}(贷款65% 首付%35)" \
              "\n其他金额{} (约3.5%)" \
              "\n房子价格: {}" \
              "\n首付交易价格: {}" \
              "\n https://www.zhihu.com/question/24534079" \
              "".format(gjj_loan, sd_loan,
                        house_money * 0.35,
                        house_money * 0.035,
                        house_money,
                        house_money * (0.35 + 0.035))
        Logger.log(msg, tag_name=LogConst.HOUSE_LOAN_DETAIL)
