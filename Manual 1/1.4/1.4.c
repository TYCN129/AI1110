#include<stdio.h>
#include<math.h>

#define N pow(10,6)

int main() {
        FILE *pfile = fopen("../1.1/uni.dat","r");
        double mean_u, mean_usq, var, rv;

        while(!feof(pfile)) {
                fscanf(pfile,"%lf",&rv);
                mean_u += (rv/N);
                mean_usq += (rv*rv/N);
        }

        var = mean_usq - mean_u*mean_u;
        printf("%lf and %lf\n",mean_u,var);

        fclose(pfile);

return 0;
}
