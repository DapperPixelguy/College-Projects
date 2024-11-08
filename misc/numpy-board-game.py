import numpy as np


sim = 10000000


def battle(attacker_dice, defender_dice, sim):
    attacker_rolls = np.sort(np.random.randint(1,7, (sim, attacker_dice)), axis=1)[:, ::-1]
    defender_rolls = np.sort(np.random.randint(1, 7, (sim, defender_dice)), axis=1)[:, ::-1]

    atk_win = 0
    def_win = 0

    first_battles = attacker_rolls[:, 0] > defender_rolls[:, 0]
    atk_win += np.sum(first_battles)
    def_win += sim - np.sum(first_battles)

    if attacker_dice > 1 and defender_dice > 1:
        second_battles = attacker_rolls[:, 1] > defender_rolls[:, 1]
        atk_win += np.sum(second_battles)
        def_win += sim - np.sum(second_battles)

    return atk_win / (atk_win + def_win) * 100


config = [
    (3,2),
    (3,1),
    (2,2),
    (2,1),
    (1,2),
    (1,1)
]

for attacker_dice, defender_dice in config:
    win_percentage = battle(attacker_dice, defender_dice, sim)
    print(f"Attacker dice: {attacker_dice}, Defender dice: {defender_dice} - Attacker win percentage {win_percentage:.2f}%")