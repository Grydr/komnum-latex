import sympy as sp
import sys
import math
from latex2sympy2_extended import latex2sympy
    
def print_table(tex, x0, x1, iterations):
    x = sp.symbols("x")
    sp_f = latex2sympy(tex)

    def f(x_val):
        return sp_f.subs(x, x_val).evalf()
    
    def secant_method(x0, x1):
        return x1 - f(x1) * (x1 - x0) / float(f(x1) - f(x0))
    
    table_rows = ""

    for i in range(iterations):
        x2 = secant_method(x0, x1)

        table_rows += (
            f"{i+1} & "
            f"\\num{{{x0:.5f}}}".replace('.', ',') + " & "
            f"\\num{{{x1:.5f}}}".replace('.', ',') + " & "
            f"\\num{{{f(x0):.5f}}}".replace('.', ',') + " & "
            f"\\num{{{f(x1):.5f}}}".replace('.', ',') + " & "
            f"\\num{{{x2:.5f}}}".replace('.', ',') + "\\\\" + "\n"
        )

        x0, x1 = x1, x2

        if (abs(f(x2)) < 10 ** -10):
            break

    latex_table = f"""\\begin{{tabular}}{{|c|c|c|c|c|c|c|}}
\\hline
iterasi & $x_{{i-1}}$ & $x_i$ & $f(x_{{i-1}})$ & $f(x_i)$ & $x_{{i+1}}$ \\\\
\\hline
{table_rows} \\hline
\\end{{tabular}}
"""

    print(latex_table)

if __name__ == "__main__":
    tex = rf"{sys.argv[1]}"
    x0 = float(sys.argv[2])
    x1 = float(sys.argv[3])
    iterations = int(sys.argv[4])
    print_table(tex, x0, x1, iterations)