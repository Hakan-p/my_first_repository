temp_typ  = input("Ange om du väljer Farenheit (F)eller Celsius (C)")
temp_grad = float(input("Ange grad "))
if temp_typ == "F":
    celsius = (temp_grad - 32)/1.8
    print(celsius)
elif temp_typ == "C":
    fahrenheit = (1.8 * temp_grad) + 32
    print(fahrenheit)
else:
    print("Du har inte något val!")
if (temp_typ == "C" and temp_grad < 10) or (temp_typ == "F" and celsius < 10 ):
    print("Ta på dig vinterkläder!")
elif (temp_typ == "C" and temp_grad >= 20) or ( temp_typ == "F" and celsius >= 20):        
    print("Packa badkläder!")