# Sort Algorithms --- increasing sequence

A = [1, 5, 9, 20, 3, 6, 0, 21, 45, 30]

def bubble_sort(A):
	for j in range(len(A), 1, -1):
		for i in range(0, j-1):
			if A[i] > A[i+1]:
				A[i], A[i+1] = A[i+1], A[i]
	return A

def insertion_sort(A):
	for i in range(2, len(A)):
		for j in range(i-1, 1, -1):
			if A[j] < A[j-1]:
				A[j], A[j-1] = A[j-1], A[j]
	return A

def selection_sort(A):
	for i in range(0, len(A)-1):
		minIndex = i
		for j in range(i+1, len(A)):
			if A[j] < A[minIndex]:
				minIndex = j
		A[i], A[minIndex] = A[minIndex], A[i]
	return A

def quick_sort(A):
	if len(A) <= 1:
		# 要注意长度 <= 1 的情况
		return A
	else:
		i = 0
		for j in range(1, len(A)):
			if A[j] < A[i]:
				A[i], A[j] = A[j], A[i]
				i += 1
		left_part = quick_sort(A[:i])
		right_part = quick_sort(A[i+1:])
		return A

def merge_lists(left, right):
	i, j = 0, 0
	res = []
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			res.append(left[i])
			i += 1
		else:
			res.append(right[i])
			j += 1
	# 要注意当一个list空了，需要将另外一个list补上的情况。
	res.extend(left[i:])
	res.extend(right[j:])
	return res


def merge_sort(A):
	if len(A) <= 1:
		return A
	else:
		pivot = int(len(A)/2)
		left = merge_sort(A[:pivot])
		right = merge_sort(A[pivot:])
		A = merge_lists(left, right)

	return A
	
	

B = selection_sort(A)
C = bubble_sort(A)
D = insertion_sort(A)
E = quick_sort(A)
F = merge_sort(A)
print(F)





