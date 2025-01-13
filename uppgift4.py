# Ange hur långt du ska köra 
while True:
   try:
       avstand = input("Hur långt ska du köra ange i km :")
       if avstand == "":
          print("Du måste ange ett värde")   
          continue
       avstand = int(avstand)
       break # Om omvandlingen lyckas, gå vidare till nästa steg  
   except ValueError:
    print("Ogiltig inmatning! Vänligen ange ett giltigt heltal för avstand.")

# Ange hur fort du kör i km/h 
while True:
   try:
       hastighet = input("Hur fort kör du ange i km/h :")
       if hastighet == "":
          print("Du måste ange ett värde")   
          continue
       hastighet = int(hastighet)
       break # Om omvandlingen lyckas, gå vidare till nästa steg  
   except ValueError:
    print("Ogiltig inmatning! Vänligen ange ett giltigt heltal för avstand.")
   # Beräkna hurlång tid resan tar

if  hastighet != 0 and avstand !=0 :
  # Beräkna i timmar och minuter
  restid =  (avstand // hastighet)
  minuter = avstand % hastighet / hastighet
  minuter = int(minuter*60)
  print(f"Det tar {restid} timmar ")
  print(f"och {minuter} minuter")
  # Beräkna i minuter
  
  print(f"Restid omvandlat till {(restid * 60) + minuter} minuter")
  # Beräkna i sekunder
  print(f"Restid omvandlat till {((restid * 60) + minuter) * 60} sekunder")

else:
  print(f"Resan har inte startat än")

      
               