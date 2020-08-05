m = int(input()); n = int(input())
A = []
B = []
for i in range(1, 101):
    a = i * i
    if m <= a <= n:
        A.append(a)
if A == B:
    print(-1)
else:
    print(sum(A))
    print(min(A))