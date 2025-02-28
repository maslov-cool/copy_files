import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--upper', action="store_const", const=True, dest="upper", default=False)
parser.add_argument('--lines', default='all')
parser.add_argument('source', type=str)
parser.add_argument('receiver', type=str)

args = parser.parse_args()
file = open(args.source).readlines()
if args.lines == 'all' or int(args.lines) >= len(file):
    args.lines = len(file)
else:
    args.lines = int(args.lines)
with open(args.receiver, 'w') as f:
    for i in range(args.lines):
        if args.upper:
            f.write(file[i].upper())
        else:
            f.write(file[i])




