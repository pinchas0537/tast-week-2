def ask_player_action() -> str:
    input_ch = input("Please enter HIT = H or STAND = S ")
    while len(input_ch) != 1 or input_ch.isdigit():
        input_ch = input("Please enter HIT = H or STAND = S ")
ask_player_action()