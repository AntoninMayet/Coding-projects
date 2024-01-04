# Definitions:

- Vidéo de stockage: vidéo daans laquelle les données sont encodées

# Roadmap

- Take the video (x) to convert
- Extract data from x
- Encode data from x on y's canvas
    - Use a 4k grid 
        - 3840 by 2160 = 8,294,400 pixels
        - theoretically 1Go of x = 962 frames so just under than 17s!
    - B&W from 0 to 255 to map binary values? (better idea?)
    - Store y video @60fps
    - Hope size reduction from x to y

- Decode y to x
    - Read pixel by pixel decode values
    - Assemble obtained values to recreate x
    - Play x

- Encode & decode should be two functions 

## Comment faire la vidéo de stockage

- Générer des images de la bonne résolution
- Modifier pix par pix la couleur de chaque pix
- Faire un time-lapse des images générée

# Versions

Must use the Major.Minor.patch version naming method