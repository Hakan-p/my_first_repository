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