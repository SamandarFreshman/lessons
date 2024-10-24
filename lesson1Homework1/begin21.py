from cmath import sqrt
x1, y1, x2, y2, x3, y3 =map(int,input().split())
a=sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
b=sqrt(abs(x2-x3)**2+abs(y2-y3)**2)
c=sqrt(abs(x3-x1)**2 + abs(y3-y1)**2)
p=(a+b+c)/2
S=sqrt(p*(p-a)*(p-b)*(p-c))
print(S)
