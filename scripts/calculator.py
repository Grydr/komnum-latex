import sympy as sp
import sys
import math
from latex2sympy2_extended import latex2sympy

def substitute(f, x_val):
    x = sp.symbols("x")

    return f.subs(x, x_val).evalf()

if __name__ == "__main__":
    tex = rf"{sys.argv[1]}"
    f = latex2sympy(tex)
    x_val = float(sys.argv[2])
    print(substitute(f, x_val))
