#include "../coeffs.h"

int main() {

	FILE *y = fopen("../5.1/Y.dat","r"), *x_cap = fopen("X_cap.dat","w");
	double temp = 0.0;
	while(fscanf(y,"%lf",&temp) != -1) {
		if(temp < 0) fprintf(x_cap,"%lf\n",-1.0);
		else fprintf(x_cap,"%lf\n",1.0);
	}

	fclose(y);
	fclose(x_cap);

return 0;
}
