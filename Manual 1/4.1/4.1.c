#include "../coeffs.h"

#define N pow(10,6)

void triangular(char *str, int len)
{
int i;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
fprintf(fp,"%lf\n",(double)rand()/RAND_MAX + (double)rand()/RAND_MAX);
}
fclose(fp);
}

int main() {
        char str[] = "tri.dat";
        triangular(str,N);

return 0;
}
