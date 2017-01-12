#!/usr/local/bin/python


def trapping_rain_water(data):
	left_max = [data[0]]
	right_max = [data[-1]]
	for x in data[1:]:
		left_max.append(max(x, left_max[-1]))
	
	for x in reversed(data[:-1]):
		right_max.insert(0, max(x, right_max[0]))
	# if loop append	
	# right_max.append(max(x, right_max[-1])))
	#right_max.reverse()
	
	sum = 0
	for idx, val in enumerate(data):
		sum = sum + (min(left_max[idx], right_max[idx]) - val)

	return sum


if __name__ == '__main__':
	data = [ 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
	#data = [3, 0, 0, 2, 0, 4]
	ret = trapping_rain_water(data)
	print(ret)
