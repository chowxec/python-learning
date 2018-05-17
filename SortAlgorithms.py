

# BubbleSort
def bubble_sort(a):
	for i in range(len(a), 0, -1):
		for j in range(i - 1):
			if a[j] > a[j + 1]:
				a[j], a[j + 1] = a[j + 1], a[j]
	return a

# SelectSort
def select_sort(a):
	for i in range(len(a), 0, -1):
		max = i - 1
		for j in range(max):
			max = j if a[j] > a[max] else max
			a[i - 1], a[max] = a[max], a[i - 1]
	return a

# InsertSort
def insert_sort(a):
	for i in range(len(a), 0, -1):
		for j in range(i - 1, len(a) - 1):
			if a[j] > a[j + 1]:
				a[j], a[j + 1] = a[j + 1], a[j]
	return a

# MergeSort

# QuickSort

# HeepSort

# CountSort


# data
a = [5,3,1,4,2,9,8,0,6,7]

# 
#print(bubble_sort(a))
#print(select_sort(a))
#print(insert_sort(a))
print(bubble_sort(a))
