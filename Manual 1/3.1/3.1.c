#include<stdio.h>
#include<math.h>
#include<stdlib.h>

#define N pow(10,6)

int main() {
        FILE *pfile = fopen("v.dat","w+");
        for(int i = 0; i < N; i++) {
                double u = (double)rand()/RAND_MAX;
                double v = -2*log(1 - u);
                fprintf(pfile,"%lf\n",v);
        }

        fclose(pfile);

return 0;
}
