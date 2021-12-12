def gcd(a,b): #Поиск НОД
    if a == 0: #Проверка чисел на 0, если 0 - НОД = abs(b)
        return(abs(b)) 
    elif b == 0:
        return(abs(a))
    else:
        c = max(abs(a),abs(b)) #НОД определён с точностью до ассоциированности - ищем для положительных
        d = min(abs(a),abs(b))
        f = 0
        while c % d != 0: #Алгоритм Евклида
            f = d
            d = c % d #Остаток - новый минимум
            c = f #Делимое - новый максимум
        return (d) 

a = int(input('Первое число: '))
b = int(input('Второе число: '))

print('НОД = ',gcd(a,b)) 