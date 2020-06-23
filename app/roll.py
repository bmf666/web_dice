import sys
import random
# import json
from datetime import date, datetime

today = str(date.today())


def roll_em():
    # here is where we evaluate what the user has input as dice
    #
    # dieCount = int(die.split("d", 1)[0])
    # debug
    dieCount = 2
    # dieValue = int(die.split("d", 2)[1])
    dieValue = 20

    # this is where we start the json
    #
    rollLog = {'dice_log': []}
    rollLog['dice_log'].append({
        'game date': today
    })

    # a loop to roll the number and type of dice per the user input
    #
    dieTotal = 0
    count = 1
    mod = 0

    while dieCount > 0:
        # so here is our simple dice rolling logic
        #
        letsRoll = random.randint(1, dieValue) + int(mod)
        print("d", dieValue, count, ":", sep="", end="")
        print("", letsRoll)
        dieTotal = int(letsRoll) + dieTotal
        rollLog['dice_log'].append({
            'roll ID': str(datetime.now()),
            'd': dieValue,
            'value': letsRoll,
            'total': dieTotal
        })
        dieCount = dieCount - 1
        count = count + 1

    # write to file, exit to shell
    #
    print("\n\nRoll Total:", dieTotal)
    print("Modifier:", mod)
    rollLog['dice_log'].append({
        'Roll Total': dieTotal,
        'Modifier': int(mod)
    })

    return rollLog
