# Estudo N°3 da biblioteca argparse.

import argparse
parser = argparse.ArgumentParser(prog="lqspow", description="calculate X to the power of Y using %(prog)s")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
group.add_argument("-q", "--quiet", action="store_true", help="run simple output")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

# quiet e verbose fazem parte do mesmo grupo, logo não podem ser executados juntos, apenas um de cada vez.
if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")