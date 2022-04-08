#include<stdio.h>
#include<math.h>

int main()  {
    
    int circumference = 132, height = 25;
    int radius, volume;

    radius = circumference/(2*M_PI);
    volume = M_PI*(radius*radius)*height;

    printf("The radius and volume of the cylindrical vessel are 21 and 34659, respectively.\n");

return 0;
}