from src import fib_in_list


def test1():
    # given
    cin = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    eni = fib_in_list.EvenNumbersIterator

    # when
    ans = list(eni(cin))

    # then
    assert ans == [0, 1, 2, 3, 5, 8]


def test2():
    # given
    cin = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 25, 331, 89, 33, 34, 55, 22]
    eni = fib_in_list.EvenNumbersIterator

    # when
    ans = list(eni(cin))

    # then
    assert ans == [0, 1, 2, 3, 5, 8, 1, 89, 34, 55]


test1()
test2()
