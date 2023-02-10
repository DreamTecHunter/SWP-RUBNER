import random
import json


def game():
    # https://www.w3schools.com/python/ref_random_choice.asp
    print("Willkommen bei Schere, Stein, Papier, Echse, Spock")
    print("Wähle 0 für Schere, 1 für Stein, 2 für Papier, 3 für Echse, 4 für Spock")
    symbole = [0, 1, 2, 3, 4]
    sheldon = random.choice(symbole)
    eingabe = int(input("Wähle aus '0', '1', '2', '3','4': "))

    # https://stackoverflow.com/questions/62092773/syntax-error-on-line-6-if-elif-statements-and-and-or-statements
    if sheldon == eingabe:
        print("Unentschieden! Bazinga")
        return 'Unentschieden', eingabe  # TODO: return von zwei werten
    elif (sheldon == 0 and eingabe == 2) or (sheldon == 0 and eingabe == 3) or \
            (sheldon == 1 and eingabe == 3) or (sheldon == 1 and eingabe == 4) or \
            (sheldon == 2 and eingabe == 1) or \
            (sheldon == 3 and eingabe == 1) or (sheldon == 3 and eingabe == 4) or \
            (sheldon == 4 and eingabe == 0) or (sheldon == 4 and eingabe == 1):
        print("Du hast verloren! Bazinga")
        return 'Sheldon', eingabe  # TODO: return von zwei werten
    else:
        print("Du hast gegen Dr.Cooper gewonnen! Kann nicht jeder behaupten")
        return 'eingabe', eingabe  # TODO: return von zwei werten


dict = {}
try:
    with open('dict.json') as file:
        dict = json.load(file)
except FileNotFoundError:
    dict = {
        'eingabe': 0,
        'Sheldon': 0,
        'Unentschieden': 0

    }

while True:
    # TODO: die beiden return-Werte werden in der gleichen reihenfolge den beiden Variablen übergeben
    result, eingabe = game()  # TODO: result = unentschieden, Sheldon oder eingabe und eingabe erhält die nummer
    # TODO: es noch das symbol in einem json gespeichert werden.
    # Ergebnis im dict wie beim poker
    dict[result] += 1
    # https://stackoverflow.com/questions/26961427/asking-the-user-if-they-want-to-play-again
    play_again = input("Möchtest du nochmal spielen (j/n)? ").lower()
    if play_again[0] != 'j':
        break
        print(test)

# daten als json  https://ingo-janssen.de/json-lesen-und-schreiben-mit-python/
with open('dict.json', 'w') as file:
    json.dump(dict, file)

# dict ausgeben
print("Du hast", dict['eingabe'], " mal gewonnen")
print("Sheldon hat ", dict['Sheldon'], " mal gewonnen")
print("Du hast ", dict['Unentschieden'], " mal unentschieden gespielt")
