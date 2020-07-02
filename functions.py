def hello_world():
    return 'hello world'


result = hello_world()

message = '{} {} {}'.format(result, result, result)

print(message)
