#Name: Andrew Lee
#OSU 325
#Assignment 5: FeedDog.py
#Due date: February 13, 2023


def feedDog(hunger_level, biscuit_size):
    #merge sort both arrays
    #starting from the largest biscuit try to find a corresponding hunger level, using a binary search?
    #if not give to the next largest dog
    number_fed = 0
    for x in hunger_level:
        if x in biscuit_size:
            hunger_level.remove(x)
            biscuit_size.remove(x)
            number_fed += 1
    for x in hunger_level:
        for y in biscuit_size:
            if x <= y:
                hunger_level.remove(x)
                biscuit_size.remove(y)
                number_fed += 1
    return number_fed


