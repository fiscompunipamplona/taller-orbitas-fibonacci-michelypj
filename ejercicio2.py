#A partir de la segunda ley de Kepler, escriba un programa que calcule la posición y velocidad en el afelio, dada la posición y velocidad en el perihelio.

print("Posición y velocidad en el afelio")

r2=float(input("Digite la posición del perihelio"))
v2=float(input("Digite la velocidad del perihelio"))

pi=3.1416
g=6.67e-11
m=1.989e30

v1=(((2*g*m)/(v2*r2))+(((2*g*m)/(v2*r2))**2+4*((v2**2-2*g*m)/r2))**1/2)/2
r1=(r2*v2)/v1
a=(r2+r1)/2
b=(r2*r1)**(1/2)
T=(2*pi*a*b)/(r2*v2)
ex=(r1-r2)/(r1+r2)

print("Velocidad del afelio:" ,v1)
print("Posición del afelio:" ,r1)
print("Semieje mayor:" ,a)
print("Semieje menor:" ,b)
print("Periodo orbital:", T)
print("Excentricidad orbital:" ,ex)

#Escriba un código que calcule la secuencia de Fibonacci hasta 1000.

print("Serie de Fibonacci")

f1=1
f2=1

print("Serie de fibonacia hasta 1000")
print(f1)
while f2 <= 1000:

        print(f2)
        Fn=f1+f2
        f1=f2
        f2=Fn
