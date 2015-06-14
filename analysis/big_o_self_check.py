def min_quad(list):
	min = None
	for x in list:
		is_min = True
		for y in list:
			if y < x:
				is_min = False
		if is_min:
			min = x
	return min

def min_linear(list):
	min = list[0]
	for x in list:
		if x < min:
			min = x
	return min