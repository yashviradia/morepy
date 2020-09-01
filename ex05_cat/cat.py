import argparse
parser = argparse.ArgumentParser()

parser.add_argument('files', metavar = 'F', type = str, nargs = '+')
parser.add_argument('-n', '--numbers', action = 'store_true', help = 'Print line numbers')
parser.add_argument('-b', '--lines', action = 'store_true', help= 'number the non-blank output lines.')
parser.add_argument('-s', '--squeeze', action = 'store_true', help = 'Squeeze multiple adjacent empty lines, causing the output to be single spaced.')

args = parser.parse_args()


print(">>> parsed args: ", args)

# implementation of the -n
line_number = 1
for in_file_name in args.files:
    in_file = open(in_file_name)
    if args.numbers:
        for line in in_file.readlines():
            print(f"\t{line_number}\t{line}", end = "")
            line_number += 1
    else:
        print(in_file.read())

# implementation of the -b in cat
line_nums = 1
for in_file_name in args.files:
    in_file = open(in_file_name)
    if args.lines:
        for line_read in in_file.readlines():
            print(f"{line_nums}\t{line_read}", end = "")
            line_nums += 1
    else:
        print(in_file.read())

# implementation of the -s in cat
line_squeeze = 1
for in_file_name in args.files:
    in_file = open(in_file_name)
    if args.lines:
        for line_squeeze_num in in_file.readlines():
            print(f"{line_squeeze}\t{line_squeeze_num}", end = "")
            line_squeeze += 1
    else:
        print(in_file.read())
