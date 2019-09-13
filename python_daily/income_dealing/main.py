# -*- coding:utf-8 -*-

from account import Account
from log.logger import Logger
from const.const import Const

def process_income():
	income_processor = Account()
	income_processor.process_all()

def process_expectation():
	sum = 0
	iter_times = 10000
	for i in xrange(iter_times):
		income_processor = Account()
		income_processor.process_all()
		one = income_processor.all_assets_value()
		msg = '{} : {}'.format(i,one)
		Logger.log(msg, tag_name=Const.MAIN_LOG_NAME)
		sum += one

	avg = sum / iter_times
	msg = 'avg: {}'.format(avg)
	Logger.log(msg, tag_name=Const.MAIN_LOG_NAME)


def main():
	process_income()

if __name__ == '__main__':
	main()