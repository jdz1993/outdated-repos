# -*- coding:utf-8 -*-

PC = 'windows'
ANDROID = 'android'
IOS = 'ios'

Platform = PC
from logger import Logger


class Unexpected(object):
	"""在多平台依赖于底层接口工作时，面对的很可能就是如此逗比的实现"""

	@classmethod
	def do_unexpect(cls, platform):
		if platform == 'windows':
			Logger.log(platform, 1 / 2.0)
			return 'windows is ok'
		elif platform == 'android':
			Logger.log(platform, 1 / 0)
			return 'android is error'
		elif platform == 'ios':
			Logger.log(platform, 1 / 2)
			return 'ios is wrong'
