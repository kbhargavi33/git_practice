# snakes and ladders single player game
import random
player_position = 0
snakes_ladders_dict = {4: 14, 17: 7, 98: 79, 80: 99}
while player_position < 100:
    dice_value = random.randint(1, 6)
    print("dice value is: ", dice_value)
    if player_position + dice_value < 100:
        if player_position + dice_value in snakes_ladders_dict:
            player_position = snakes_ladders_dict[player_position + dice_value]
        else:
            player_position += dice_value
        print(player_position)
    elif player_position + dice_value > 100 or (player_position + dice_value == 100 and dice_value == 6):
        continue
    elif player_position + dice_value == 100 and dice_value != 6:
        print("game over")
        break


