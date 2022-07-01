#include "../coeffs.h"
#define N pow(10,6)

double var(char *str) {
        int i=0,c;
        FILE *fp;
        double x, temp=0.0;

        fp = fopen(str,"r");
//get numbers from file
        while(fscanf(fp,"%lf",&x)!=EOF)
        {
//Count numbers in file
                i=i+1;
//Add all numbers in file
                temp = temp+(x*x);
        }
        fclose(fp);
        temp = temp/(i-1);
        return temp - mean(str)*mean(str);
}

int main() {
        char str[] = "../1.1/uni.dat";
        printf("Mean is %lf and variance is %lf.\n",mean(str),var(str));
return 0;
}
