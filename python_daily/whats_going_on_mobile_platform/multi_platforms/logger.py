# -*- coding:utf-8 -*-
import os
import time


class Logger(object):
	'''模拟print等正常log的行为，无法修改'''

	@classmethod
	def log(cls, platform, msg):
		if platform == 'windows':
			print msg


class PlatformLogger(object):
	@classmethod
	def log(cls, msg, logfile='log.md'):
		time_str = str(time.time())
		line = '[%s]%s\n' % (time_str, msg)
		print line
		log_name = os.path.join(os.getcwd(), logfile)
		with open(log_name, "a") as fd:
			fd.write(line)
