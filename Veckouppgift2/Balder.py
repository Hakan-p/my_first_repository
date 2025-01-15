#Kontroll av om person har rätt längd för att åka Balder
#  
person_length = int(input("Hur lång är du (Ange i cm)"))
print ("Du är ", person_length, "lång")
if person_length >= 130 :
    print("Du får åka Balder")
else:
    print("Du får inte åka Balder")    