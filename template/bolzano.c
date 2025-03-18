#include <stdio.h>
#include <math.h>

double f(double x) {
    return x * x * x - 2 * x - 5; // f(x) = x^3 - 2x - 5
}

double bolzano_method(double a, double b, double tol, int max_iter, double *root) {
    if (f(a) * f(b) >= 0) {
        printf("Error: Fungsi harus memiliki tanda yang berbeda di a dan b.\n");
        return NAN;
    }

    double c;
    for (int i = 0; i < max_iter; ++i) {
        c = (a + b) / 2;
        printf("Iterasi %d: a = %.5f, b = %.5f, c = %.5f, f(c) = %.5f\n", i + 1, a, b, c, f(c));

        if (fabs(f(c)) < tol) {
            *root = c;
            break;
        }

        if (f(a) * f(c) < 0) {
            b = c;
        } else {
            a = c;
        }
    }

    return c;
}

void save_function_data(const char *filename, double a, double b, int points) {
    FILE *file = fopen(filename, "w");
    if (!file) {
        printf("Error: Tidak bisa membuka file untuk menyimpan data.\n");
        return;
    }

    double step = (b - a) / points;
    for (double x = a; x <= b; x += step) {
        fprintf(file, "%.5f %.5f\n", x, f(x));
    }

    fclose(file);
}

void plot_graph(const char *data_filename, double root) {
    FILE *gnuplot = popen("gnuplot -persist", "w");
    if (!gnuplot) {
        printf("Error: Tidak bisa membuka GNUplot.\n");
        return;
    }

    fprintf(gnuplot, "set title 'Grafik Fungsi dan Titik Akar'\n");
    fprintf(gnuplot, "set xlabel 'x'\n");
    fprintf(gnuplot, "set ylabel 'f(x)'\n");
    fprintf(gnuplot, "plot '%s' with lines title 'f(x)', \\\n", data_filename);
    fprintf(gnuplot, " '-' with points pointtype 7 title 'Akar'\n");
    fprintf(gnuplot, "%.5f %.5f\n", root, f(root));
    fprintf(gnuplot, "e\n");
    fprintf(gnuplot, "set grid\n");
    fprintf(gnuplot, "replot\n");

    pclose(gnuplot);
}

int main() {
    double a = 2.0, b = 3.0;
    double tol = 1e-6;
    int max_iter = 100;
    double root;

    bolzano_method(a, b, tol, max_iter, &root);

    if (!isnan(root)) {
        printf("\nAkar yang ditemukan: %.6f\n", root);

        save_function_data("function_data.txt", a, b, 400);
        plot_graph("function_data.txt", root);
    }

    return 0;
}
