# Roadmap

- Take the video (x) to convert
- Extract data from x
- Encode data from x on y's canvas
    - Use a 4k grid 
        - 3840 by 2160 = 8,294,400 pixels
        - theoretically 1Go of x = 121 frame so just over than 2s! 🤯
    - B&W from 0 to 255 to map binary values? (better idea?)
    - Store y video @60fps
    - Hope size reduction from x to y

- Decode y to x
    - Read pixel by pixel decode values
    - Assemble obtained values to recreate x
    - Play x

# Versions

Must use the Major.Minor.patch version naming method