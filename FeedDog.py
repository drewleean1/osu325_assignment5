#Name: Andrew Lee
#OSU 325
#Assignment 5: FeedDog.py
#Due date: February 13, 2023


def feedDog(hunger_level, biscuit_size):
    #sort both arrays
    #starting from the largest biscuit try to find a corresponding hunger level, using a binary search?
    #if not give to the next largest dog
    hunger_level.sort()
    biscuit_size.sort()
    dogs_left = len(hunger_level) - 1
    biscuits_left = len(biscuit_size) - 1
    number_fed = 0

    while dogs_left >=0 and biscuits_left >= 0:
        if biscuit_size[biscuits_left] >= hunger_level[dogs_left]:
            dogs_left -= 1
            biscuits_left -= 1
            number_fed += 1
        else:
            dogs_left -= 1

    return number_fed

#print(feedDog([1,5], [1,2,3]))
