n, t = map(int, input().split())
s  = input()

while t > 0:
    i = 0
    while i < n - 1:
        if s[i] == 'B' and s[i + 1] == 'G':
            s = s[:i] + 'GB' + s[i + 2:]
            i += 1
        i += 1
    t -= 1
print(s)
