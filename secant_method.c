#include <stdio.h>
#include <math.h>

float f(float x) {
    return x*x*x - x - 2;   // example function
}

int main() {
    float x0, x1, x2;
    int i = 0;

    printf("Enter x0 and x1: ");
    scanf("%f %f", &x0, &x1);

    do {
        if(f(x1) - f(x0) == 0) {
            printf("Division by zero error\n");
            return 0;
        }

        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0));

        x0 = x1;
        x1 = x2;

        i++;

    } while(fabs(f(x2)) >= 0.0001);

    printf("Root = %.4f\n", x2);
    printf("Iterations = %d\n", i);

    return 0;
}
