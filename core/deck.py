from random import randint
optimal_rank = {"2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
            "10":10,
            "J":10,
            "Q":10,
            "K":10,
            "A":1}
optimal_suite = ["H","C","D","S"]

def build_standard_deck() -> list[dict]:
    all_card = []
    for i in optimal_rank:
        for j in optimal_suite:
            all_card.append({"rank":i,"suite":j})
    return all_card

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for _ in range(swaps):
        index1 = randint(0,51)
        index2 = randint(0,51)
        if index1 == index2:
            index2 = randint(0,51)
        while index1 != index2:
            if deck[index1]["suite"] == "H" and index2 %5==0:
                break
            elif deck[index1]["suite"] == "C" and index2 %3==0:
                break
            elif deck[index1]["suite"] == "D" and index2 %2==0:
                break
            elif deck[index1]["suite"] == "S" and index2 %7==0:
                break
            index2 = randint(0,51)
        temp = deck[index1]
        deck[index1] = deck[index2]
        deck[index2] = temp
    return deck