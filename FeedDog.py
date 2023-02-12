#Name: Andrew Lee
#OSU 325
#Assignment 5: FeedDog.py
#Due date: February 13, 2023


def feedDog(hunger_level, biscuit_size):
    '''function takes two arrays: hunger_level which correlates to the hunger level of the dogs; and biscuit_size which
    is the number of biscuits we have and how much hunger they satisfy. We sort both arrays, start from the end of both
    arrays, giving the biggest dog the biggest biscuit.'''

    hunger_level.sort()                                 #python's built in sort function, nlogn time
    biscuit_size.sort()

    dogs_left = len(hunger_level) - 1                   #vars to keep track of where we are in the array
    biscuits_left = len(biscuit_size) - 1

    number_fed = 0                                      #var to store the result

    while dogs_left >=0 and biscuits_left >= 0:         #while loop that continues if we have both dogs and biscuits left
        if biscuit_size[biscuits_left] >= hunger_level[dogs_left]:     #condition for a biscuit to satisfy a dog's hunger
            dogs_left -= 1
            biscuits_left -= 1
            number_fed += 1
        else:
            dogs_left -= 1

    return number_fed

