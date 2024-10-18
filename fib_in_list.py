def fib_elem_gen():
    """Генератор, возвращающий элементы ряда Фибоначчи"""
    a = 0
    b = 1

    while True:
        yield a
        res = a + b
        a = b
        b = res


class EvenNumbersIterator():

    def __init__(self, instance):
        g = fib_elem_gen()
        #print(instance)
        self.instance = instance
        self.idx = 0  # инициализируем индекс для перебора элементов

        mi = max(instance)
        self.fib = []
        now = 1;

        while mi > now:
            now = next(g)
            self.fib.append(now)

    def __iter__(self):
        return self  # возвращает экземпляр класса, реализующего протокол итераторов

    def __next__(self):  # возвращает следующий по порядку элемент итератора
        while True:
            try:
                res = self.instance[self.idx]  # получаем очередной элемент из iterable

            except IndexError:
                raise StopIteration

            if res in self.fib:  # проверяем на четность элемента
                self.idx += 1  # если четный, возвращаем значение и увеличиваем индекс
                return res

            self.idx += 1  # если нечетный, то просто увеличиваем индекс



if __name__ == "__main__":
    print(list(EvenNumbersIterator([0,1,2,3,4,5,6,7,8,9])))  # [0, 2, 4, 6, 8]
    assert list(EvenNumbersIterator([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1])) ==  [0, 1, 2, 3, 5, 8, 1]