rabotniDni = int(input())
izkariPariNaDen = float(input())
dolarLev = float(input())


mesecnaZaplata = rabotniDni * izkariPariNaDen
godisenDohod = mesecnaZaplata * 12 + mesecnaZaplata * 2.5
tax = godisenDohod * 0.25
cistDohod = godisenDohod - tax
salaryInLeva = cistDohod * dolarLev

print(round(salaryInLeva /365,2))
