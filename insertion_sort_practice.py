from random import randint

def insertion_sort(arr, f_loop, w_loop):
	key = 1
	# swap_happened = False
	for num in range(key, len(arr)):
		# swap_happened = False
		# print(f"Iteration {key}\nFor loop status: {arr}")
		if arr[key] < arr[key-1]:
			working_index = key-1
			# swap_happened = True
			# print("Swap happened, running working_index key {}".format(working_index))
			arr[key], arr[key-1] = arr[key-1], arr[key]
			while working_index>0:
				# print(f"--While loop status: {arr}")
				w_loop += 1
				if arr[working_index] < arr[working_index-1]:
					# print(f"--Swap happened: {arr[working_index-1]}, {arr[working_index]}")
					arr[working_index], arr[working_index-1] = arr[working_index-1], arr[working_index]
				else: break
				working_index -= 1
		# if swap_happened == False:
		# 	print("No swap occurred")
		key += 1
		f_loop += 1
	return f_loop, w_loop


w_loop = 0
f_loop = 0
l1 = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
l2 = [randint(0,5000) for num in range(10000)]
# print("Input list:")
# print(l2)
f_loop, w_loop = insertion_sort(l2, f_loop, w_loop)
print("Output list:")
print(l2)
print(f"Number of for loops: {f_loop}")
print(f"Number of while loops: {w_loop}")
