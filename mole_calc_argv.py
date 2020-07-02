import sys

print(sys.argv)

name1 = sys.argv[1]
name2 = sys.argv[2]
result = "Number of moles"
message = "{} {}".format(float(name1)/float(name2), result)
print(message)
