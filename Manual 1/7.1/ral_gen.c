#include "../coeffs.h"

#define N pow(10,6)

int main(int argc, char *argv[]) {
    char str[] = "ral.dat";
    double gamma = 0;
    sscanf(argv[argc - 1],"%lf",&gamma);
    printf("%lf\n",gamma);
    ral_gen(str,gamma,N);

return 0;
}
