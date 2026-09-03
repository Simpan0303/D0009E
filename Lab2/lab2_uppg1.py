# Labb 2 av Simon Svanberg
# Obs! Varning för myyycket svengelska nedan.

# ------------------------------------------------------------------------------
# Uppgift 1
# Rekursivt bounce
def bounce(number):
    # Skriver det "initiala" number.
    # Varje nummer n hamnar i väntläge medans n-1 anropas
    print(number)

    if number > 0:
        # Rekursionen, dvs "spegeln"
        # ner till 0
        bounce(number - 1)

        # Exekveras i "motsatt ordning" jämfört med print ovan
        # Måste vara i if-satsen för att hamna omedelbart
        # efter/under rekursionen i hierarki (och att 0 skrivs dubbelt)
        print(number) 

# Interaktivt call
# bounce(int(input("Siffra för bounce: ")))
# bounce(5)

"""

bounce(n):
    print(n)
    bounce(n-1)
    print(n)

"""

# ------------------------------------------------------------------------------
# Deluppgift 2
# Iterativt bounce
def bounce2(number):
    # första n
    print(number)

    # temporär "klon" av number för att gå lika stor
    # decrease som increase
    temp = number

    # decrease
    for x in range(temp):
        temp = temp - 1
        print(temp)

    # increase
    for x in range(number):
        temp = temp + 1
        print(temp)

# Interaktivt call
# bounce2(int(input("Siffra för bounce2: ")))


# -------------------------------------------------------------------------------
# Deluppgift 3
# Tvärsumma. Exempel 349 ger 3 + 4 + 9 = 16
# Rekursivt

def tvarsumma(number):
    # printar individuella siffror i ett tal
    digit = number % 10
    # Modulo kapar bort den högraste siffran
    print(digit)

    # Kollar ifall tiotalen tagit slut, i vilket fall den
    # returnerar den högraste siffran utan manipulation
    if (number // 10) == 0:
        return digit
    
    else:
        # digit är från början endast den högraste siffran i ett tal
        # men allt eftersom tvarsumma(n) körs rekursivt med dividering
        # av number i steg av 10-tal (perfa för vårt 10-bas talsystem)
        # så adderas de resulterande "nya högraste" siffrorna till
        # digit. Detta skapar en tvärsumma.
        return digit + tvarsumma(number // 10)

# Interaktivt call bara för att det är coolt sa de
#x_sum = int(input("Ange tal att få tvärsumman från: "))
#print("Tvärsumman blir: ", tvarsumma(x_sum))

# För att vara ärlig råkade jag bara på den här lösningen, funkar najs iaf.

# -------------------------------------------------------------------------------
# Deluppgift 4
# Iterativ tvärsumma
def tvarsumma2(number):
    #print(number)
    #print(number // 10)

    digit = number % 10

    count = 0
    while number:
        count += 1
        number = number // 10
        digit = digit + number % 10

    print("tvärsumma2 är:", digit)

#tvarsumma2(int(input("Ange tal att få tvärsumma från: ")))

# Deluppgift 5a
# Returnerar första derivatan för f(x)
import math
def f(x):
    #print("bruh")
    return x**2
    #return x + 2
    #return math.log(x) #log(x, bas) bas e

def derivative(f, x, h):
    fxh = f(x + h)
    print("f(x) =", fxh)
    print("f'(x) =", (f(x + h) - f(x - h)) / (2*h))
    return((f(x + h) - f(x - h)) / (2*h))
#print("f'(x) =", derivative(f, 5, 1))

# Deluppgift 5b
# solve med Newton-Raphson metoden
# dvs en loop som kollar om differensen mellan x koordinater
# är mindre än h, vilket indikerar lokalt minimum eller maximum
# tangenslinjer med lutning (förstaderivatan) df(x),
def solve(f, x0, h):
    x = float(x0)

    # körs tills beräkningarna är klara
    while True:
        # derivatan av f
        df = derivative(f, x, h)
        # check så att icke tillåten operation inte körs
        if df == 0:
            raise ValueError("Operation not valid. Derivatan = noll")

        # x_new används för att undvika upprepa samma beräkning under samma loop
        x_new = x - f(x) / df
        # själva checken om differensen mellan x_new och x är mindre än h
        if abs(x_new - x) < h:
            # om ja är beräkningen klar, varpå loopen avlsutas och värdet returneras
            return float(x_new)
        # om nej, fortsätt loopen
        x = x_new

# f är den matematiska funktionen
# x0 är den initiala gissningen. Ju närmare x0 är f(x)=0, 
# desto färre ggr körs loopen i funktionen
# h, ("höjden") är ett litet steg antingen höger (x+h) elr vänster (x-h),
# dessutom gäller: mindre h, större precision på f(x)=0
print(solve(f, 5, 1))