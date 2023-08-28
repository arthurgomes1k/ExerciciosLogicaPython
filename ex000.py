a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)


if a > b and a > c:
    n3 = a
    if b > c:
        n2 = b
        n1 = c
    else:
        n2 = c
        n1 = b
if b > a and b > c:
    n3 = b
    if a > c:
        n2 = a
        n1 = c
    else:
        n2 = c
        n1 = a
if c > a and c > b:
    n3 = c
    if a > b:
        n2 = a
        n1 = b
    else:
        n1 = a
        n2 = b
print(n1)
print(n2)
print(n3)
print()
print(a)
print(b)
print(c)
