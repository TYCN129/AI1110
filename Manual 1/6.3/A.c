#include "../coeffs.h"

#define N pow(10,6)

int main() {
	
	FILE *v = fopen("../6.1/v.dat","r"), *a = fopen("a.dat","w");
	double temp = 0.0;
	while(fscanf(v,"%lf",&temp) != -1) {
		fprintf(a,"%lf\n",sqrt(temp));
	}
	
	fclose(v);
	fclose(a);

return 0;
}
