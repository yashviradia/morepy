
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('integers', metavar='N', type=int, nargs='+')
parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max,
                    help='sum the integers (default: find the max)')
parser.add_argument('echo', help="echo the string you use here.")
parser.add_argument('-z', '--start', action='store_true')
parser.add_argument('-x', '--stop', action='store_false')
parser.add_argument('-f', '--foo', help="foo help")
parser.add_argument('-b', '--bar', help="bar help")
parser.add_argument('-c', '--char', help="char help")
parser.add_argument("square", help="display a square of a given number.", type=int)

args = parser.parse_args()
print(args)
