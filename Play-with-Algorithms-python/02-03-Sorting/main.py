# -*- coding:utf-8 -*-

import copy
from functools import partial

import sort_functions
import sort_test_helper


def test_array(arr):
	sort_test_helper.test_sort('selection_sort', sort_functions.selection_sort, copy.deepcopy(arr))
	sort_test_helper.test_sort('insertion_sort_naive', sort_functions.insertion_sort_naive, copy.deepcopy(arr))
	sort_test_helper.test_sort('insertion_sort', sort_functions.insertion_sort, copy.deepcopy(arr))
	for i in xrange(2, 8):
		print 'step:', i,
		sort_test_helper.test_sort('shell_sort', partial(sort_functions.shell_sort, i), copy.deepcopy(arr))
	sort_test_helper.test_sort('merge_sort', sort_functions.merge_sort, copy.deepcopy(arr))
	sort_test_helper.test_sort('merge_sort_bottom_up', sort_functions.merge_sort_bottom_up, copy.deepcopy(arr))
	sort_test_helper.test_sort('quick_sort', sort_functions.quick_sort, copy.deepcopy(arr))


def do_test():
	n = 10000

	print '\n=========== random array test ==========='
	arr = sort_test_helper.generate_random_array(n, 0, n)
	test_array(arr)

	print '\n=========== nearly ordered array test ==========='
	arr = sort_test_helper.generate_nearly_ordered_array(n, 100)
	test_array(arr)


def main():
	do_test()


if __name__ == '__main__':
	main()
