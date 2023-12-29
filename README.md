# Coding projects

__This place is where I'll developpe my projects of any kind__
I make anything that can seem interesting whatever this word means. My goal is to take the documentation of something, understand it and make something with it. I don't want to look at YouTube video that explains the code and the logic. I want to write it myself.

___
## ASCII converter

I want to write a code that takes a standard image and converts every pixel into an ASCII character (' .:-=+*#%@') to make it cooler.

### ASCII V1

This program finaly works. If you give it the good path to your desire image, it will return a .txt. However, it works better with low resolution picture.

### ASCII V2

I would like the program to create a web page in order to have a monospace kind of font. A GUI would also be a plus.

## QRcode generator

I think the title is self-explanatory

### QRcode V1

This is the proof of concept : the discovery of the lib. I create a basic input/print thing to simply interact with the lib and that's it

### QRcode generator v2

I've created a simple QRcode generator using the two following lib :
- qrcode for the qrcode generation (sound straightforward)
- tkinter for the GUI part

I've also used a piece of software called auto-py-to-exe to ... convert the .py file to a .exe one

### What I would like to do for the QRcode V3

I would like to do an encryption part of my qrcode.
My idea is to encode data with a key, generate a qrcode and share it with the world. The interesting part is that only the people with the encryption key can properly read the qrcode, everyone else will see a weird thing : an encrypted one.