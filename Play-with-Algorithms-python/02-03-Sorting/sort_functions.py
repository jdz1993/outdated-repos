# -*- coding:utf-8 -*-

def selection_sort(arr):
	"""选择排序：1-n遍历，遍历剩余元素最小值，并与第i位交换位置"""
	n = len(arr)
	for i in xrange(n):
		min_index = i  # 剩余元素包括当前的第i位
		for j in xrange(i + 1, n):
			if arr[j] < arr[min_index]:
				min_index = j
		arr[i], arr[min_index] = arr[min_index], arr[i]
	return arr


def insertion_sort_naive(arr):
	"""插入排序：1-n遍历，遍历之前所有元素，并将第i位元素放到1-i中的合适的位置上，这个过程是通过一次次swap实现(naive)"""
	n = len(arr)
	for i in xrange(n):
		for j in xrange(i, 0, -1):
			if arr[j] < arr[j - 1]:
				arr[j], arr[j - 1] = arr[j - 1], arr[j]
			else:
				break
	return arr


# 插排可能提前中止循环的特性，使得插排比选择排序更快 等同于insertion_sort_range(arr, 0, len(arr) - 1)
def insertion_sort(arr):
	"""插入排序：1-n遍历，遍历之前所有元素，并将第i位元素放到1-i中的合适的位置上，这个过程是通过先将大数放后面，最后一次放第i位，省一半的赋值操作"""
	n = len(arr)
	for i in xrange(n):
		current = arr[i]
		j = i
		while j > 0 and current < arr[j - 1]:
			arr[j] = arr[j - 1]
			j -= 1
		arr[j] = current
	return arr


def insertion_sort_range(arr, l, r):
	"""插入排序[l,r]"""
	for i in xrange(l, r + 1):
		current = arr[i]
		j = i
		while j > l and current < arr[j - 1]:
			arr[j] = arr[j - 1]
			j -= 1
		arr[j] = current
	return arr


# 希尔排序
def shell_sort(magic_step, arr):
	"""希尔排序：也就是不同步长的插入排序，使用 h = h * magic_step + 1 的步长进行排序"""
	n = len(arr)
	h = 1
	while h < n / magic_step:
		h = h * magic_step + 1

	while h >= 1:
		for i in xrange(n):
			current = arr[i]
			j = i
			while j - h >= 0 and current < arr[j - h]:
				arr[j] = arr[j - h]
				j -= h
			arr[j] = current
		h /= magic_step
	return arr


def __merge(arr, l, mid, r):
	"""对[l,mid],[mid+1,r]进行归并"""
	aux = [arr[i] for i in xrange(l, r + 1)]

	i, j = l, mid + 1
	for k in xrange(l, r + 1):
		# 首先确认数组索引的合法性，一定要先判断，并且注意四个条件是互斥的
		if i > mid:
			arr[k] = aux[j - l]
			j += 1
		elif j > r:
			arr[k] = aux[i - l]
			i += 1
		elif aux[i - l] < aux[j - l]:
			arr[k] = aux[i - l]
			i += 1
		else:
			arr[k] = aux[j - l]
			j += 1


def __merge_sort(arr, l, r):
	"""[l,r]归并排序"""
	# if l >= r:
	# 	return

	if r - l <= 15:  # 使用插入排序优化归并排序
		insertion_sort_range(arr, l, r)
		return

	mid = l + (r - l) / 2
	__merge_sort(arr, l, mid)
	__merge_sort(arr, mid + 1, r)
	if arr[mid] > arr[mid + 1]:  # 提前退出的可能
		__merge(arr, l, mid, r)


def merge_sort(arr):
	__merge_sort(arr, 0, len(arr) - 1)


def merge_sort_bottom_up(arr):
	"""效率略低于递归实现的归并，好处是可以应用于链表结构，因为内部实现不需要数组取值操作"""
	sz = 1
	n = len(arr)
	while sz <= n:  # 实现思路：每次将sz大小的切片两两merge，对sz进行loop，就形成了归并排序
		i = 0
		while i + sz < n:  # 边界越界检测
			__merge(arr, i, i + sz - 1, min(i + sz * 2 - 1, n - 1))
			i += sz * 2
		sz *= 2


def __partition(arr, l, r):
	pivot = arr[l]
	j = l
	for i in xrange(l + 1, r + 1):
		if arr[i] < pivot:
			arr[i], arr[j + 1] = arr[j + 1], arr[i]
			j += 1
	arr[j], arr[l] = arr[l], arr[j]
	return j


def __quick_sort(arr, l, r):
	if l >= r:
		return
	mid = __partition(arr, l, r)
	__quick_sort(arr, l, mid)
	__quick_sort(arr, mid + 1, r)


def quick_sort(arr):
	"""快速排序"""
	__quick_sort(arr, 0, len(arr)-1)
