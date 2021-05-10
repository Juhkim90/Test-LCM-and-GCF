# Ctrl + Enter
















































def lcm(n1, n2):
	if (n1 <= 0 or n2 <= 0):
		return "Wrong input. Positive integers Only"
	if (n1 >= n2):
		greater = n1
	elif (n1 < n2):
		greater = n2

	while (True):
		if (greater % n1 == 0 and greater % n2 == 0):
			return greater
		else:
			greater += 1

def gcf(n1, n2):
	if (n1 <= 0 or n2 <= 0):
		return "Wrong input. Positive integers Only"
	if (n1 <= n2):
		smaller = n1
	elif (n1 > n2):
		smaller = n2

	for x in range(1, smaller + 1):
		if (n1 % x == 0 and n2 % x == 0):
			smaller = x
	return smaller

print("Least Common Multiple")
print(lcm(int(input("Enter a number: ")), int(input("Enter a number: "))))
print("Greatest Common Factor")
print(gcf(int(input("Enter a number: ")), int(input("Enter a number: "))))