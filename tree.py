from FractalWorld import *

world = FractalWorld(width=1000,height=600,delay=0)
bob = Fractal()
print bob
bob.set_delay(0)

def test(t,l,n,a):
    if n == 0:
        return
    fd(t,l)
    lt(t,a)
    test(t,l/1.5,n-1)
    lt(t,180-a*2)
    test(t,l/1.5,n-1)
    lt(t,a)
    fd(t,l)

lt(bob,90)

print test(bob,75,13,30)

wait_for_user()
