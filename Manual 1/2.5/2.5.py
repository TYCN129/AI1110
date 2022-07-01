Last login: Fri Jul  1 10:02:53 on ttys001
vedantabhandare@Vedantas-MacBook-Air ~ % cd desktop/ai1110/code1
vedantabhandare@Vedantas-MacBook-Air code1 % mkdir 2.3
mkdir: 2.3: File exists
vedantabhandare@Vedantas-MacBook-Air code1 % ls
1.1	1.2	1.3	1.4	2.1	2.2	2.3	2.4	2.5	3.1
vedantabhandare@Vedantas-MacBook-Air code1 % ls 2.3
2.3.py
vedantabhandare@Vedantas-MacBook-Air code1 % cd 2.3
vedantabhandare@Vedantas-MacBook-Air 2.3 % cat 2.3.py
import numpy as np
import matplotlib.pyplot as plt

N = 10**6

X = np.loadtxt("../2.1/gau.dat",dtype='double')
x = np.linspace(-6,6,50)

cdf = []
pdf = []

def gauss_pdf(x):
	return(1/np.sqrt(2*np.pi))*np.exp(-(x**2/2))

for i in range(0,50):
	cdf.append(np.size(np.nonzero(X < x[i]))/N)

for i in range(0,49):
	pdf.append((cdf[i+1] - cdf[i])/(x[i+1] - x[i]))

plt.plot(x,gauss_pdf(x),label="Theory",color="orange")
plt.scatter(x[0:49],pdf,label="Numerical")
plt.grid()
plt.legend()
plt.show()
vedantabhandare@Vedantas-MacBook-Air 2.3 % python3 2.3.py 
vedantabhandare@Vedantas-MacBook-Air 2.3 % vim 2.3.py
vedantabhandare@Vedantas-MacBook-Air 2.3 % python3 2.3.py
No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.
vedantabhandare@Vedantas-MacBook-Air 2.3 % vim 2.3.py    
vedantabhandare@Vedantas-MacBook-Air 2.3 % python3 2.3.py
No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.
vedantabhandare@Vedantas-MacBook-Air 2.3 % python3 2.3.py
No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.
vedantabhandare@Vedantas-MacBook-Air 2.3 % cat 2.3.py    
import numpy as np
import matplotlib.pyplot as plt

N = 10**6
pts = 100

X = np.loadtxt("../2.1/gau.dat",dtype='double')
x = np.linspace(-6,6,pts)

cdf = []
pdf = []

def gauss_pdf(x):
	return(1/np.sqrt(2*np.pi))*np.exp(-(x**2/2))

for i in range(0,pts):
	cdf.append(np.size(np.nonzero(X < x[i]))/N)

for i in range(0,pts-1):
	pdf.append((cdf[i+1] - cdf[i])/(x[i+1] - x[i]))

plt.plot(x,gauss_pdf(x))
#plt.scatter(x[0:pts-1],pdf,label="Numerical")
plt.grid()
plt.legend()
plt.show()
vedantabhandare@Vedantas-MacBook-Air 2.3 % vim 2.3.py
vedantabhandare@Vedantas-MacBook-Air 2.3 % python3 2.3.py
vedantabhandare@Vedantas-MacBook-Air 2.3 % vim 2.3.py    
vedantabhandare@Vedantas-MacBook-Air 2.3 % python3 2.3.py
vedantabhandare@Vedantas-MacBook-Air 2.3 % cd ../2.4
vedantabhandare@Vedantas-MacBook-Air 2.4 % ls
2.4.c	run
vedantabhandare@Vedantas-MacBook-Air 2.4 % cat 2.4.c
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
vedantabhandare@Vedantas-MacBook-Air 2.4 % ls
2.4.c	run
vedantabhandare@Vedantas-MacBook-Air 2.4 % ./run
0.000629 and 1.000150
vedantabhandare@Vedantas-MacBook-Air 2.4 % ./run
-288268077133759909031474239399487297706242960358730507194651874911927001574958166078355853698227899072331961262980990797648966141496982872282862597456265216.000000 and -inf
vedantabhandare@Vedantas-MacBook-Air 2.4 % ./run
0.000629 and 1.000150
vedantabhandare@Vedantas-MacBook-Air 2.4 % ./run
-14859984266170633461867108734345137779519320035232955486655486042973441540961239965865172221143114482110727486800345372597907728108460276338339475504148178842384454385664.000000 and -inf
vedantabhandare@Vedantas-MacBook-Air 2.4 % ./run
0.000629 and 1.000150
vedantabhandare@Vedantas-MacBook-Air 2.4 % cd ../2.3
vedantabhandare@Vedantas-MacBook-Air 2.3 % ls
2.3.py		Figure_2.3.png	a.png
vedantabhandare@Vedantas-MacBook-Air 2.3 % vim 2.3.py 
vedantabhandare@Vedantas-MacBook-Air 2.3 % vim 2.3.py

import numpy as np
import matplotlib.pyplot as plt

N = 10**6
pts = 60

X = np.loadtxt("../2.1/gau.dat",dtype='double')
x = np.linspace(-6,6,pts)

cdf = []
pdf = []

def gauss_pdf(x):
        return(1/np.sqrt(2*np.pi))*np.exp(-(x**2/2))

for i in range(0,pts):
        cdf.append(np.size(np.nonzero(X < x[i]))/N)

for i in range(0,pts-1):
        pdf.append((cdf[i+1] - cdf[i])/(x[i+1] - x[i]))

plt.plot(x,gauss_pdf(x),color="orange",)
plt.scatter(x[0:pts-1],pdf,label="Numerical")
plt.grid()
plt.legend()
plt.show()
