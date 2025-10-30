from core.player_io import ask_player_action

def calculate_hand_value(hand: list[dict]) -> int:
    sum_ = 0
    for i in range(len(hand)):
        if hand[i]["rank"] == 'Q' or hand[i]["rank"] =='J' or hand[i]["rank"] == 'K':
            sum_ += 10
        elif hand[i]["rank"] == 'A':
            sum_+=1
        else:
            hand[i]["rank"] = int(hand[i]["rank"])
            sum_ += hand[i]["rank"]
    return sum_ 

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player["hand"].append(deck.pop(0))
    player["hand"].append(deck.pop(0))
    dealer["hand"].append(deck.pop(0))
    dealer["hand"].append(deck.pop(0))
    print(f"The player's score is:{calculate_hand_value(player['hand'])}")
    print(f"The dealer's score is:{calculate_hand_value(dealer['hand'])}")
    
def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while dealer["rank"] <= 17:
        dealer["rank"].append(deck.pop(0))
    if dealer["rank"] > 21:
        return False
    elif dealer["hand"]["rank"] >17 and dealer["hand"]["rank"] <21:
        return True

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck,player,dealer)
    ask_player_action()
    while ask_player_action == "H":
        player["hand"].append(deck.pop(0))
        calculate_hand_value(player["hand"])
        if player["hand"]["rank"] > 21:
            print("You are disqualified, you are over 21!")
            break
        else:
            continue
    if ask_player_action == "S":
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