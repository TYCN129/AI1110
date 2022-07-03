#include<stdio.h>
#include<math.h>
#include<stdlib.h>

#define N pow(10,6)

int main() {
	FILE *pfile=fopen("Y.dat","w");
	for(int i = 0; i < N; i++) {
		double random = rand() > (double)RAND_MAX/2 ? 0.5 : -0.5;
		double temp = 0.0;
		for(int j = 0; j < 12; j++) {
			temp += (double)rand()/RAND_MAX;
		}
		temp -= 6;
		fprintf(pfile,"%lf\n",temp + random);
	}
	fclose(pfile);

return 0;
}
