import unittest

tc = unittest.TestCase()


# methods, definitions, and functions are all the same thing
def inc(x):
    return x + 1


tc.assertEqual(inc(335), 336)
tc.assertEqual(inc(35), 36)
tc.assertEqual(inc(10), 11)


def square(x):
    return x ** 2


print(square(10))
