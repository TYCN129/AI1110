#include<stdio.h>
#include<math.h>
#include<stdlib.h>

#define N pow(10,6)

int main() {
	FILE *pfile = fopen("X.dat","w");
	for(int i = 0; i < N; i++) {
		double random = rand() > (double)RAND_MAX/2 ? 1 : -1;
		fprintf(pfile,"%lf\n",random);
	}
	fclose(pfile);

return 0;
}
