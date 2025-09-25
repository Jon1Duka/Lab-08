kategori = input("Kategori: ").lower()
sasia = int(input("Sasia: "))
karte = input("Ke karte studenti? (po/jo): ").lower()

match kategori:
    case "supa": cmimi = 120
    case "sallate": cmimi = 150
    case "pasta": cmimi = 220
    case "embelsire": cmimi = 180
    case _: 
        print("Kategori e pavlefshme")
        exit()

nenshuma = cmimi * sasia
zbritje = 0

if karte == "po":
    zbritje += 10
if sasia >= 5:
    zbritje += 5

vlera_zbritje = round(nenshuma * zbritje / 100, 2)
totali = round(nenshuma - vlera_zbritje, 2)

print("\n------------------------------")
print(f"Artikulli: {kategori} ({cmimi} Lek)")
print(f"Sasia: {sasia}")
print(f"Zbritje totale: {zbritje}% (Vlera: {vlera_zbritje} Lek)")
print(f"Nën-total: {nenshuma} Lek")
print(f"Totali: {totali} Lek")
