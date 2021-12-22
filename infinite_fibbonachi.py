class Fib:    
    """По объектам этого класса можно итерироваться и получать числа Фибоначчи"""

    class _Fib_iter:
        """Внутренний класс — итератор"""
        def __init__(self):
            self.fib_1 = 1
            self.fib_2 = 1
        
        def __next__(self):
            j = self.fib_1
            h = self.fib_2
            self.fib_2 = j + h
            self.fib_1 = h
            return j


    def __iter__(self):
        """Создать и вернуть итератор"""
        return Fib._Fib_iter()

f = Fib()

for i in f:
    print(i)
    if i>10000:
        break
