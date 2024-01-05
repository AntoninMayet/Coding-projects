import cv2, codecs
from PIL import Image

latitude = 3840
longitude = 2160

path_to_input_file = r'/home/antonin/code/Coding-projects/Video_storage/chien.jpg'#input("Path to your image: ")
path_to_binary_file = r'/home/antonin/code/Coding-projects/Video_storage/bin_file.txt'
'''
image_for_data = Image.new('RGB', (latitude, longitude), color='white')
image_for_data.save('base_for_data.jpg')

img = cv2.imread(path_to_file)
assert img is not None, "file could not be read, check with os.path.exists()"

px = img[1,1]
print(px)
'''
def convert_file_to_binary(path_to_input_file, path_to_binary_file):
    try:
        with open(path_to_input_file, 'rb') as file:
            binary_data = file.read()
            binary_representation = ''.join(format(byte, '08b') for byte in binary_data)

        with open(path_to_binary_file, 'w') as output_file:
            output_file.write(binary_representation)

        print(f"Binary representation of '{path_to_input_file}' saved to '{path_to_binary_file}'.")
        return binary_representation

    except FileNotFoundError:
        print(f"File '{path_to_input_file}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

binary_data = convert_file_to_binary(path_to_input_file, path_to_binary_file)

if binary_data:
    print(f"Binary representation of '{path_to_input_file}':")
    print(binary_data)
