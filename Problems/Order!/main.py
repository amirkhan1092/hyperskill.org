lst = []
for _ in range(3):
    lst.append(int(input()))

if sorted(lst) == lst:
    print(True)
else:
    print(False)
