import math
print("Presmqtane na lice i obikolka na geometricni figuri")
print("Izbere fugurata :")

print("1 - kvadrat")
print("2 - pravougalnik")
print("3 - triugalnik")
print("4 - okruznost")
vstup = int(input("Izbiram:"))
match vstup:
    case 1:
        print("Figurata e kvadrat") 
        a = int(input("Molq zadajte daljina stara : "))
        s = a * a
        o = 4 * a
        print(f"Liceto e ravno na:", s )
        print(f"Obikolkata e ravna na:", o )
    case 2: 
        print("Figurata e pravougalnik") 
        a = int(input("Molq zadajte daljina stara a: "))
        b = int(input("Molq zadajte daljina stara b: "))
        s = a * b
        o = (2*a)+(2*b)
        print(f"Liceto e ravno na:", s )
        print(f"Obikolkata e ravna na:", o )
    case 3:
        print("Figurata e triugalnik")
        a = int(input("Molq zadajte daljina stara a: "))
        b = int(input("Molq zadajte daljina stara b: "))
        c = int(input("Molq zadajte daljina stara c: "))
        p =(a + b + c) / 2
        o = p * 2
        s = (p - a) * (p - b) * (p - c) * p
        s = (math.sqrt(s))
        print(f"Liceto e ravno na:", s )
        print(f"Obikolkata e ravna na:", o )
        
          
    case 4:
        print("Figurata e okruznost")
        r = int(input("Molq zadajte radius: "))
        pi = 3.14
        s = pi * (r * r)
        o = 2 * (pi * r)
        print(f"Liceto e ravno na:", s )
        print(f"Obikolkata e ravna na:", o )
    case _:
        print("Nesastestvuvasta figura")   
        
        
         
    
    
        
        
    
     
    



