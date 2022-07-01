#include "../coeffs.h"
#define N pow(10,6)

int main() {
	char str[] = "../1.1/uni.dat";
	printf("Mean is %lf and variance is %lf.\n",mean(str),var(str));
return 0;
}
