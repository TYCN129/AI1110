#include <stdio.h>
#include <math.h>

float func_value(float x)  {
return x*x;
}

float integral()  {

    float area = 0;
    for(float x = -2; x <= 1; x += 0.001) {
        area += func_value(x)*0.001;
    }

return area;
}

int main()  {

    float A_trapezium = ((4.0 + 1)*3)/2;
    float A_x_2 = integral();

    printf("Area bound by the two curves is %.2f sq.units\n",A_trapezium - A_x_2);

return 0;
}