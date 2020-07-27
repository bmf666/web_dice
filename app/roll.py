import random
from datetime import date, datetime

today = str(date.today())


def roll_em(die, mod):
    # here is where we evaluate what the user has input as dice
    #
    die_count = int(die.split("d", 1)[0])
    die_value = int(die.split("d", 2)[1])
    if len(mod) == 0:
        mod = 0

    # this is where we start the roll log
    #
    roll_log = {'dice_log': []}
    roll_log['dice_log'].append({
        'game date': today
    })

    # a loop to roll the number and type of dice per the user input
    #
    die_total = 0
    count = 1

    while die_count > 0:
        # so here is our simple dice rolling logic
        #
        lets_roll = random.randint(1, die_value) + int(mod)
        print("d", die_value, " ", count, ":", sep="", end="")
        print("", lets_roll)
        die_total = int(lets_roll) + die_total
        roll_log['dice_log'].append({
            'roll ID': str(datetime.now()),
            'd': die_value,
            'value': lets_roll,
            'total': die_total
        })
        die_count = die_count - 1
        count = count + 1

    # write to file, exit to shell
    #
    print("\n\nRoll Total:", die_total)
    print("Modifier:", mod)
    roll_log['dice_log'].append({
        'Roll Total': die_total,
        'Modifier': int(mod)
    })

    return roll_log
