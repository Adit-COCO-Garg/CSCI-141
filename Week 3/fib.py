def fib_1():
    return 0


def fib_2():
    return 1


def fib_3():
    return fib_2() + fib_1()


def fib_4():
    return fib_3() + fib_2()


def fib_calc(num):
    if num <= 0:
        return None
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fib_calc(num-1) + fib_calc(num-2)


def test_negative():
    print("Should be none ", fib_calc(-5))


def test_0():
    print("Should be None: ", fib_calc(0))


def test_four():
    print("Should be 2: ", fib_calc(4))


def run_all_tests():
    test_0()
    test_four()
    test_negative()


run_all_tests()
