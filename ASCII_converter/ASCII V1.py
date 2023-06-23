from PIL import Image, ImageFont, ImageDraw
import os
import time

file_path = input('Give the path to your desired image : ')

start_time = time.time()

density = ' .:-=+*#%@'

font_name = r'C:\Users\anton\.vscode\Coding_projects\ASCII_converter\CourierPrime-Regular.ttf'
font_size = 12
spacing = 1
font = ImageFont.truetype(font_name, font_size)

text_file_path, image_name = os.path.split(file_path)
image_name_without_extension = os.path.splitext(image_name)[0]

text_file_path = os.path.join(text_file_path, f'{image_name_without_extension}.txt')

image = Image.open(file_path)
bw_image = image.convert('L')

image_width, image_height = image.size

result_image = Image.new('L', (image_width, image_height))
draw = ImageDraw.Draw(result_image)
draw.fontmode = '1'

with open(text_file_path, 'w') as text_file:
    for y in range(image_height):
        for x in range(image_width):
            pixel_lum = bw_image.getpixel((x, y))
            lum = pixel_lum / 255

            index = int(lum * (len(density) - 1))
            ASCII = density[index]

            text_file.write(ASCII)

            draw.text((x * (font_size + spacing), y * font_size), ASCII, fill='white', font=font)

        text_file.write('\n')

result_image.save('output_image.jpg')

end_time = time.time()
time_spend = end_time - start_time
print('Time spend (ms) : ', time_spend)