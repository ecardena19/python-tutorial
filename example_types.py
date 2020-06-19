import unittest

tc = unittest.TestCase()

# boolean
bool1 = True
bool2 = False

tc.assertEqual(bool1, True)

# integers
int1 = 2 ** 63
int2 = 2 ** 63

tc.assertEqual(int1 + int2, 18446744073709551616)
tc.assertEqual(int1 - 1, 9223372036854775807)

# float
float1 = 332343.00000002
float2 = 33.00000001
float_sum = float1 + float2

tc.assertEqual(float_sum, 332376.00000003004)

# strings
string1 = 'hello world'
string2 = "hello world"
string3 = 'sldkjdlksfjslkj333##===0ÏÏ-™£™£∞'

# lists
empty_list = []
list_with_one_element = ['a']
list_with_many_elements = [1, 3, 5, 5, 0, -1]

name1 = 'Bonds'
name2 = 'Sanders'
list1 = [name1, 1, name2, 33, 49]
tc.assertEqual(list1, ['Bonds', 1, 'Sanders', 33, 49])
tc.assertEqual(list1[4], 49)

list1.remove('Bonds')
tc.assertEqual(list1, [1, 'Sanders', 33, 49])
list1.pop(1)
tc.assertEqual(list1, [1, 33, 49])
del list1[1]
tc.assertEqual(list1, [1, 49])

list2 = [1, 3, 5]
list2.append(11)
tc.assertEqual(list2, [1, 3, 5, 11])

list3 = ["Red Sox", "Yankees", "Dodgers"]
list3.reverse()
tc.assertEqual(list3, ['Dodgers', 'Yankees', 'Red Sox'])

list4 = [123, 125, 100]
list4.sort()
tc.assertEqual(list4, [100, 123, 125])

beers = {}
tc.assertEqual(beers.get(100), None)

chemical_reactions = {}
chemical_reactions.update({'name': 'aldol condensation2'})
chemical_reactions.update({'name': 'sharpless epoxidation', 'abc': 123})
tc.assertEqual(chemical_reactions.get('name'), 'sharpless epoxidation')

# bolean decimal value is being read by index function instead of reading appropriate
# element's index position within the tuple
tuple1 = ('string', 132, False)
print(tuple1.index(0))
