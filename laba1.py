#a*x**2 + b*x + c == 0

import math
a, b, c = map(float, input().split())
D = (b)**2 - 4*a*c
if D<0:
    print('корней нет')
elif D==0:
    print('Корень ур-я:', float((-1*b)/(2*a)))
else:
    print('Первый корень ур-я:', float(((-1*b) + math.sqrt(D)) / (2*a)))
    print('Второй корень ур-я:', float(((-1*b) - math.sqrt(D)) / (2*a)))

#Брезгунова АР БВТ2303