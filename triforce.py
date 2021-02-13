from FractalWorld import *

world = FractalWorld(width=1000,height=500,delay=0)
bob = Fractal(draw=False)
print bob

#base funktion
def tri(t,l,n):
    a = 60
    fd(t,l)
    lt(t,a*2)
    fd(t,l)
    rt(t,a*2)
    fd(t,l)
    rt(t,a*2)
    fd(t,l)
    lt(t,a*2)
    fd(t,l)
    lt(t,a*2)
    fd(t,l*2)
    lt(t,a*2)
    fd(t,l*2)
    lt(t,a*2)
    fd(t,l*2)

def triforce(t,l,n):
    a = 60
    if n == 0:
        tri(t,l,n)
        return
    triforce(t,l/2.0,n-1)
    lt(t,a*2)
    fd(t,l)
    rt(t,a*2)
    triforce(t,l/2.0,n-1)
    rt(t,a*2)
    fd(t,l)
    lt(t,a*2)
    triforce(t,l/2.0,n-1)
    
    

print triforce(bob,150,5)

wait_for_user()
