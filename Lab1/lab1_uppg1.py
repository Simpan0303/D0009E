# k = P + (a+1)P*r/2
# k = total kostnad
# P = Lånat belopp
# r = årlig räntesats

p = float(input("Lånat belopp: "))

r = float(input("Årlig räntesats: "))

a = float(input("Antal år för återbetalning: "))  

def kostnad(p, r, a):
    k = p+(a+1)*p*r/2
    print("Den totala kostnaden efter", int(a), "år är:")
    print(int(k))

kostnad(p, r, a)

