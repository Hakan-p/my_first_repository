def huvudmeny():
    print("*******************************************")
    print("*******************************************")
    print("*****                               *******")
    print("** Välkommen till Todo list extravaganza **")
    print("****                                 ******")
    print("******   Alternativ    ********************")
    print(" 1. Se innehållet i din lista              ")
    print(" 2. Lägga till nya punkter i din lista     ")
    print(" 3. Markera som klar i din lista           ")
    print(" 4. Lägga till nya punkter i din lista     ")
    print(" 5. Lämna programmet                       ")
    print("*******************************************")
    print("*******************************************") 
import os
os_type = os.name  # Kan vara 'posix', 'nt', eller 'os2', beroende på operativsystemet
if os_type == 'posix':
    #("Detta är ett Unix-liknande OS (t.ex. Linux eller macOS)")
    ostyp = "clear" 
elif os_type == 'nt':
    #("Detta är Windows")
    ostyp ="cls"
else:
    print("Okänt operativsystem")
os.system(ostyp)
lista =[]
lista_borttagna=[]
list_item =""
alt =""
list_item_bort =""
huvudmeny()
while alt !="5":
    alt = input ("Välj ett alternativ :") 
    if alt == ("1"):
        os.system(ostyp)
        print("Du har valt att se innhehållet i din listal")
        print(lista)
        input("Tryck på Enter för att fortsätta...")
        os.system('clear')
        huvudmeny()
    elif alt == ("2"):
        os.system(ostyp)
        print("Du har valt att lägga till innhehållet i din listal")
        list_item =input("Varsågod och börja nu kan du lägga in i din lista :")
        lista.append(list_item)
        os.system(ostyp)
        huvudmeny()
    elif alt ==("3"):
        os.system(ostyp)
        print(lista)        
        list_item_bort = input("Vilken grej är du färdig med ?")
        lista.remove(list_item_bort)
        lista_borttagna.append(list_item_bort)
        os.system('clear')
        huvudmeny()
    elif alt ==("4"):
        os.system('clear')
        print(lista_borttagna)
        list_item_ater = input("Vilken grej vill du lägga tillbaka i listan ?")
        lista_borttagna.remove(list_item_ater)
        lista.append(list_item_ater)
        os.system(ostyp)
        huvudmeny()
    else:
        os.system(ostyp)
        if alt !="5":
            print("Du har gjort ett felaktigt alternativ !!")
            input("Tryck på Enter för att fortsätta...")
            os.system(ostyp)
            huvudmeny()
        else:      
            alt ="5"
            print("Du har valt att avsluta")   
                   
print(f"listan innehåller nedanstående element {lista}")
