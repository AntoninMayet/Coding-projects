import cv2, PIL

path_to_image = input("Path to your image: ")

img = cv2.imread(path_to_image)
assert img is not None, "file could not be read, check with os.path.exists()"

px = img[1,1]
print(px)

