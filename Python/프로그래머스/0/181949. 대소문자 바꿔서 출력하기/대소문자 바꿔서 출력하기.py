str = input()
count = 0
for c in str:
    if ord(c) < 97:
        c = c.lower()
    else:
        c = c.upper()
    count += 1
    print(c, end="")