#include<stdio.h>
#include<math.h>
#include<stdlib.h>

#define N pow(10,6)

int main() {
	FILE *pfile = fopen("gau.dat","w+");
	for(int i = 0; i < N; i++) {
		double sum = 0;
		for(int j = 0; j < 12; j++) {
			sum += ((double)rand()/RAND_MAX);
		}
		fprintf(pfile,"%lf\n",sum - 6);
	}

	fclose(pfile);

return 0;
}
