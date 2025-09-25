pike = int(input("Pike: "))
if 90 <= pike <= 100:
    print("Niveli: Shkelqyeshem")
elif 80 <= pike < 90:
    print("Niveli: Shume mire")
elif 70 <= pike < 80:
    print("Niveli: Mire")
elif 50 <= pike < 70:
    print("Niveli: Kalues")
elif 0 <= pike < 50:
    print("Niveli: Dobet")
else:
    print("Vlerë e pavlefshme")


cmimi = float(input("Cmimi: "))
if cmimi < 100:
    print("Etiketa: I lirë")
elif 100 <= cmimi < 500:
    print("Etiketa: Mesatar")
elif cmimi >= 500:
    print("Etiketa: I shtrenjtë")
else:
    print("Vlerë e pavlefshme")
