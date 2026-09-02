'''
1st sockerkaka

Till formen:
ca 15 g smör
ca 3 msk ströbröd

Sockerkaka:

3 st ägg
3 dl strösocker
2 tsk vaniljsocker
2 tsk bakpulver
3 dl vetemjöl
75 g smör
1 dl vatten

1 sockerkaka är lämplig för 4 pers, enligt uppgiften. Detta ger 3 bitar/person
'''

people_amount = int(input("Hur många personer ska du baka sockerkaka till? "))

# Deluppgift 1
# Tiden det tar att blanda smeten
def tidblanda(people_amount):
    t = 10 + 1*(people_amount)
    # Om vi gör sockerkaka för 0 personer tillagar vi 0 ingredienser, 
    # i vilket fall det varken behövs blandas eller gräddas.
    if people_amount < 1:
        return 0
    return t

# Deluppgift 2
# Denna funktion verkar anta att all smet gräddas i samma form,
# Men den tillhör uppgiften, så... Samma struktur som deluppgift 1 iaf.
def tidgradda(people_amount):
    t = 30 + 3*people_amount
    if people_amount < 1:
        return 0
    return t

# Deluppgift 3
def sockerkaka(people_amount):
    # Kvot baserad på antal människor som varje ingrediens 
    # ska multipliceras med
    kvot = float(people_amount/4)

    # Delar upp printoutet till en "kolumn" ingredienser
    print("\nRecept för", people_amount, "personer:\n", 
          "Till formen:\n",
          15*kvot, "g smör\n",
          3*kvot, "msk ströbröd\n\n",

          "Till sockerkakan:\n",
          round(3*kvot), "st ägg\n",
          3*kvot, "dl strösocker\n",
          2*kvot, "tsk vaniljsocker\n",
          2*kvot, "tsk bakpulver\n",
          3*kvot, "dl vetemjöl\n",
          75*kvot, "g smör\n",
          1*kvot, "dl vatten")


print("Minuter det tar att blanda smeten:", tidblanda(people_amount))
print("Minuter det tar att grädda smeten:", tidgradda(people_amount))
sockerkaka(people_amount)

# Deluppgift 4
# Skriver ut recept för sockerkakerecept för 4 respektive 7 personer
sockerkaka(4)
sockerkaka(7)

