
prisoner_count = 5
chocolates = 10
starting_prisoner = 5

#1 2 3 4 5

while(chocolates > 0 ):
    for i in range(starting_prisoner, prisoner_count+1):
        chocolates -= 1
        if chocolates == 0:
            print(i)
            break

    starting_prisoner = 1


