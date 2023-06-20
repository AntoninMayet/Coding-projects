#DONE Get the image
#TODO Get the dimension of the image
#TODO Convert it in B&W
#TODO Get the value of each pixel
#TODO Convert the value in a char
#TODO Print each char on a grid the same size of the image
#TODO Open the coolest version of the image

from PIL import Image as im

density =  ' .:-=+*#%@'

file_path = (input('Give the path to your desire image :\n'))

u_file = im.open(file_path)

bw_image = u_file.convert('L')

file_width, file_height = u_file.size

'''
print('w', file_width)
print('h', file_height)
'''

for x in range(file_width):
    for y in range(file_height):
       
        pixel_lum = bw_image.getpixel((x, y))
        lum = pixel_lum / 255
       
        index = int(lum * (len(density) - 1))
        ASCII = density[index]
        print(ASCII, end=' ')
       
        count =+ 1
       
        if count > file_height:
            print('\n')
            cout = 0