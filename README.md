# ASCII-picture
Converts coloured .png/.jpeg pictures into black and white pictures (made of ASCII characters).
How to use converter: 
1)   Enter python3 converter.py in terminal.
2)   Zoom out to see best results.
3)   Change picture by editing the file path in line 11 of the converter 
     ->   im = Image.open("twin-towers.jpg")

<img src="https://github.com/yili288/ASCII-pic/blob/master/twin-towers.jpg" width="200" height="250" />
<img src="https://github.com/yili288/ASCII-pic/blob/master/Black-white-twin-towers.png" width="200" height="250" />

How it works:
1)   Uses the Python Imaging Library (PIL) to import the selected picture.
2)   Finds the RGB value for end bit in the picture.
3)   Represents each pixel in a 2 dimension matrix.
4)   Convert RGB value to this grey scale 
     ->  `^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$.
6)   Prints the matrix in the terminal.

