from core import deck ,game_logic

if __name__ == "__main__":
    packet = deck.build_standard_deck()
    mixed_pack = deck.shuffle_by_suit(packet)
    
    player = {"hand":[]}
    dealer = {"hand":[]}
    game_logic.run_full_game(mixed_pack,player,dealer)