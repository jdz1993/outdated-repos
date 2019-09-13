# -*- coding:utf-8 -*-

import time
from random import randint


# 生成有n个元素的随机数组,左闭右闭
def generate_random_array(n, rangeL, rangeR):
	assert rangeL <= rangeR
	return [randint(rangeL, rangeR) for i in xrange(n)]


# 生成n个几乎有序的数组
def generate_nearly_ordered_array(n, swap_times):
	order_arr = [x for x in xrange(n)]
	for i in xrange(swap_times):
		x = randint(0, n - 1)
		y = randint(0, n - 1)
		order_arr[x], order_arr[y] = order_arr[y], order_arr[x]
	return order_arr


# 测试
def test_sort(sort_name, sort_func, arr):
	n = len(arr)
	start_t = time.time()
	sort_func(arr)
	end_t = time.time()
	if not is_sorted(arr):
		print arr
		assert False
	print sort_name, ':', end_t - start_t, 'seconds'


def is_sorted(arr):
	for i in xrange(len(arr) - 1):
		if arr[i] > arr[i + 1]:
			return False
	return True
