def count(s, c):
    res = 0
    for i in range(len(s)):

        # Checking character in string
        if (s[i] == c):
            res = res + 1
    return res
str = "My Pakistan"
c = 's'
print(count(str, c))