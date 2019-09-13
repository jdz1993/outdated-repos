# -*- coding:utf-8 -*-

from functools import wraps

def show_log(tag = 'log'):
	def decorator(func):
		@wraps(func)
		def wrapper(*args,**kwargs):
			tag_name = '<%s>'%tag
			print '{} {} before running [args]{} [kwargs]{}'.format(tag_name,func.__name__,args,kwargs)
			res = func(*args,**kwargs)
			print '%s %s finish [result] %s '%(tag_name,func.__name__,res)
			return res
		return wrapper
	return decorator