def hello_world():
    return 'hello world'


for x in range(3):  # [0, 1, 2]
    print(hello_world())


def print_hello_world():
    print('hello world')


for x in range(3):
    print_hello_world()


def print_my_name(name):
    print('hello ' + name)


print_my_name('emilio')


# [print_my_name(n) for n in ['emilio', 'adam']]
# map(print_my_name, ['emilio', 'adam'])


def addition(int1, int2):
    return int1 + int2


print(addition(1, 2))


def multiply(int3, int4):
    return int3 * int4


print(multiply(3, 100))


def division(float1, float2):
    return int(float1 / float2)


print(division(25, 12.2))

# function composition

print(multiply(10, addition(1, 3)))
print(10 * 1 + 3)


def to_lower_case(string):
    return string.lower()


def to_upper_case(string):
    return string.upper()


print(to_lower_case(to_upper_case('test')))
print(to_upper_case(to_lower_case('test')))

print(multiply(5, division(5, addition(5, 1))))
