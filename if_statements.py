import unittest

tc = unittest.TestCase()

# equal equal
tc.assertTrue(3 == 3)
tc.assertFalse(3 == 2)

tc.assertTrue('cow' == 'cow')
tc.assertTrue(10.44444 == 10.44444)

# not equal
tc.assertTrue(3 != 5)
someBool = False
tc.assertTrue(not someBool)
tc.assertFalse(not 33 == 33)

# less/greater than
tc.assertTrue(3 > 1)
tc.assertTrue(10 < 20)

tc.assertFalse(3 > 3)
tc.assertFalse(not 3 >= 3)

var = 10
if True:
    var = 20
tc.assertEqual(var, 20)

var = 10
if False:
    var = 20
tc.assertEqual(var, 10)

var = 10
if False:
    var = 20
elif False:  # else if
    var = 30
elif False:  # else if
    var = 40
else:
    var = 50
tc.assertEqual(var, 50)
