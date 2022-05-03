import random


def dice_role():
    dice_sides = [1, 2, 3, 4, 5, 6]

    side_on_top = random.choice(dice_sides)

    if side_on_top:
        print("SIDE ON TOP : " + str(side_on_top))


if __name__ == "__main__":
    dice_role()
