import math

def quadratic_solve(a,b,c):
    disc = b**2 - 4*a*c

    if disc < 0:
        print("The curves do not intersect")
    elif disc == 0:
        x = -b/2*a
        y = x**2
        print("The curves intersect at a unique point ({},{})" .format(x,y))
    elif disc > 0:
        x1 = (-b - math.sqrt(disc))/2*a
        x2 = (-b + math.sqrt(disc))/2*a
        y1 = x1**2
        y2 = x2**2
        print("The curves intersect at two distinct points ({},{}) and ({},{})" .format(x1,y1,x2,y2))

# the quadratic is x**2 + x - 2 = 0
quadratic_solve(1,1,-2)