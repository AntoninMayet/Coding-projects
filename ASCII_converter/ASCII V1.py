from PIL import Image, ImageFont, ImageDraw
import os

density = ' .:-=+*#%@'

file_path = input('Give the path to your desired image : ')

text_file_path, image_name = os.path.split(file_path)
image_name_without_extension = os.path.splitext(image_name)[0]

text_file_path = os.path.join(text_file_path, f'{image_name_without_extension}.txt')

image = Image.open(file_path)
bw_image = image.convert('L')

file_width, file_height = image.size

font_name = r'C:\Users\anton\.vscode\Coding_projects\ASCII_converter\CourierPrime-Regular.ttf'
font_size = 12
spacing = 1
font = ImageFont.truetype(font_name, font_size)

with open(text_file_path, 'w') as text_file:
    for y in range(file_height):
        for x in range(file_width):
            pixel_lum = bw_image.getpixel((x, y))
            lum = pixel_lum / 255

            index = int(lum * (len(density) - 1))
            ASCII = density[index]

            print(ASCII, end=' ')
            text_file.write(ASCII)

        text_file.write('\n')