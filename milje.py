
print("Dobro dosli u program preracunavanja kilometara u milje")
while True:

    km = int(input("Unesite kilometre : "))
    mil = 0.63 * km

    print(mil)
    izbor = input("Ponovo, da ili ne : ")
    if (izbor != "da"):
        break