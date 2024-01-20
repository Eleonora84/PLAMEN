print("Dobre doshli v programata koqto moje da presmqta lice i obikolka na pravoagalnik ili kvadrat" )

print("Molq zadaite strana a:")
a=int(input())
print("Molq zadaite strana b:")
b=int(input())

if(a==b):
    print("Figurata e kvadrat")
    s=a*b
    o=4*a
else:
    print("Figurata e pravoagalnik") 
    s = a*b
    o = (2*a)+(2*b)

print(f"Liceto e ravno na:", s)
print(f"Obikolkata e ravna na:", o)
