# Estudo N°1 sobre a biblioteca argparse.

# Estrutura básica:
# import argparse --> importação da biblioteca.
# parser = argparse.ArgumentParser() --> definição do parser.
# parser.add_argument("exemplo") --> adição de argumentos ao parser.
# args = parser.parse_args() --> passando argumentos do parser para uma variável.


# execute pelo terminal com --> python note1.py (input)
import argparse 
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display a square of a given number")
parser.add_argument("-v", "--verbose", action="count", default=0, help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose == 1:
    print(f'the square of {args.square} equals {answer}')
elif args.verbose >= 2:
    print(f'{args.square}² == {answer}')
else:
    print(answer)
    