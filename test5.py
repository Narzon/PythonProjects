def main():
	num = 75
	for i in range (1, num + 1):
		for j in range (1, (i - 1), 2):
			if i % 2 == 0:
				print ((j + 1), end = " ")
			if (i - 2) == j:
				print()
	while (num >= 1):
		for i in range (1, num):
			if i % 2 == 0:
				print (i, end = " ")
			if i == (num - 1):
				print()
		num -= 2
main()