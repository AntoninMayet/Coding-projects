import cv2, codecs, csv, os, moviepy
from PIL import Image

# <Variables>
latitude = 3840
longitude = 2160

path_to_input_file = r'/home/antonin/code/Coding-projects/Video_storage_pof/chien.jpg' 
path_to_binary_file = r'/home/antonin/code/Coding-projects/Video_storage_pof/binary_file.txt'
path_to_csv = r'/home/antonin/code/Coding-projects/Video_storage_pof/encode.csv'
path_to_base_image = r'/home/antonin/code/Coding-projects/Video_storage_pof/base_image.jpg'

input_file_root, input_file_extension = os.path.splitext(path_to_input_file)
# </Variables>

# <Work_preparer>
fichier=codecs.open(path_to_csv,'r','utf-8')
encode=list(csv.DictReader(fichier,delimiter=','))
fichier.close()
# </Work_preparer>

# <Functions_zone>
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

def colour_definer(extracted_octet_from_input_file):
    for i in encode:
        i['extracted_octet_from_input_file']=str(i['MSB'])+str(i['3'])+str(i['2'])+str(i['LSB'])
    for i in encode:
        if i['extracted_octet_from_input_file']==str(extracted_octet_from_input_file):
            return [i['R'],i['G'],i['B']]

def file_reader(path_to_input_file, asked): #Est-ce que l'on peut faire tourner deux fonction en même temps, trouver un moyen de sauvegarder l'état d'avancement du le lecture pour ne pas donner deux fois le même octet
    with open('binary_file.txt', 'r', encoding='utf-8') as binary_file:
        while asked == True:
            read_octet = binary_file.read(4)

            if not read_octet:
                print("Reached end of input file")
                asked = False
                break

        
def base_image_generator():
    image_for_data = Image.new('RGB', (latitude, longitude), color='white')
    image_for_data.save(path_to_base_image, 'JPEG')
# </Functions_zone>

# <Testing_things_zone>
img = cv2.imread(path_to_input_file)
assert img is not None, "file could not be read, it might not exist"
# </Testing_things_zone>

# <Heart_of_the_programm>
convert_file_to_binary(path_to_input_file, path_to_binary_file)
colour_definer(extracted_octet_from_input_file)
# </Heart_of_the_programm>