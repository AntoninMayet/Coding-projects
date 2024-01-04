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

- Générer des images de la bonne résolution, en blanc
- Modifier pix par pix la couleur de chaque pix
- Faire un time-lapse des images générée

## This is how to encode data with colours:

| R   | G   | B   |   | MSB | 3 | 2 | LSB |
|-----|-----|-----|---|-----|---|---|-----|
| 0   | 0   | 0   |   | 0   | 0 | 0 | 0   |
| 0   | 0   | 125 |   | 0   | 0 | 0 | 1   |
| 0   | 0   | 255 |   | 0   | 0 | 1 | 0   |
| 0   | 125 | 0   |   | 0   | 0 | 1 | 1   |
| 0   | 125 | 125 |   | 0   | 1 | 0 | 0   |
| 0   | 125 | 255 |   | 0   | 1 | 0 | 1   |
| 0   | 255 | 0   |   | 0   | 1 | 1 | 0   |
| 0   | 255 | 125 |   | 0   | 1 | 1 | 1   |
| 0   | 255 | 255 |   | 1   | 0 | 0 | 0   |
| 125 | 0   | 0   |   | 1   | 0 | 0 | 1   |
| 125 | 0   | 125 |   | 1   | 0 | 1 | 0   |
| 125 | 0   | 255 |   | 1   | 0 | 1 | 1   |
| 125 | 125 | 0   |   | 1   | 1 | 0 | 0   |
| 125 | 125 | 125 |   | 1   | 1 | 0 | 1   |
| 125 | 125 | 255 |   | 1   | 1 | 1 | 0   |
| 125 | 255 | 0   |   | 1   | 1 | 1 | 1   |

NB: White (255, 255, 255) will be the default color

### Brain vomit

Le programme génére des images blanches. Il encode ensuite les données dessus. Si données > place sur l'image alors le programme en génére une nouvelle (function?). Quand toutes les données ont étaient écrtites sur des images, le programme les assemble en vidéo au format *.avi* parce que format raw donc zéro compressioon ni modif (en théorie).

Faire une fonction qui encode les données et retourne un message quand elle n'a plus de oplace pour que le programme attrappe ce message etdemande à l'autre fonction de générer une image.

# Versions

Must use the Major.Minor.patch version naming method