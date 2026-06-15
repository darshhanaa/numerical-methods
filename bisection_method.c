#include <stdio.h>
#include <math.h>

float f(float x) {
    return x*x*x - x - 2;   // example function
}

int main() {
    float a, b, c;
    int i = 0;

    printf("Enter a and b: ");
    scanf("%f %f", &a, &b);

    if(f(a) * f(b) >= 0) {
        printf("Invalid interval\n");
        return 0;
    }

    do {
        c = (a + b) / 2;

        if(f(c) == 0.0)
            break;
        else if(f(a) * f(c) < 0)
            b = c;
        else
            a = c;

        i++;

    } while(fabs(b - a) >= 0.0001);

    printf("Root = %.4f\n", c);
    printf("Iterations = %d\n", i);

    return 0;
}
