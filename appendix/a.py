def makeSmallestPalindrome(s: str) -> str:
	s = list(s)
	n = len(s)
	for i in range(n):
		c = min(s[i], s[n - 1 - i])
		s[i] = c
		s[n - 1 - i] = c
	return "".join(s)


def function1(var1: str) -> str:
	var1 = list(var1)
	var2 = len(var1)
	for var3 in range(var2):
		var4 = min(var1[var3], var1[var2 - 1 - var3])
		var1[var3] = var4
		var1[var2 - 1 - var3] = var4
	return ''.join(var1)


