def f(x):
    return x**4-2*x+1
N=20
a=0.0
b=2.0
#20 Slices
h=(b-a)/N
h2=(b-a)/(2*N)
s=.5*f(a)+.5*f(b)
s2=.5*f(a)+.5*f(b)
for k in range(1,N):
    s+=f(a+k*h)
s*=h
#10 Slices
h2=2*(b-a)/(N)
s2=.5*f(a)+.5*f(b)
for k in range(1,int(N/2)):
    s2+=f(a+k*h2)
s2*=h2
S=1/5*(b)**5-b**2+b
print("20 slice " + str(s))
print("10 slice " + str(s2))
print("Actual " + str(S))

print("Actual Error "+str((s-S)))
print("Approx Error "+str((s2-s)/3))