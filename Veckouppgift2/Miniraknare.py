# Miniräknare 
# Summera tal1 och tal2 och tal3
tal1 = float(input("Mata in ett tal "))
tal2 = float(input("Mata in ett tal "))
tal3 = float(input("Mata in ett tal "))
summera = tal1+tal2+tal3
print(f"Summan av talen är", {summera})
# Vilket tal är störst
tal1_great = tal1 > tal2 > tal3
tal2_great = tal2 > tal1 and tal2 > tal3
tal3_great = tal3 > tal1 and tal3 > tal2

if tal1_great == True :
    print("tal1 är störst") 
elif tal2_great == True :
    print("tal2 är störst")
elif tal3_great == True :
    print("tal3 är störst")    
# Vilket Tal är Lika
# Vilket Tal är mitterst
box1_mittersta = tal1 > tal2 and tal2 < tal3 and tal1 < tal3  or tal1 < tal2 and tal2 > tal3 and tal1 > tal3
box2_mittersta = tal1 < tal2 and tal2 < tal3 and tal1 < tal3 or tal1 > tal2 and tal2 > tal3 and tal1 > tal3
box3_mittersta = tal1 < tal2 and tal2 > tal3 and tal1 < tal3  or tal1 > tal2 and tal2 < tal3 and tal1 > tal3
tal1_lika_tal2_lika_tal3 = tal1 == tal2 and tal1 == tal3
tal1_lika_tal2 = tal1 == tal2
tal2_lika_tal3 = tal2 == tal3 
tal3_lika_tal1 = tal3 == tal1
if box1_mittersta:
    print("tal1 är det mittersta") 
elif box2_mittersta:
    print("tal2 är det mittersta")
elif box3_mittersta:
    print("tal3 är det mittersta")
elif tal1_lika_tal2_lika_tal3 :
    print("Alla tal är lika")
elif tal1_lika_tal2 == True:
    print("tal1 och tal2 är lika") 
elif tal2_lika_tal3 == True:
    print("tal2 och tal3 är lika")       
elif tal3_lika_tal1 == True:
        print("tal3 och tal1 är lika")

