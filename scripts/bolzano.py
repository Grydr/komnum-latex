import sympy as sp
import sys
import math
from latex2sympy2_extended import latex2sympy

def print_bolzano(tex, lower_bound, upper_bound, total_iteration, decimal_digits):
    x = sp.symbols("x")
    function = latex2sympy(tex)

    x_1 = lower_bound
    x_2 = upper_bound

    def f(x_val):
        return function.subs(x, x_val).evalf()
    
    def sign(val):
        return -1 if val < 0 else 1

    table_rows = ""

    for i in range(total_iteration):
        x_3 = (x_1 + x_2)/2

        table_rows += (
            f"{i+1}" + " & " +
            "\\num{" + f"{x_1:.{decimal_digits}f}".replace('.',',') + "}" + " & " +
            "\\num{" + f"{x_2:.{decimal_digits}f}".replace('.',',') + "}" + " & " +
            "\\num{" + f"{x_3:.{decimal_digits}f}".replace('.',',') + "}" + " & " +
            "\\num{" + f"{f(x_1):.{decimal_digits}f}".replace('.',',') + "}" + " & " +
            "\\num{" + f"{f(x_2):.{decimal_digits}f}".replace('.',',') + "}" + " & " +
            "\\num{" + f"{f(x_3):.{decimal_digits}f}".replace('.',',') + "}" + "\\\\" + "\n"
        )

        if (abs(f(x_3)) < 10 ** -(decimal_digits+1)):
            break

        if (sign(f(x_3)) == sign(f(x_1))):
            x_1 = x_3
        else:
            x_2 = x_3

    latex_table = f"""\\begin{{tabular}}{{|c|c|c|c|c|c|c|}}
\\hline
iterasi & $x_1$ & $x_2$ & $x_3$ & $f(x_1)$ & $f(x_2)$ & $f(x_3)$ \\\\
\\hline
{table_rows} \\hline
\\end{{tabular}}
"""
    
    print(latex_table)

if __name__ == "__main__":
    string = str(sys.argv[1])
    tex = rf"{string}"
    lower_bound = float(sys.argv[2])
    upper_bound = float(sys.argv[3])
    iteration = int(sys.argv[4])
    decimal_digits = int(sys.argv[5])
    print_bolzano(tex, lower_bound, upper_bound, iteration, decimal_digits)