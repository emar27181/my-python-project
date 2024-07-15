def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


"""
print(hex_to_rgb("#000000"))
print(hex_to_rgb("#FFFFFF"))
print(hex_to_rgb("#FF0000"))
print(hex_to_rgb("#FF5500"))
"""
