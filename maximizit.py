from itertools import product

K, M = map(int,input().split())
data = [map(int,input().split()[1:]) for _ in range(K)]

F = lambda x: x**2               
S = lambda x: sum(map(F, x)) % M

print(max(map(S, product(*data))))
