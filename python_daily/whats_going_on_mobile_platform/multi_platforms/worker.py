# -*- coding:utf-8 -*-


import functools

from logger import Logger, PlatformLogger
from unexpected import Unexpected


class OriginWorker(object):
	def __init__(self, platform):
		self.platform = platform
		self.logging = functools.partial(Logger.log, self.platform)

	def do_something(self):
		self.something_went_wrong()

	def something_went_wrong(self):
		Unexpected.do_unexpect(self.platform)


def platform_logging_decorator(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		PlatformLogger.log('[before_run]{}'.format(func.__name__))
		res = None
		try:
			res = func(*args, **kwargs)
		except Exception as e:
			PlatformLogger.log('[error_occur]{} [error]{}'.format(func.__name__, e))
		PlatformLogger.log('[finish_run]{} [result]{}'.format(func.__name__, res))
		return res

	return wrapper


class PlatformWorker(OriginWorker):
	"""每次在移动平台上测试时间成本很高，一定要尽可能详细的记录信息"""

	def something_went_wrong(self):
		self.do_unexpect()

	@platform_logging_decorator
	def do_unexpect(self):
		return Unexpected.do_unexpect(self.platform)
