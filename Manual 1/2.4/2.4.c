#include<stdio.h>
#include<math.h>

#define N pow(10,6)

int main() {
	FILE *pfile = fopen("../2.1/gau.dat","r");
	double mean_x, mean_xsq, var, rv;

	while(!feof(pfile)) {
		fscanf(pfile,"%lf",&rv);
		mean_x += (rv/N);
		mean_xsq += (rv*rv/N);
	}
	
	var = mean_xsq - mean_x*mean_x;
	printf("%lf and %lf\n",mean_x,var);

	fclose(pfile);

return 0;
}
