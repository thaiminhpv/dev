def shortestBeautifulSubstring(s: str, k: int) -> str:
	ans = None
	n = len(s)
	for i in range(n):
		for j in range(i, n):
			t = s[i:j+1]
			if t.count('1') == k and (ans is None or len(t) < len(ans) or (len(t) == len(ans) and t < ans)):
				ans = t
	return "" if ans is None else ans

def function1(var1: str, var2: int) -> str:
	var3 = None
	var4 = len(var1)
	for var5 in range(var4):
		for var6 in range(var5, var4):
			var7 = var1[var5:var6 + 1]
			if var7.count('1') == var2 and (var3 is None or len(var7) < len(var3) or (len(var7) == len(var3) and var7 < var3)):
				var3 = var7
	return '' if var3 is None else var3