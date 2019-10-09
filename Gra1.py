from time import sleep
from random import randint

game_running = True

while game_running == True:
    player = {"name": "Player", "attack": 10, "crit": 15, "heal": 16, "health": 100, "mana": 100}

    counter = 0

    print("-----------------------")
    print("    TEXT: THE GAME")
    print("-----------------------")
    sleep(2)
    print("-----------------------")
    print("         Menu")
    print("-----------------------")
    print("Witaj w grze")
    print("1) Pojedynek!")
    print("2) Nowa przygoda!")
    print("3) Opcje")
    print("4) Wyjdź z gry")
    print("-----------------------")

    player_choice1 = input()
    if player_choice1 == "3":
        monster = {"name": "Monster", "max_attack": 20, "min_attack": 10, "health": 100}
        print("1) Poziom trudności")
        print("2) Soon")
        player_choice2 = input()
        if player_choice2 == "1":
            print("1) Poziom łatwy")
            print("2) Poziom normalny")
            print("3) Poziom trudny")
            wybor2 = input()
            if wybor2 == "1":
                pass
            elif wybor2 == "2":
                monster["health"] = 150
            elif wybor2 == "3":
                monster["health"] = 200
                print(monster["health"])
            else:
                print("Nieznana komenda")

    if player_choice1 == "1":
        new_round = True

        print("-----------------------")
        print("Wybierz postać:")
        sleep(0.5)
        print("1) Rycerz")
        sleep(0.5)
        print("2) Berserker")
        sleep(0.5)
        print("3) Mag")
        print("-----------------------")
        wybor = input()
        if wybor == "1":
            pass
        if wybor == "2":
            player["attack"] = 20
            player["heal"] = 8
            player["health"] = 65
        if wybor == "3":
            player["attack"] = 25
            player["health"] = 60

        while new_round == True:
            counter = counter + 1
            player_won = False
            monster_won = False
            print("-----------------------")
            print("Wybierz akcje!: ")
            sleep(1)
            print("1) Atak")
            print("2) Uleczenie")
            if wybor == "3":
                print("3) Wypij potion na mane")
            print("5) Wyjdź do menu")
            print("-----------------------")

            miss_attack2 = randint(1, 10)
            crit_chance = randint(1, 10)

            player_choice = input()
            if player_choice == "1":

                if wybor == "3":
                    if player["mana"] <= 0:
                        print("Masz za malo many!")
                        print(player["mana"])
                    else:
                        player["mana"] = player["mana"] - 25
                        print("Zostalo ci: " + str(player["mana"]) + "% many")
                        monster["health"] = monster["health"] - player["attack"]
                        print("Zadałeś obrażenia równe: " + str(player["attack"]) + "HP")
                        print("Potworowi zostało: " + str(monster["health"]) + "HP")
                else:
                    if crit_chance < 3:

                        print("Critical attack!")
                        monster["health"] = monster["health"] - player["crit"]
                        print("Zadałeś obrażenia równe: " + str(player["crit"]) + "HP")
                        print("Potworowi zostało: " + str(monster["health"]) + "HP")

                    elif miss_attack2 < 3:
                        print("Spudłowałeś")
                        print("Zadałeś obrażenia równe: 0HP")
                        print("Potworowi zostało: " + str(monster["health"]) + "HP")

                    else:
                        monster["health"] = monster["health"] - player["attack"]
                        print("Zadałeś obrażenia równe: " + str(player["attack"]) + "HP")
                        print("Potworowi zostało: " + str(monster["health"]) + "HP")

                if monster["health"] <= 0:
                    player_won = True

                monster_attack = randint(monster["min_attack"], monster["max_attack"])
                miss_attack = randint(1, 10)

                if miss_attack < 3:
                    monster_attack = 0
                    print("Potwór spudłował")
                player["health"] = player["health"] - monster_attack

                if player["health"] <= 0:
                    monster_won = True
                print("Potwór zadał ci: " + str(monster_attack)+"HP")
                print("Zostało ci: " + str(player["health"])+"HP")

                if monster["health"] <= 0:
                    print("-----------------------")
                    print("Wygrałes!")
                    print("Ilość rund: " + str(counter))
                    print("-----------------------")

                if player["health"] <= 0:
                    print("-----------------------")
                    print("Potwór wygrał!")
                    print("Ilość rund: " + str(counter))
                    print("-----------------------")
            elif player_choice == "2":
                        if wybor == "3":
                            if player["health"] <= 44:
                                player["health"] = player["health"] + player["heal"]
                                print("Uleczyłeś się! Twoje zycie wynosi: " + str(player["health"]) + "HP")

                            else:
                                player["health"] = 60
                                print("Masz maksymalne HP")
                                player["health"] = player["health"] - 6
                                print("Stałes nieruchomo.")
                                print("Potwór cie zaatakował i zadał dodatkowe obrażenia, twoje HP wynosi: " + str(player["health"]) + "HP")

                        elif player["health"] <= 84:
                            player["health"] = player["health"] + player["heal"]
                            print("Uleczyłeś się! Twoje zycie wynosi: " + str(player["health"])+"HP")
                            player["health"] = player["health"] - 6
                            print("Stałes nieruchomo.")
                            print("Potwór cie zaatakował i zadał dodatkowe obrażenia, twoje HP wynosi: " +
                                  str(player["health"]) + "HP")
                        else:
                            player["health"] = 100
                            print("Masz maksymalne HP")
                            player["health"] = player["health"] - 6
                            print("Stałes nieruchomo.")
                            print("Potwór cie zaatakował i zadał dodatkowe obrażenia, twoje HP wynosi: " +
                                  str(player["health"])+"HP")

                        if player["health"] <= 0:
                            monster_won = True
            elif player_choice == "3":
                player["mana"] = player["mana"] + 25
                print("Wypiłeś potke na mane. Twoja mana wynosi: " + str(player["mana"]) + "%")
                player["health"] = player["health"] - 6
                print(
                    "Stałes nieruchomo. Potwór cie zaatakował i zadał dodatkowe obrażenia, twoje HP wynosi: " +
                     str(player["health"]) + "HP")




            elif player_choice == "5":
                break
            else:
                print("Nie rozpoznano akcji!")
            if player_won == True or monster_won == True:
                new_round = False

# FABUŁA!

    elif player_choice1 == "2":
        monster = {"name": "Monster1", "min_attack": 1, "max_attack": 10, "health": 30}
        player = {"name": "Player", "attack": 10, "crit": 15, "heal": 16, "health": 100, "mana": 100}
        print("-----------------------")
        print("CHAPTER ONE")
        print("-----------------------")
        print("Budzisz się cały obolały, nie posiadając niczego co by ci mogło pomóc")
        print("W oddali widzisz chatkę, która wydaje ci się opuszczona ")
        print("Idziesz czy zostajesz? 1)idę / 2)zostaję")
        _wybor = input()
        if _wybor == "1":
            print("Mądra decyzja, pozostanie tutaj byłoby niebezpieczne")
            print("Dotarłeś do chatki, wchodzisz do środka ostrożnym ruchem i widzisz drewniany miecz")
            print("1)Biore go / 2)Nie biorę")
            _wybor2 = input()
            if _wybor2 == "1":
                player["attack"] = 5
                print("Świetnie! Drewniany miecz nadaje się jeszcze do użycia i zwiększa twój atak")
                print("Twój atak wynosi teraz: " + str(player["attack"]) + " punktów obrażeń")
            else:
                player["attack"] = 2
                print("Masz rację. Lepiej nie brać nie swoich rzeczy")
            print("Nagle słyszysz szelest dochodzący z lewej strony")
            print("Okazuje się, że to człowiek... ale po dokładnym popatrzeniu coś ci nie pasuje")
            print("Tajemnicza osoba nic nie mówi. Macha rękami, jakby cos próbowała zrobić")
            print("Nagle twoim oczom ukazuję się wielki portal, wyłania się z niego potwór, ktorego nawet nie umiesz opisać")
            print("A sylwetka tajemniczej osoby zanika w portalu")
            print("Wystraszony nie wiesz co robić, potwór zblizą sie do ciebie, wydaję się, że chce cie zaatakować")
            print("Co robisz? 1) Walczę / 2) Uciekam")
            _wybor3 = input ()
            if _wybor3 == "1":
                if _wybor2 == "1":
                    print("Na szczęscie masz miecz")
                if _wybor2 == "2":
                    print("Musisz walczyć gołymi pięśćmi")
                print("Zaczynacie walkę")
                new_round = True
                while new_round == True:
                    miss = randint(1, 10)
                    crit = randint(1, 10)
                    monster_attack = randint(monster["min_attack"], monster["max_attack"])
                    counter = counter + 1
                    player_won = False
                    monster_won = False
                    print("-----------------------")
                    print("Wybierz akcje!: ")
                    print("1) Atak")
                    print("-----------------------")
                    player_choice = input()
                    if player_choice == "1":
                        if crit < 3:
                            print("Critical attack!")
                            monster["health"] = monster["health"] - player["crit"]
                            print("Zadałeś obrażenia równe: " + str(player["crit"]) + "HP")
                            print("Potworowi zostało: " + str(monster["health"]) + "HP")

                        elif miss < 3:
                            print("Spudłowałeś")
                            print("Zadałeś obrażenia równe: 0HP")
                            print("Potworowi zostało: " + str(monster["health"]) + "HP")

                        else:
                            monster["health"] = monster["health"] - player["attack"]
                            print("Zadałeś obrażenia równe: " + str(player["attack"]) + "HP")
                            print("Potworowi zostało: " + str(monster["health"]) + "HP")

                        if monster["health"] <= 0:
                            player_won = True

                        if miss < 3:
                            monster_attack = 0
                            print("Potwór spudłował")
                        player["health"] = player["health"] - monster_attack

                        if player["health"] <= 0:
                            monster_won = True
                        print("Potwór zadał ci: " + str(monster_attack) + "HP")
                        print("Zostało ci: " + str(player["health"]) + "HP")

                        if player["health"] <= 0:
                            print("-----------------------")
                            print("Potwór wygrał!")
                            print("Ilość rund: " + str(counter))
                            print("Koniec gry, nie żyjesz")
                            print("-----------------------")
                            break
                        if player_won == True or monster_won == True:
                            new_round = False
                print("Udało ci sie pokonać potwora!")
                print("We wzłokach potwora znajdujesz zniszczony hełm")
                print("Masz plus 20 do obrony")
                player["health"] = player["health"] + 20
                print("Twoje HP wynosi teraz: " + str(player["health"]))
                print("Jesteś zszokowany tym zajściem, ale postanawiasz wyjść z domu i iść dalej")
                print("Idziesz przez ciemny las, ledwo widzisz co jest przed tobą")
                print("Jednakże po tym co zobaczyłeś nie straszne ci ciemności")
                print("Chcesz tylko zrozumieć kim była ta tajemnicza postać i co sie tutaj dzieje")

            else:
                print("Niestety potwór jest szybszy od ciebie i wbija od tyłu swoje szpony w ciebie")
                print("Przegrałeś...")
                break
        if _wybor == "2":
            print("Masz racje, lepiej zostać, Nigdy niewiadomo co może czychać na nieznanym terenie")
            print("Gdy tak sie rozglądasz zauważasz leżący żelazny miecz")
            print("Podnosisz go")
            player["attack"] = 15
            player["crit"] = 25
            print("Twój atak wynosi teraz: " + str(player["attack"]) + " punktów obrażeń")
            print("Chowasz miecz do pasa")
            print("Gdy tak rozglądasz się w poszukiwaniu odpowiedzi, zauważasz błysk dochodzący z pobliskiej chatki")
            print("Wystraszony biegniesz przed siebie w głąb lasu")
        print("Las spowija mrok i czarne narośla na drzewach, ziemia również dziwna, wygląda na zepsutą")
        print("Idąc już jakiś czas zauważasz starszego pana patrzącego na ciebie")
        print("Idziesz do niego powoli i ostrożnie, niewiadomo czy jest dobry czy zły")
        print("Stary mędrzec podaje ci złoty klucz i przestrzega cie przez siłami zła, które nadchodzą")
        print("Starzec zaczyna machać rękami tak jak tamta istota, otwiera portal, dużo mniejszy, ale jasniejszy od tamtego i znika")
        print("Jesteś bardzo skołowany tym zajściem")
        print("Patrzysz na klucz i widzisz na nim znak. Są to dwa ognie z napisem \"Wybrany ten który posiada nic, a posiada wszystko\"")
        print("Teraz już wiesz, że musisz stawić czoła wyzwaniu i pokonać zło!")
        print("Bierzesz się w garść, poprawiasz swój podniszczony chełm i idziesz przed siebie...")
        print("-----------------------")
        print("CHAPTER TWO")
        print("-----------------------")
        print("Gdy idziesz polaną zauważasz w oddali płonącą wioske. Jako, że czujesz się bohaterem postanawiasz pobiec w jej kierunku")
        print("Na miejscu widzisz jak dwa potwory terroryzują wioske i ich mieszkańcow")

        if _wybor2 == "2":
            print("Zaciskasz pięści i biegniesz w ich kierunku")
        elif _wybor2 == "1":
            print("Wyciągasz miecz i biegniesz w ich kierunku")

        print("Stajesz przed nimi gotowy do krwawej walki")
        monster["health"] = 50
        new_round = True
        while new_round == True:
            miss = randint(1, 10)
            crit = randint(1, 10)
            monster_attack = randint(monster["min_attack"], monster["max_attack"])
            counter = counter + 1
            player_won = False
            monster_won = False
            print("-----------------------")
            print("Wybierz akcje!: ")
            print("1) Atak")
            print("-----------------------")
            player_choice = input()
            if player_choice == "1":
                if crit < 3:
                    print("Critical attack!")
                    monster["health"] = monster["health"] - player["crit"]
                    print("Zadałeś obrażenia równe: " + str(player["crit"]) + "HP")
                    print("Potworowi zostało: " + str(monster["health"]) + "HP")

                elif miss < 3:
                    print("Spudłowałeś")
                    print("Zadałeś obrażenia równe: 0HP")
                    print("Potworowi zostało: " + str(monster["health"]) + "HP")

                else:
                    monster["health"] = monster["health"] - player["attack"]
                    print("Zadałeś obrażenia równe: " + str(player["attack"]) + "HP")
                    print("Potworowi zostało: " + str(monster["health"]) + "HP")

                if monster["health"] <= 0:
                    player_won = True
                if miss < 3:
                    monster_attack = 0
                    print("Potwór spudłował")
                player["health"] = player["health"] - monster_attack

                if player["health"] <= 0:
                    monster_won = True
                print("Potwór zadał ci: " + str(monster_attack) + "HP")
                print("Zostało ci: " + str(player["health"]) + "HP")

                if player["health"] <= 0:
                    print("-----------------------")
                    print("Potwór wygrał!")
                    print("Ilość rund: " + str(counter))
                    print("Koniec gry, nie żyjesz")
                    print("-----------------------")
                    break
                if player_won == True or monster_won == True:
                    new_round = False
        print("Od razu rzuca się na ciebie drugi potwor!")
        monster["health"] = 50
        new_round = True
        while new_round == True:
            miss = randint(1, 10)
            crit = randint(1, 10)
            monster_attack = randint(monster["min_attack"], monster["max_attack"])
            counter = counter + 1
            player_won = False
            monster_won = False
            print("-----------------------")
            print("Wybierz akcje!: ")
            print("1) Atak")
            print("-----------------------")
            player_choice = input()
            if player_choice == "1":
                if crit < 3:
                    print("Critical attack!")
                    monster["health"] = monster["health"] - player["crit"]
                    print("Zadałeś obrażenia równe: " + str(player["crit"]) + "HP")
                    print("Potworowi zostało: " + str(monster["health"]) + "HP")

                elif miss < 3:
                    print("Spudłowałeś")
                    print("Zadałeś obrażenia równe: 0HP")
                    print("Potworowi zostało: " + str(monster["health"]) + "HP")

                else:
                    monster["health"] = monster["health"] - player["attack"]
                    print("Zadałeś obrażenia równe: " + str(player["attack"]) + "HP")
                    print("Potworowi zostało: " + str(monster["health"]) + "HP")

                if monster["health"] <= 0:
                    player_won = True
                if miss < 3:
                    monster_attack = 0
                    print("Potwór spudłował")
                player["health"] = player["health"] - monster_attack

                if player["health"] <= 0:
                    monster_won = True
                print("Potwór zadał ci: " + str(monster_attack) + "HP")
                print("Zostało ci: " + str(player["health"]) + "HP")

                if player["health"] <= 0:
                    print("-----------------------")
                    print("Potwór wygrał!")
                    print("Ilość rund: " + str(counter))
                    print("Koniec gry, nie żyjesz")
                    print("-----------------------")
                    break
                if player_won == True or monster_won == True:
                    new_round = False
        print("Ledwo co, ale udało ci się pokonać te dwa potwory")
        print("Idziesz do pobliskiego domu aby odpocząć, walka bardzo cię zmęczyła")
        print("W środku spotykasz wystraszone więsniaka chowającego się pod łózkiem")
        print("Krzyczysz do niego, że może już wyjść")
        print("Wieśniak wychodzi i zdaje sobie sprawe, że uratowałes jego i całą wioske")
        print("W nagrode podaje ci mikstury do regeneracji życia i robi ci leczący posiłek")
        if _wybor == "2":
            player["health"] = 100
            print("Odnowiłeś w pełni zdrowie!")
            print("Twoje życie wynosi teraz: " + str(player["health"]))
        elif _wybor2 == "1":
            player["health"] = 120
            print("Odnowiłeś w pełni zdrowie!")
            print("Twoje życie wynosi teraz: " + str(player["health"]))
        print("Wieśniak daje ci miejsce do spania i zasypiasz")
        print("NOWY DZIEŃ")
        print("Wstajesz wypoczety i zregenerowany, masz siłe by dalej ratować świat")
        print("Zauważasz, że obok leży sakwa z pieniędzmi")
        print("Bierzesz ją? 1)Tak / 2)Nie")
        _wybor4 = input()
        monety = 0
        if _wybor4 == "1":
            monety = 10
            print("Ukradłeś 10 sztuk złotych monet")
            print("Na szczęscie nikt nie zauważył tego i wychodzisz z domu jakby nigdy nic")
        elif _wybor4 == "2":
            print("Masz racje, nie wolno kraśc. Jeszcze ktoś by zauważył brak tych monet")
        else:
            print("Nieznana komenda!")

        print("Widzisz dwie ścieszki. Jedna prowadzi do sklepikarza a druga prowadzi nad staw")
        print("Którą z nich wybierzesz? 1)Ścieszka do sklepikarza / 2) Scieżka nad staw")
        _wybor5 = input()
        if _wybor5 == "1":
            print("Wybrałeś śieżke, która prowadzi do sklepikarza")
            print("Wchodzisz do sklepu i widzisz pełno broni i zbroi")
            if _wybor4 == "1":
                print("Dobrze dla ciebie, że ukradłeś tamte monety. Masz pieniądze aby kupić coś")
                print("A więc co chcez kupic?")
                print("1)Miecz - atak +15 - za 6 złota")
                print("2)Żelazny napiersnik - pancerz +50 - za 10 złota")
                print("3)Żelazny hełm - pancerz +30 - za 8 złota")
                _wybor6 = input()
                if _wybor6 == "1":
                    player["attack"] = player["attack"] + 15
                    print("Zakupiłeś żelazny miecz!")
                    print("Twój atak wynosi teraz: " + str(player["attack"]) + "HP")
                elif _wybor6 == "2":
                    player["health"] = player["health"] + 50
                    print("Zakupiłeś żelany napierśnik")
                    print("Twoje życie wynosi teraz: " + str(player["health"]) + "HP")
                elif _wybor6 == "3":
                    player["health"] = player["health"] = 30
                    print("Zakupiłeś żelazny hełm")
                    print("Twoje życie wynosi teraz: " + str(player["health"]) + "HP")
                    print("Po udanych zakupach idziesz nad staw")

            else:
                print("Niestety nie masz przy sobie piniędzy. Nic nie kupisz i musisz zawrócić")
                print("Idziesz nad staw, ale nie rozglądasz się, nie czujesz aby było tu coś interesującego")
        elif _wybor5 == "2":
            print("Idziesz nad staw")
            print("Na dnie zauważasz coś swięcacego. Postanawiasz do sprawdzić")
            print("Nurkujesz, bierzesz i wyławiasz")
            print("Okazuję się, że to żelazny napierśnik")
            player["health"] = player["health"] = 50
            print("Zwiększyłeś swój pancerz o 50")
            print("Twoje życie wynosi teraz: " + str(player["health"]) + "HP")
        else:
            print("Nie znana komenda")

        print("Postanawiasz iść ściezką, ktora zaczyna sie przy stawie")
        print("Nie ma nigdzie znaku dokąd prowadzi, ale czujesz zło w powietrzu")
        print("-----------------------")
        print("CHAPTER TWO")
        print("-----------------------")

        break
    elif player_choice1 == "4":
        break
