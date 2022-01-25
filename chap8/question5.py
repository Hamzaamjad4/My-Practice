def CountOccurrences(s1, s2):
	count = 0
	start = 0
	while start < len(s1):
		pos = string.find(s2, start)
		if pos != -1:
			start = pos + 1
			count += 1
		else:
			break
	return count

string = "My Pakistan"
print(CountOccurrences(string, "My"))
