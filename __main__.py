import argparse

import formula


def load_formula(value):
    try:
        return getattr(formula, value)
    except AttributeError:
        raise argparse.ArgumentTypeError("Formula {0} doesn't exist".format(value))


parser = argparse.ArgumentParser()
parser.add_argument('formula', type=load_formula)
parser.add_argument('quantity', type=float)
parser.add_argument('max_depth', type=int, default=0)
arguments = parser.parse_args().__dict__
formula_class = arguments.pop('formula')
print(formula_class(**arguments))
