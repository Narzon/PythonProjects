def Collatz(i, j):
	iteration = i
	v = 1

	while iteration < (j + 1):
		cycLength = 1
		num = iteration
		while num != 1:
			cycLength += 1
			if num % 2 == 0:
				num = num / 2
			else:
				num = (num * 3) + 1
		iteration += 1
		if cycLength > v:
			v = cycLength

	return v


def main():

	value = Collatz(1, 10)
	print(value)
	value = Collatz(100, 200)
	print(value)
	value = Collatz(201, 210)
	print(value)
	value = Collatz(900, 1000)
	print(value)

main()