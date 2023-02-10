from operator import truediv
from collections import Counter
import random


def generateDeck():
    cards = []
    for i in range(0, 4):
        for j in range(2, 15):
            cards.append(str(i) + "|" + str(j))
    return cards


def fillDict():
    cnt = {}

    cnt["highCard"] = 0.0
    cnt["onePair"] = 0.0
    cnt["twoPair"] = 0.0
    cnt["threeOfAKind"] = 0.0
    cnt["straight"] = 0.0
    cnt["flush"] = 0.0
    cnt["fullHouse"] = 0.0
    cnt["fourOfAKind"] = 0.0
    cnt["straightFlush"] = 0.0
    cnt["royalFlush"] = 0.0

    return cnt


def ziehung(cards, anz):
    yourcards = []
    for i in range(anz):
        index = random.randrange(len(cards))
        value = cards[index]
        cards[index] = cards[len(cards) - 1 - i]
        cards[len(cards) - 1 - i] = value
        yourcards.append(value)
    return yourcards


def getSplitColor(cards):
    cardColors = []
    for c in cards:
        cardColors.append(int(c.split("|")[0]))
    return cardColors


def getSplitIndex(cards):
    cardIndex = []
    for c in cards:
        cardIndex.append(int(c.split("|")[1]))
    return cardIndex


def hasHighCard(cards):
    if not hasOnePair(cards) and not hasTwoPair(cards) \
            and not hasThreeOfAKind(cards) and not hasStraight(cards) \
            and not hasFlush(cards) and not hasFullHouse(cards) \
            and not hasFourOfAKind(cards) and not hasStraightFlush(cards) \
            and not hasRoyalFlush(cards):
        return True
    else:
        return False


def hasOnePair(cards):
    cardsIndex = getSplitIndex(cards)
    cnt = 0

    for c in cardsIndex:
        if cardsIndex.count(c) == 2:
            cnt += 1
    if cnt == 2:  # 2, weil die Zahl vom Paar zwei mal gecheckt wird
        return True
    else:
        return False
        # hallo


def hasTwoPair(cards):
    cardsIndex = getSplitIndex(cards)
    cnt = 0

    for c in cardsIndex:
        if cardsIndex.count(c) == 2:
            cnt += 1
    if cnt == 4:
        return True
    else:
        return False


def hasThreeOfAKind(cards):
    cardsIndex = getSplitIndex(cards)
    cnt = 0

    for c in cardsIndex:
        if cardsIndex.count(c) == 3:
            cnt += 1
    if cnt == 3:
        return True
    else:
        return False


def hasStraight(cards):
    cardsIndex = getSplitIndex(cards)
    # zu list mit int Werten konvertieren
    cardsIndex = [int(i) for i in cardsIndex]
    cardsIndex.sort()

    if (int(max(cardsIndex)) - int(min(cardsIndex))) == (len(cardsIndex) - 1):
        if hasOnePair(cards) or hasTwoPair(cards) \
                or hasThreeOfAKind(cards) or hasFourOfAKind(cards):
            return False
        else:
            return True
    else:
        return False


def hasFlush(cards):
    cardsColor = getSplitColor(cards)

    for c in cardsColor:
        if cardsColor.count(c) == 5:
            return True
        else:
            return False


def hasFullHouse(cards):
    if hasOnePair(cards) and hasThreeOfAKind(cards):
        return True
    else:
        return False


def hasFourOfAKind(cards):
    cardsIndex = getSplitIndex(cards)
    cnt = 0

    for c in cardsIndex:
        if cardsIndex.count(c) == 4:
            cnt += 1
    if cnt == 4:
        return True
    else:
        return False


def hasStraightFlush(cards):
    cardsColor = getSplitColor(cards)
    cardsIndex = getSplitIndex(cards)
    # zu list mit int Werten konvertieren
    cardsIndex = [int(i) for i in cardsIndex]
    cardsIndex.sort()

    for c in cardsColor:
        if cardsColor.count(c) == 5:
            if (int(max(cardsIndex)) - int(min(cardsIndex))) \
                    == (len(cardsIndex) - 1):
                return True
            else:
                return False
        else:
            return False


def hasRoyalFlush(cards):
    cardsColor = getSplitColor(cards)
    cardsIndex = getSplitIndex(cards)
    cardsIndex = [int(i) for i in cardsIndex]
    cardsIndex.sort()
    karten = generateDeck()
    kartenINT = getSplitIndex(karten)
    kartenINT = [int(i) for i in kartenINT]
    kartenINT.sort()

    for c in cardsColor:
        if cardsColor.count(c) == 5:
            if (min(cardsIndex) == (max(kartenINT) - len(cardsIndex) + 1)) \
                    and (max(cardsIndex) == max(kartenINT)):
                return True
            else:
                return False
        else:
            return False


def statistik(anzZiehungen, anzKarten):
    cnt = fillDict()
    for i in range(0, anzZiehungen):
        deck = generateDeck()
        # print(deck)
        ziehungKarten = ziehung(deck, anzKarten)

        if hasRoyalFlush(ziehungKarten):
            cnt["royalFlush"] += 1
        elif hasStraightFlush(ziehungKarten):
            cnt["straightFlush"] += 1
        elif hasFourOfAKind(ziehungKarten):
            cnt["fourOfAKind"] += 1
        elif hasFullHouse(ziehungKarten):
            cnt["fullHouse"] += 1
        elif hasFlush(ziehungKarten):
            cnt["flush"] += 1
        elif hasStraight(ziehungKarten):
            cnt["straight"] += 1
        elif hasThreeOfAKind(ziehungKarten):
            cnt["threeOfAKind"] += 1
        elif hasTwoPair(ziehungKarten):
            cnt["twoPair"] += 1
        elif hasOnePair(ziehungKarten):
            cnt["onePair"] += 1
        elif hasHighCard(ziehungKarten):
            cnt["highCard"] += 1

    stats = {key: round(((value / anzZiehungen) * 100), 4) for key, \
                                                               value in cnt.items()}

    for key, value in stats.items():
        if (key == "flush"):
            print(key, ':        \t\t\t', value, '%')
        else:
            print(key, ':        \t\t', value, '%')
    # print(stats)


if __name__ == "__main__":
    x = input("Anzahl der Ziehungen: ")
    y = input("Anzahl der Karten: ")
    statistik(int(x), int(y))

"""
    ziehung = ['2|10', '2|10', '2|3', '1|11', '2|10']
    print(ziehung)
    print("High Card: " + str(hasHighCard(ziehung)))
    print("Paar: " + str(hasOnePair(ziehung)))
    print("Zwei Paare: " + str(hasTwoPair(ziehung)))
    print("Drilling: " + str(hasThreeOfAKind(ziehung)))
    print("Vierling: " + str(hasFourOfAKind(ziehung)))
    print("Full House: " + str(hasFullHouse(ziehung)))
    print("Royal Flush: " + str(hasRoyalFlush(ziehung)))
    print("Flush: " + str(hasFlush(ziehung)))
    print("Straight: " + str(hasStraight(ziehung)))
    print("Straight Flush: " + str(hasStraightFlush(ziehung)))
"""