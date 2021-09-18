# Python3 program to find positions
# of zeroes flipping which produces
# maximum number of xonsecutive 1's

# m is maximum of number zeroes allowed
# to flip, n is size of array
def findZeroes(arr, m) :
    # initializing left and right indices of current subarray
	left_index = right_index = 0
    # initializing values that hold starting index of best
    # subarray and its length, for extracting zeroes 
	best_index = bestWindow = 0
	zeroCount, length = 0, len(arr)
	while right_index < length:
		if zeroCount <= m :
			if arr[right_index] == 0 :
				zeroCount += 1
			right_index += 1
		if zeroCount > m :
			if arr[left_index] == 0 :
				zeroCount -= 1
			left_index += 1
		# checking if a new best window is found
		if (right_index-left_index > bestWindow) and (zeroCount<=m) :
			# updating length of best window and its starting index
			bestWindow = right_index - left_index
			best_index = left_index
	ans = []
	for i in range(0, bestWindow):
		if arr[best_index + i] == 0:
			ans.append(best_index + i)
	return ans

# Driver program
arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
m = 3
print(findZeroes(arr, m))

# This code is contributed by Shreyanshi Arun.
