# Miniräknare 
tal1 = float(input("Mata in ett tal "))
tal2 = float(input("Mata in ett tal "))
tal3 = float(input("Mata in ett tal "))
summera = tal1+tal2+tal3
print(f"Summan av talen är", {summera})
tal1_great = tal1 > tal2 > tal3
tal2_great = tal2 > tal1 and tal2 > tal3
tal3_great = tal3 > tal1 and tal3 > tal2

if tal1_great == True :
    print("tal1 är störst") 
elif tal2_great == True :
    print("tal2 är störst")
elif tal3_great == True :
    print("tal3 är störst")    

tal1_mittersta = tal2 < tal1 and tal1 < tal3
tal2_mittersta = tal1 < tal2 and tal3 > tal2
tal3_mittersta = tal1 < tal3 and tal2 > tal3  or tal1 > tal2 and tal3 > tal2
tal1_lika_tal2_lika_tal3 = tal1 == tal2 and tal1 == tal3
tal1_lika_tal2 = tal1 == tal2
tal2_lika_tal3 = tal2 == tal3 
tal3_lika_tal1 = tal3 == tal1
if tal1_mittersta:
    print("Tal1 är det mittersta") 
elif tal2_mittersta:
    print("Tal2 är det mittersta")
elif tal3_mittersta:
    print("Tal3 är det mittersta")
elif tal1_lika_tal2_lika_tal3 :
    print("Alla tal är lika")
elif tal1_lika_tal2 == True:
    print("Tal1 och tal2 är lika") 
elif tal2_lika_tal3 == True:
    print("Tal2 och tal3 är lika")       
elif tal3_lika_tal1 == True:
        print("Tal3 och tal1 är lika")

