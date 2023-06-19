import qrcode as qr

state_version = False
state_correction = False
state_personalize = False
state_extension = False

def personalization():
    box_size = int(input("Box size (int) = "))
    border = int(input("Border size (int) = "))
    fill_color = str(input("Fill color (str) = "))
    back_color = str(input("Back color (str) = "))
    return box_size, border, fill_color, back_color


while not state_version:
    print("What version do you want your qrcode to be ?")
    u_version = int(input("Select an integer in [1;40]\n"))

    if u_version < 1 or u_version > 40:
        print("Error, you specified a wrong int\n", "try again")
    else:
        state_version = True

print("\n")

print("Enter the data the qrcode will represent\n", "You must unescape the text before")
u_data = input("data :")

print("\n")

while not state_correction:
    print("What level of error correction do your want ?")
    print("Low = 7%; Medium = 15%; Quartile = 25%; High = 30%")
    u_correction_1 = input("L M Q H\n")
    print("\n")

    match u_correction_1:
        case 'L':
            u_correction_2 = qr.constants.ERROR_CORRECT_L
            state_correction = True
        case 'M':
            u_correction_2 = qr.constants.ERROR_CORRECT_M
            state_correction = True
        case 'Q':
            u_correction_2 = qr.constants.ERROR_CORRECT_Q
            state_correction = True
        case 'H':
            u_correction_2 = qr.constants.ERROR_CORRECT_H
            state_correction = True
        case 'l':
            u_correction_2 = qr.constants.ERROR_CORRECT_L
            state_correction = True
        case 'm':
            u_correction_2 = qr.constants.ERROR_CORRECT_M
            state_correction = True
        case 'q':
            u_correction_2 = qr.constants.ERROR_CORRECT_Q
            state_correction = True
        case 'h':
            u_correction_2 = qr.constants.ERROR_CORRECT_H
            state_correction = True
        case _:
            print("Error, you specified a wrong chr\n", "Try again")
            print("\n")

while not state_personalize:
    print("Do you want to change the box size and border ?")
    personalize = input("y or n (pro only)\n")
    print("\n")
    match personalize:
        case 'y':
            u_box_size, u_border, u_fill_color, u_back_color = personalization()
            state_personalize = True
        case 'n':
            u_box_size = 10
            u_border = 4
            state_personalize = True
        case _:
            print("Error,  you specified a wrong chr\n", "Try again")
            print("\n")

while not state_extension:
    print("What extension do you want your file to be ?")
    u_extension = input("svg or png\n")
    print("\n")

    match u_extension:
        case "svg":
            state_extension = True
        case "png":
            state_extension = True
        case _:
            print("Error,  you specified a wrong extension\n", "Try again")
            print("\n")


print("Give a name for your file\n", "Be careful, if the name is already given, it will overwrite the existing file")
u_name = input("Name of the file :")
print("\n")

u_file_name = u_name + '.' + u_extension

qr = qr.QRCode(
    version=u_version,
    error_correction=u_correction_2,
    box_size=u_box_size,
    border=u_border,
)

qr.add_data(u_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save(u_file_name)

print("Done the file was successfully created and saved")
print("\n")