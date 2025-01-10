from src import gen_fib

def test1():
    # given
    n1 = 10
    n2 = 5
    n3 = 7
    my_genn = gen_fib.fib_coroutine(gen_fib.my_genn)
    gen = my_genn()

    # when
    ans1 = gen.send(n1)
    ans2 = gen.send(n2)
    ans3 = gen.send(n3)

    # then
    assert ans1 == [f'{n1}:', 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert ans2 == [f'{n2}:', 1, 1, 2, 3, 5, 8]
    assert ans3 == [f'{n3}:', 1, 1, 2, 3, 5, 8, 13, 21]

test1()
