import cv2, codecs, csv, os
from PIL import Image

latitude = 3840
longitude = 2160

path_to_input_file = r'/home/antonin/code/Coding-projects/Video_storage/chien.jpg' #input("Path to your image: ")
path_to_binary_file = r'/home/antonin/code/Coding-projects/Video_storage/binary_file.txt'
path_to_encode_csv = r'/home/antonin/code/Coding-projects/Video_storage/encode.csv'

fichier=codecs.open(path_to_encode_csv,'r','utf-8')
encode=list(csv.DictReader(fichier,delimiter=','))
fichier.close()

def colour_definer(read_binary_code):
    for i in encode:
        i['read_binary_code']=str(i['MSB'])+str(i['3'])+str(i['2'])+str(i['LSB'])
    for i in encode:
        if i['read_binary_code']==str(read_binary_code):
            return [i['R'],i['G'],i['B']]

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
    except Exception as E:
        print(f"An error occurred: {E}")
        return None

convert_file_to_binary(path_to_input_file, path_to_binary_file)