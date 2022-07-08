Last login: Fri Jul  8 08:33:15 on console
vedantabhandare@Vedantas-MacBook-Air ~ % cd desktop/ai1110/code1
vedantabhandare@Vedantas-MacBook-Air code1 % ls
1.1		1.4		2.3		3.1		4.2		5.1		5.4		6.1		test.py
1.2		2.1		2.4		3.2		4.3		5.2		5.6		6.3
1.3		2.2		2.5		4.1		4.5		5.3		5.7		coeffs.h
vedantabhandare@Vedantas-MacBook-Air code1 % vim coeffs.h





































for (j = 0; j < 12; j++)
{
temp += (double)rand()/RAND_MAX;
}
temp-=6;
fprintf(fp,"%lf\n",temp);
}
fclose(fp);

}
//End function for generating Gaussian random numbers

//Defining function for generating Chi_sq random numbers
void chi_gen(char *str, int len)
{
    FILE *fp = fopen(str, "w");
    int j;
    double v;
    double x1, x2;

    for (int i = 0; i < len; i++)
    {
        x1 = 0;
        for (j = 0; j < 12; j++)
        {
            x1 += (double)rand() / RAND_MAX;
        }
        x1 -= 6;
        x2 = 0;
        for (j = 0; j < 12; j++)
        {
            x2 += (double)rand() / RAND_MAX;
        }
        x2 -= 6;

        v = x1 * x1 + x2 * x2;

        fprintf(fp, "%lf\n", v);
    }
    fclose(fp);
}
//End function for generating Chi_sq random numbers
