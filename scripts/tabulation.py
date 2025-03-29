import sympy as sp
import sys
import math
from latex2sympy2_extended import latex2sympy

def print_tabulation(tex, lower_bound, upper_bound, step, table_count):
    x = sp.symbols("x")
    f = latex2sympy(tex)

    def find_sign_change(x_values, f_values):
        for i in range(1, len(f_values)):
            if (f_values[i-1] > 0 and f_values[i] < 0) or (f_values[i-1] < 0 and f_values[i] > 0):
                return i-1
        return -1
    
    decimal_places = max(2, -int(math.log10(step)))
    
    latex_output = ""
    for _ in range(table_count):
        row_count = 11
        x_values = [lower_bound + step * i for i in range(row_count)]
        f_values = [f.subs(x, val).evalf() for val in x_values]

        sign_change_index = find_sign_change(x_values, f_values)

        table_rows = "\n".join([
            ("\\textcolor{red}{\\num{" + f"{x_val:.{decimal_places}f}".replace('.', ',') + "}}" + 
            f" & \\textcolor{{red}}{{\\num{{{f_val:.4f}}}}}".replace('.', ',')
            if i == sign_change_index or i == sign_change_index + 1 else
            "\\num{" + f"{x_val:.{decimal_places}f}".replace('.', ',') + "}" +
            f" & \\num{{{f_val:.4f}}}".replace('.', ','))
            + " \\\\" for i, (x_val, f_val) in enumerate(zip(x_values, f_values))
        ])

        decimal_places = min(5, decimal_places + 1)

        latex_table = f"""\\begin{{tabular}}{{|c|c|}}
\\hline
$x$   & $f(x)$ \\\\
\\hline
{table_rows}
\\hline
\\end{{tabular}}\\quad
"""

        latex_output += latex_table

        lower_bound = x_values[sign_change_index]
        step /= 10

    print(latex_output)

if __name__ == "__main__":
    string = str(sys.argv[1])
    tex = rf"{string}"
    lower_bound = float(sys.argv[2])
    upper_bound = float(sys.argv[3])
    step = float(sys.argv[4])
    table_count = int(sys.argv[5])
    print_tabulation(tex, lower_bound, upper_bound, step, table_count)

    # example: python3 tabulation.py "e^x - x - 2" -2 -1 0.1 4 | xclip -selection clipboard
