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
os.system('clear')
lista =[]
lista_borttagna=[]
list_item =""
alt =""
list_item_bort =""
huvudmeny()
while alt !="5":
    alt = input ("Välj ett alternativ :") 
    if alt == ("1"):
        os.system('clear')
        print("Du har valt att se innhehållet i din listal")
        print(lista)
        input("Tryck på Enter för att fortsätta...")
        os.system('clear')
        huvudmeny()
    elif alt == ("2"):
        os.system('clear')
        print("Du har valt att lägga till innhehållet i din listal")
        list_item =input("Varsågod och börja nu kan du lägga in i din lista :")
        lista.append(list_item)
        os.system('clear')
        huvudmeny()
    elif alt ==("3"):
        os.system('clear')
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
        os.system('clear')
        huvudmeny()
    else:
        os.system('clear')
        print("Du har valt att avsluta")   
                   
print(f"listan innehåller nedanstående element {lista}")
