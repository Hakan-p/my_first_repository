# Programmet beräknar priset på en vara med visst avdrag
while True:
    try:
        pris = input("Hur mycket kostar varan? :")
        if pris == "":
            print("Du måste ange ett pris!")
            continue  # Om input är tom, fråga igen

        pris = int(pris)  # Försök omvandla till heltal
        break  # Om omvandlingen lyckas, gå vidare till nästa steg
    except ValueError:
        print("Ogiltig inmatning! Vänligen ange ett giltigt heltal för priset.")

# Rabattinmatning
while True:
    try:
        rabatt = input("Hur mycket rabatt på varan? :")
        if rabatt == "":
            rabatt = 0  # Om inget anges, sätt rabatt till 0
            break

        rabatt = int(rabatt)  # Försök omvandla till heltal
        break  # Om omvandlingen lyckas, gå vidare
    except ValueError:
        print("Ogiltig inmatning! Vänligen ange ett giltigt heltal för rabatten.")

# Beräkning och utskrift av priset
if rabatt != 0:
    nytt_pris = pris - (pris * rabatt / 100)
    print(f"Varan kostar {nytt_pris:.2f} kronor efter {rabatt}% rabatt.")
else:
    print(f"Varan kostar {pris} kronor.")