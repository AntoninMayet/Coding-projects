import cv2
from PIL import Image, ImageDraw

image_for_data = Image.new('RGB', (3840, 2160), color='white')

image_for_data.save('base_for_data.jpg')

path_to_file = input("Path to your image: ")

img = cv2.imread(path_to_file)
assert img is not None, "file could not be read, check with os.path.exists()"

px = img[1,1]
print(px)