from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys
import webcolors

ct = ColorThief("Purple_sample.png")
colors = {'#1772e0': 'blue', '#36e912': 'green', '#871bbe': 'purple', '#c82323': 'red', '#e9e212': 'yellow', '#7d7d7d': 'gray'}
# dominant_color = ct.get_color(quality=1)

# plt.imshow([[dominant_color]])
# plt.show()

palette = ct.get_palette(color_count=3)
plt.imshow([[palette[i] for i in range(3)]])
plt.show()

for color in palette:
    print(color)
    print(colorsys.rgb_to_hls(*color))
    print("")

for i in range(4):    
    if((colorsys.rgb_to_hls(palette[i][0], palette[i][1], palette[i][2]))[1] > 90):
        dominant_color = palette[i]
        break

print(dominant_color)

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