'''
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
 если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
'''
n = int(input("Введите длину шоколадки\n"))
m = int(input("Введите ширину шоколадки\n"))
k = int(input("Введите количество долек\n"))

if (k%n==0 or k%m==0) and k<m*n:
    print("Можно")
else:
    print("Нельзя")