# Programmet låter användaren mata in 2 heltal
# Om användaren matar in något annat än 2 heltal så fortsätter programmet annars bryter det.
loopkod = True
while loopkod is True:
    try :
   
      heltal1 = int(input("Ange ett Heltal :"))
      print ("Du matade in ett heltal", heltal1)
      heltal2 = int(input("Ange ett Heltal :"))
      print ("Du matade in ett heltal", heltal2)
      print ("Summan av de två talen är", heltal1 + heltal2)
      loopkod= False
    except ValueError:
     print("Det var inte ett giltigt heltal som du matade in, försök igen") 
     loopkod = True
   