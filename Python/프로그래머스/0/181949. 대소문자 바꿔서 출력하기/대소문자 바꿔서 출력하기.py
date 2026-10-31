str = input()

for c in str:
    if ord(c) < 97:
        print(c.lower(), end = "")
    else:
        print(c.upper(), end = "")