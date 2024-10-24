from cmath import sqrt
x1, y1, x2, y2=map(int,input().split())
print(sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2))