class Fib:    
    """По объектам этого класса можно итерироваться и получать числа Фибоначчи"""

    class _Fib_iter:
        """Внутренний класс — итератор"""
        def __init__(self):
            self.fibs = [1, 1]
        
        def __next__(self):
            j = self.fibs[0]
            h = self.fibs[1]
            self.fibs[1] = j + h
            self.fibs[0] = h
            return j


    def __iter__(self):
        """Создать и вернуть итератор"""
        return Fib._Fib_iter()

f = Fib()

for i in f:
    print(i)
    if i>10000:
        break
