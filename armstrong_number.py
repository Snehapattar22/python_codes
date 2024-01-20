def is_armstrong(num):
	n_str = str(num)
	l = len(n_str)
	sum = 0
	for digit in n_str:
		sum += int(digit)**l
	if sum == num:
		return True
	else:
		return False
num=int(input())
print(is_armstrong(num))
