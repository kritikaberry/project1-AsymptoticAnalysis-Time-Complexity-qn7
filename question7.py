def compute_sum(a, b, c, n):
	total = 0
	for i in range(1, n + 1):
		for j in range(i, n + 1):
			for k in range(j * j, n + 1):
				total += a[i] * b[j] * c[k]
	return total

if __name__ == "__main__":
	n = 5
	a = [0, 1, 2, 3, 4, 5]
	b = [0, 2, 3, 4, 5, 6]
	c = [0, 3, 4, 5, 6, 7]
	result = compute_sum(a, b, c, n)
	print("Result:", result)
