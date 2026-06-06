running = True

def lista_filmow():
    with open ('Filmy.txt', 'r') as f:
        filmy = f.read()
    filmy = filmy.splitlines()
    print("\n---Lista filmow---")
    for numer, film in enumerate(filmy, start=1):
        print(f"{numer}. {film}")
    return filmy

def daj_ocene():
    ocena = int(input("-> Wpisz jaka chcesz dac ocene (1-10): "))
    if 1 > ocena > 10:
        print("Nieprawidlowy numer!")
    print(f"Dales filmowi {filmy[nr - 1]} ocene {ocena}/10")
    filmy[nr - 1] = filmy[nr - 1] + f" | {ocena}/10"
    with open('filmy.txt', 'w') as f:
            for film in filmy:
                f.write(film + "\n")
    return ocena    

def zmien_ocene():
    nr = int(input("-> Wpisz numer filmu, ktoremu chcesz zmienic ocene: "))
    if 1 <= nr <= len(filmy):
        nazwa = filmy[nr - 1].split(" | ")[0]
        ocena = int(input("-> Wpisz jaka chcesz dac ocene (1-10): "))
        if 1 > ocena > 10:
            print("Nieprawidlowy numer!")
        nazwa = nazwa + f" | {ocena}/10"
        filmy[nr - 1] = nazwa
        with open('filmy.txt', 'w') as f:
            for film in filmy:
                f.write(film + "\n")
        
    else:
        print("Nieprawidlowy numer!")

while running:
    menu = ("---Menu---\n"
    "1. Dodaj film\n"
    "2. Pokaż filmy\n"
    "3. Usuń film\n"
    "4. Dodaj ocenę\n"
    "5. Zmien ocenę\n"
    "6. Usun ocenę\n"
    "7. Wyjdź")
    print("\n" + menu)

    wybor = input("---> ")
    
    if wybor == "1":
        film = input("Dodaj film, który obejrzałeś: \n")

        with open ('Filmy.txt', 'a') as f:
            f.write (film + "\n")
        print (f"Dodano film {film} do listy")

    elif wybor == "2":
        lista_filmow()

    elif wybor == "3":
        filmy = lista_filmow()

        nr = int(input("-> Wpisz numer filmu, ktory chcesz usunac: "))
        if 1 <= nr <= len(filmy):
            usuniety = filmy.pop(nr - 1)
            with open('filmy.txt', 'w') as f:
                for film in filmy:
                    f.write(film + "\n")
            print(f"Usunieto film {usuniety}")
        else: 
            print("Nieprawidlowy numer!")

    elif wybor == "4":
        filmy = lista_filmow()

        nr = int(input("-> Wpisz numer filmu, ktory chcesz ocenic: "))
        if 1 > nr > len(filmy):
            print("Nieprawidlowy numer!")
        if " | " in filmy[nr - 1]:
            zmiana = input('Ten film ma juz ocene. Jesli chcesz ja zmienic, napisz "tak": ')
            if zmiana == "tak":
                zmien_ocene()
            else:
                continue
        elif " | " not in filmy[nr - 1]:
            ocena = daj_ocene()


    elif wybor == "5":
        filmy = lista_filmow()

        zmien_ocene()

    elif wybor =="6":
        filmy = lista_filmow()

        nr = int(input("-> Wpisz numer filmu, ktoremu chcesz usunac ocene: "))
        if 1 <= nr <= len(filmy):
            nazwa = filmy[nr - 1].split(" | ")[0]
            filmy[nr - 1] = nazwa
            with open('filmy.txt', 'w') as f:
                for film in filmy:
                    f.write(film + "\n")
            
        
    elif wybor == "7":
        print("Do widzenia!")
        running = False

    else:
        print("Niepoprawny wybór. Spróbuj jeszcze raz\n")
