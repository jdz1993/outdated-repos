# -*- coding:utf-8 -*-

from multi_platforms.worker import PlatformWorker, OriginWorker


def process():
	l = ['windows', 'android', 'ios']
	for platform in l:
		worker = PlatformWorker(platform)
		worker.do_something()


def process_origin():
	l = ['windows', 'android', 'ios']
	for platform in l:
		worker = OriginWorker(platform)
		worker.do_something()


def main():
	process()
	print
	# process_origin()


if __name__ == '__main__':
	main()
