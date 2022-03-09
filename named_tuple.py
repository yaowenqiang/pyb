from collections import namedtuple

# color = (55, 255 ,2550)

# print(color[0])

Color = namedtuple('Color', ['red', 'green', 'blue'])

color2 = Color(red=55, green=255, blue=255)
print(color2.red)