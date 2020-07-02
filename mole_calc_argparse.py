import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--mass')
parser.add_argument('-w', '--molecular_weight')

args = parser.parse_args()

result = "Number of moles"
message = "{} {}".format(float(args.mass)/float(args.molecular_weight), result)
print(message)
