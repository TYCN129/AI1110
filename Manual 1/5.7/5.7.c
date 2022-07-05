#include "../coeffs.h"

int main(int argc, char *argv[]) {

        FILE *y = fopen("y.dat","w"), *gau = fopen("../2.1/gau.dat","r"), *ber = fopen("../5.1/X.dat","r");
        double a, gauss = 0.0, bern = 0.0;
        sscanf(argv[argc - 1],"%lf",&a);
        
        while(fscanf(gau,"%lf",&gauss) != -1) {
                fscanf(ber,"%lf",&bern);
                fprintf(y,"%lf\n",gauss + a*bern);
        }

        fclose(y);
        fclose(ber);
        fclose(gau);

        y = fopen("y.dat","r");
        FILE *x_cap = fopen("x_cap.dat","w");
        double temp = 0.0;

        while(fscanf(y,"%lf",&temp) != -1)
                temp < 0.0 ? fprintf(x_cap,"%d\n",-1) : fprintf(x_cap,"%d\n",1);

        fclose(y);
        fclose(x_cap);

return 0;
}
