import random
player_position= 0
while(True):
    dice_value = random.randint(1, 6)
    player_position += dice_value
    print(player_position)