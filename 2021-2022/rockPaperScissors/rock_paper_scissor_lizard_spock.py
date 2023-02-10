# rock, paper, scissor, lizard, spock
# item = 00000
# 1 = item gewinnt gegen das andere item
# 0 = item gewinnt nicht
# - = unentschieden
import random

items = {
    "rock": [0, "-0110"],
    "paper": [1, "1-001"],
    "scissor": [2, "01-10"],
    "lizard": [3, "010-1"],
    "spock": [4, "1010-"]
}


def fight(attacker: str, defender: str):
    value = list(items[attacker][1])[items[defender][0]]
    if "1" == value:
        return True
    if "0" == value:
        return False
    if "-" == value:
        return None


def start():
    leave = False
    while not leave:
        reply = input("\nWelcome to rock-paper-scissor-lizard-spock:\n"
                      "0:\texit\n"
                      "1:\tplay\n"
                      "2:\tinstructions(disabled)\n")
        if reply == "0":
            leave = True
        if reply == "1":
            play()
        if reply == "2":
            instructions()


def play():
    leave = False
    while not leave:
        reply = input("\nPick a hand:\n"
                      "rock\n"
                      "paper\n"
                      "scissor\n"
                      "lizard\n"
                      "spock\n"
                      "or exit by hitting 0\n")
        if reply == "0":
            leave = True
        elif items.__contains__(reply):
            defender = None
            i = random.randrange(0, 4)
            print(i)
            for item in items:
                print(items[item])
                if items[item][0] == i:
                    defender = item
            print("you picked "+reply+" against "+defender)
            state = fight(reply, defender)
            if state:
                print("You won!")
            elif not state:
                print("You lost!")
            elif state is None:
                print("Both picked" + reply)


def instructions():
    pass


if __name__ == "__main__":
    start()
