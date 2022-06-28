#include<stdio.h>
#include<math.h>
#include<stdlib.h>

#define N pow(10,6)

int main() {
	
	FILE *pfile = fopen("uni.dat","w+");
	for(int i = 0; i < N; i++) {
		double x = (double)rand()/RAND_MAX;
		fprintf(pfile,"%f\n",x);
	}

return 0;
}
