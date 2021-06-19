# DEFINE VARIABLES

# Colors
DARK_BLACK = (0, 0, 0)
BLACK = (20, 20, 20)
DARK_GRAY = (60, 60, 60)
GRAY = (110, 110, 110)
LIGHT_GRAY = (190, 190, 190)
WHITE = (230, 230, 230)
LIGHT_WHITE = (255, 255, 255)

LIGHT_YELLOW = (252,255,163)
YELLOW = (255, 255, 25)
DARK_YELLOW = (224, 217, 0)
ORANGE = (255, 187, 51)
DARK_ORANGE = (230, 153, 0)
LIGHT_RED = (255, 136, 77)
RED = (255, 0, 0)
DARK_RED = (204, 0, 0)
PINK = (255, 102, 255)
LIGHT_PURPLE = (196, 77, 255)
PURPLE = (115, 0, 230)
DARK_PURPLE = (64, 0, 128)
BROWN = (117, 0, 0)
DARK_BROWN = (74, 0, 0)

LIGHT_AQUA = (153, 255, 255)
AQUA = (0, 255, 255)
DARK_AQUA = (0, 179, 179)
LIGHT_BLUE = (128, 170, 255)
BLUE = (0, 42, 255)
DARK_BLUE = (0, 0, 179)

LIGHT_LIME = (179, 255, 179)
LIME = (128, 255, 149)
DARK_LIME = (0, 255, 0)
GREEN = (0, 204, 0)
DARK_GREEN = (0, 128, 0)


# METHODS

# Modify a Color
def modify(color: tuple[int, int, int], modifier: tuple[int, int, int]) -> tuple[int, int, int]:

    result = [0, 0, 0]

    for i in range(0, 3):

        result[i] = color[i] + modifier[i]

        if result[i] > 255:
            result[i] = 255
        if result[i] < 0:
            result[i] = 0

    return result[0], result[1], result[2]


# Mix two Colors
def mix(color1: tuple[int, int, int], color2: tuple[int, int, int]) -> tuple[int, int, int]:

    result = [0, 0, 0]

    for i in range(0, 3):

        result[i] = (color1[i] + color2[i]) // 2

    return result[0], result[1], result[2]
