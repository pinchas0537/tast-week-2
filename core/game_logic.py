import player_io

def calculate_hand_value(hand: list[dict]) -> int:
    result = []
    for i in hand:
        result.append(int(i["rank"]))
    sum_ = result[0] + result[1]
    return sum_ 

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    players = deck[:2]
    dealers = deck[2:4]
    player["hand"].append(deck.pop(0))
    player["hand"].append(deck.pop(0))
    dealer["hand"].append(deck.pop(0))
    dealer["hand"].append(deck.pop(0))
    print(f"The player's score is:{calculate_hand_value(players)}")
    print(f"The dealer's score is:{calculate_hand_value(dealers)}")
    
def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while dealer["hand"]["rank"] <= 17:
        dealer["hand"].append(deck.pop(0))
    if dealer["hand"]["rank"] > 21:
        return False
    elif dealer["hand"]["rank"] >17 and dealer["hand"]["rank"] <21:
        return True

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck,player,dealer)
    player_io.ask_player_action()
    while player_io.ask_player_action == "H":
        player["hand"].append(deck.pop(0))
        calculate_hand_value(player["hand"])
        if player["hand"]["rank"] > 21:
            print("You are disqualified, you are over 21!")
            break
        else:
            continue
    if player_io.ask_player_action == "S":
        dealer_play(deck,dealer)
        if dealer_play == False:
            print("You lost.")
            exit
        else:
            the_sum_of_the_hand_is_player = player["hand"]["rank"]
            the_sum_of_the_hand_is_dealer = dealer["hand"]["rank"]
            if the_sum_of_the_hand_is_player > the_sum_of_the_hand_is_dealer:
                print(f"The player won{player['hand']["rank"]}")
            elif the_sum_of_the_hand_is_dealer >the_sum_of_the_hand_is_player:
                print(f"The dealer won{dealer['hand']["rank"]}")
            else:
                print(f"draw{player['hand']["rank"]}{dealer['hand']["rank"]}")          