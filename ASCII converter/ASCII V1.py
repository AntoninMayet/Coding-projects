#DONE Get the image
#TODO Get the dimension of the image
#TODO Convert it in B&W
#TODO Get the value of each pixel
#TODO Convert the value in a char
#TODO Print each char on a grid the same size of the image
#TODO Open the coolest version of the image

from PIL import Image as im

density =  ' .:-=+*#%@'

u_image = (input('Give the path to your desire image\n'))
image = im.open(u_image)

image.show()