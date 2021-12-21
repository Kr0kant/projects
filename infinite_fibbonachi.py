class Fib:    
    """По объектам этого класса можно итерироваться и получать числа Фибоначчи"""

    class _Fib_iter:
        """Внутренний класс — итератор"""
        def __init__(self):
            self.i = 0
            self.fibs = [1]
        
        def __next__(self):
            j = self.i
            self.i += 1
            if self.i == 1:
                self.fibs.append(1)
                return self.fibs [j]
            else:
                self.fibs.append(self.fibs[j-1]+self.fibs[j])
                return self.fibs [j]


    def __iter__(self):
        """Создать и вернуть итератор"""
        return Fib._Fib_iter()

f = Fib()

for i in f:
    print(i)
    if i>1000:
        break
