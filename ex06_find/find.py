import argparse
parser = argparse.ArgumentParser()

parser.add_argument('files', metavar = 'F', type = str, nargs = '+')
parser.add_argument('-name', '--names', action = "store_true", help = "find the directories.")
parser.add_argument('-type', '--types', action = "store_true", help = 'the type of the file.')
parser.add_argument('-print', '--prints', action = 'store_true', help = 'print path name of the current file.')
args = parser.parse_args()
print(args)
