s = input()
if len(s) > 10:
    print(s[:6])
else:
    print(s.ljust(12, 'o'))    