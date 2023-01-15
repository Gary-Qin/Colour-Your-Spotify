from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys
import webcolors

ct = ColorThief("nejat.jpg")
colors = {'#1772e0': 'blue', '#36e912': 'green', '#871bbe': 'purple', '#c82323': 'red', '#e9e212': 'yellow', '#7d7d7d': 'gray'}
# dominant_color = ct.get_color(quality=1)

# plt.imshow([[dominant_color]])
# plt.show()

palette = ct.get_palette(color_count=5)
plt.imshow([[palette[i] for i in range(5)]])
plt.show()

for color in palette:
    print(color)
    print(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}")
    print(colorsys.rgb_to_hsv(*color))
    print(colorsys.rgb_to_hls(*color))

# def closest_color(rgb):
#     differences = {}
#     for color_hex, color_name in colors.items():
#         r, g, b = webcolors.hex_to_rgb(color_hex)
#         differences[sum([(r - rgb[0]) ** 2,
#                          (g - rgb[1]) ** 2,
#                          (b - rgb[2]) ** 2])] = color_name
#     return differences[min(differences.keys())]

# try:
#     cname = webcolors.rgb_to_name(dominant_color)
#     print(f"The dominant color is {cname}")
# except ValueError:
#     cname = closest_color(dominant_color)
#     print(f"The dominant color is most like {cname}")

# plt.imshow([[dominant_color]])
# plt.show()