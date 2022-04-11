#include <stdio.h>
#include <math.h>

float y_coords(float x)  {
return x*x;
}

float x_coords(float a, float b, float c)  {

    static int counter = 0;
    float disc = b*b - 4*a*c;

    if(counter == 0) {
        counter++;
        return (-b - sqrt(disc))/2*a;
    } else return (-b + sqrt(disc))/2*a;
    
}

int main()  {

    float a = 1, b = 1, c = -2;               //solving ax^2 + bx + c = 0
    float x1, x2; 

    x1 = x_coords(a,b,c);
    x2 = x_coords(a,b,c);

    float y1 = y_coords(x1), y2 = y_coords(x2);

    printf("The points of intersection are (%.0f,%.0f) and (%.0f,%.0f)\n",x1,y1,x2,y2);

return 0;
}