# snakes and ladders multi player game
import random
n = int(input("enter number of players: "))
player_list = n * [0]
snakes_ladders_dict = {4: 14, 17: 7, 98: 79, 80: 99}
condition = True
while(condition):
    for player_no in range(len(player_list)):
        dice_value = random.randint(1, 6)
        print("dice value of player_{}: {}".format(player_no+ 1, dice_value))
        if player_list[player_no] + dice_value < 100:
            if player_list[player_no] + dice_value in snakes_ladders_dict:
                player_list[player_no] = snakes_ladders_dict[player_list[player_no] + dice_value]

            else:
                player_list[player_no] += dice_value

            print("player {} position: {}". format(player_no+1, player_list[player_no]))
        elif player_list[player_no] + dice_value > 100 or (player_list[player_no] + dice_value == 100 and dice_value == 6):
            continue
        elif player_list[player_no] + dice_value == 100 and dice_value != 6:
            print("player {} wins".format(player_no + 1))
            condition = False
            break



