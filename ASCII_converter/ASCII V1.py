from PIL import Image

density = ' .:-=+*#%@'

file_path = input('Give the path to your desired image : ')
text_file_path = input('Give the path to save the text file : ')

image = Image.open(file_path)
bw_image = image.convert('L')

file_width, file_height = image.size

with open(text_file_path, 'w') as text_file:
    for y in range(file_height):
        for x in range(file_width):
            pixel_lum = bw_image.getpixel((x, y))
            lum = pixel_lum / 255

            index = int(lum * (len(density) - 1))
            ASCII = density[index]

            print(ASCII, end=' ')
            text_file.write(ASCII)

        print()
        text_file.write('\n')