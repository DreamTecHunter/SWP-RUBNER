import random

rounds = 1000000


# Wahrscheinlichkeiten Wikipedia: https://de.wikipedia.org/wiki/Poker

# System Karten:
#     Wert zw. 0 - 51
#     Wert modulo 13 ergibt die Zahl
#     Wert dividiert durhc 13 ergibt die Farbe

def kartenAusteilen(anzahl):
    karten = []
    for i in range(5):
        karten.append(ziehung(karten))
    return karten


def ziehung(karten):
    rand = random.randint(0, 51)
    if not rand in karten:
        return rand
    else:
        return ziehung(karten)


def paarVorhanden(karten):
    paar = []
    for i in karten:
        paar.append(i % 13)
    # print(paar)
    for k in paar:
        if paar.count(k) == 2:
            # print("PAAR "+ str(k))
            return True
    return False


def zweiPaarVorhanden(karten):
    paar = []
    for i in karten:
        paar.append(i % 13)
    # print(paar)
    counts = []
    for k in paar:
        counts.append(paar.count(k))
    if counts.count(2) == 4:
        # print("2 PAAR ")
        return True
    return False


def drillingeVorhanden(karten):
    drilling = []
    for i in karten:
        drilling.append(i % 13)
    # print(drilling)
    counts = []
    for k in drilling:
        counts.append(drilling.count(k))
    if counts.count(3) == 3:
        # print("Drillinge ")
        return True
    return False


def fourOfaKindVorhanden(karten):
    foak = []
    for i in karten:
        foak.append(i % 13)
    # print(drilling)
    counts = []
    for k in foak:
        counts.append(foak.count(k))
    if counts.count(4) == 4:
        # print("Four of a kind ")
        return True
    return False


def fullhouseVorhanden(karten):
    drilling = drillingeVorhanden(karten)
    paar = paarVorhanden(karten)
    if paar and drilling:
        # print("Full House")
        return True
    return False


def flushVorhanden(karten):
    flush = []
    vorherigeFarbe = -1
    for i in karten:
        card = int(i / 13)
        if len(flush) == 0:
            vorherigeFarbe = card
        if not vorherigeFarbe == card:
            return False
        else:
            flush.append(card)
    # print("Flush")
    return True


def straightVorhanden(karten, with_ace_as_lowest: bool = True):
    symbol_count = 13
    _hand = sorted(h % symbol_count for h in karten)
    if with_ace_as_lowest:
        ace_amount = sum(h == symbol_count - 1 for h in _hand)
        if 1 < ace_amount:
            return False
        if ace_amount == 1:
            if all(_hand[i] == i for i in range(0, len(_hand) - 1)):
                return True
    return all(_hand[i] + 1 == _hand[i + 1] for i in range(len(_hand) - 1))


def straightFlushVorhanden(karten):
    straight = straightVorhanden(karten)
    flush = flushVorhanden(karten)
    if straight and flush:
        # print("straight flush")
        return True
    return False


def royalflushVorhanden(karten):
    sf = straightFlushVorhanden(karten)
    hc = getHighCard(karten)
    if sf and (hc == 12 or hc == 25 or hc == 38 or hc == 51):
        # print("Royal Flush")
        return True
    return False


def getHighCard(karten):
    cards = []
    for i in karten:
        cards.append(i % 13)
    karten.insertion_sort()
    return karten[len(karten) - 1]


dic = {"highCard": 0,
       "paar": 0,
       "zwei paar": 0,
       "drillinge": 0,
       "staight": 0,
       "flush": 0,
       "full house": 0,
       "four of a kind": 0,
       "straight flush": 0,
       "royal flush": 0
       }

for i in range(0, rounds):
    hand = kartenAusteilen(5)

    if royalflushVorhanden(hand):
        dic["royal flush"] = dic["royal flush"] + 1
    elif straightFlushVorhanden(hand):
        dic["straight flush"] = dic["straight flush"] + 1
    elif fourOfaKindVorhanden(hand):
        dic["four of a kind"] = dic["four of a kind"] + 1
    elif fullhouseVorhanden(hand):
        dic["full house"] = dic["full house"] + 1
    elif flushVorhanden(hand):
        dic["flush"] = dic["flush"] + 1
    elif straightVorhanden(hand):
        dic["staight"] = dic["staight"] + 1
    elif drillingeVorhanden(hand):
        dic["drillinge"] = dic["drillinge"] + 1
    elif zweiPaarVorhanden(hand):
        dic['zwei paar'] = dic["zwei paar"] + 1
    elif paarVorhanden(hand):
        dic["paar"] = dic["paar"] + 1
    else:
        dic["highCard"] = dic["highCard"] + 1

if __name__ == '__main__':
    print(dic)
    ergDic = dic
    for i in ergDic:
        ergDic[i] = ergDic[i] / rounds * 100
    print([k + ":" + str(ergDic[k]) + "%" for k in ergDic.keys()])
