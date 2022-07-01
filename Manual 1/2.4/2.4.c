#include "../coeffs.h"

#define N pow(10,6)

int main() {
	printf("Mean is %lf and variance is %lf",mean("../2.1/gau.dat"),var("../2.1/gau.dat"));
return 0;
}
