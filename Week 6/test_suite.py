import test_debug1
import test_debug2


def test_jump_db1():
    print("Expect shift of 1, the result: ", test_debug1.caesar("z", "a"))
    print("Expect shift of 1, the result: ", test_debug1.caesar("a", "b"))
    print("Expect shift of 1, the result: ", test_debug1.caesar("za", "ab"))
    print("Expect shift of 2, the result: ", test_debug1.caesar("z", "b"))
    print("Expect shift of 2, the result: ", test_debug1.caesar("a", "c"))
    print("Expect shift of 25, the result: ", test_debug1.caesar("z", "y"))
    print("Expect shift of 25, the result: ", test_debug1.caesar("a", "z"))
    print("Expect shift of 24, the result: ", test_debug1.caesar("z", "x"))
    print("Expect shift of 24, the result: ", test_debug1.caesar("a", "y"))


def test_words_db1():
    print("Expect shift of 25, the result: ", test_debug1.caesar("zack",
                                                                 "yzbj"))
    print("Expect shift of 5, the result: ", test_debug1.caesar("very",
                                                                 "ajwd"))

def test_db2():
    print("expected 1, got: ", test_debug2.match("a", "a"))
    print("expected 3, got: ", test_debug2.match("established", "ballistic"))
    print("expected 3, got: ", test_debug2.match("abc", "abcabc"))
    print("expected 1, got: ", test_debug2.match("abc", "cba"))


def test_db1():
    test_jump_db1()
    test_words_db1()


if __name__ == '__main__':
    test_db2()

