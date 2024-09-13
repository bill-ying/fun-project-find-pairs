import time


def find_pairs_slow(input_list, sum_target):
	pairs = []
	
	for i in range(len(input_list)):
		for j in range(i+1, len(input_list)):
			if input_list[i] + input_list[j] == sum_target:
				pairs.append((input_list[i], input_list[j]))
	
	return list(set(pairs))


def find_pairs(input_list, sum_target):
	pairs=[]
	seen = set()
	
	for number in input_list:
		complement = sum_target - number
		
		if complement in seen:
			pairs.append((complement, number))
		
		seen.add(number)
	
	return list(set(pairs))
	

my_list = [5, -3, 9, 0, 1, 7, 7, 3, 8, 2, 1, -5, 11, 4, 6, 8, -2]
target = 10
start_time = time.time()
result = find_pairs_slow(my_list, target)
end_time = time.time()
print("Slow: ", result, f"time taken: {end_time - start_time}")

start_time = time.time()
result = find_pairs(my_list, target)
end_time = time.time()
print("Fast: ", result, f"time taken: {end_time - start_time}")