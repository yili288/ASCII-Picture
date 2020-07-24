# Converts images into black and white pictures in terminal 
# Idea from https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/
# represents each pixel with a character based on how 'dark' the character is 
# each grid made is 2D (list / tuple)

# PIL - Python Imaging Library
from PIL import Image
from PIL.Image import core as _imaging

# Add image file name here
im = Image.open("twin-towers.jpg"). 
print(im.format, im.size, im.mode)
im.show()
height, width = im.size

# getdata() - provides RBG code for each pixel
pixel_list = list(im.getdata())

pixel_grid = []
new_row = []
col = height

for i in range(width):
	new_row = pixel_list[ i*col : (i+1)*col ]
	pixel_grid.append(new_row)

pixel_grid_tuple = tuple(pixel_grid)

#convert RBG code to brightness level
average_list = []

for row in pixel_grid_tuple:
	for pixel in row:
		average = ( pixel[0] + pixel[1] + pixel[2] )/ 3
		average_list.append(average)

#make brightness level grid
brightness_grid = []
col = height

for i in range(width):
	new_row = average_list[ i*col : (i+1)*col ]
	brightness_grid.append(new_row)

asci = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

interval = 255 / len(asci)

# returns the position of the value on the ascii light to dark shade range 
# to start, x should be 1 
def sort(value, x):
	if(value < (interval*x) or x > len(asci)):
		if(x >= 65):
			x = 64
		return asci[x-1]
	else:
		return sort(value, x+1)

# convert average value grid into characters based on range in the asci string
symbol_grid = []
symbol_list= []
symbol_row = []

for row in brightness_grid:
	for num in row:
		round(num)
		symbol = sort(num, 1)
		symbol_list.append(symbol)

for i in range(width):
	symbol_row = symbol_list[ i*col : (i+1)*col ]
	symbol_grid.append(symbol_row)

# prints the black and white picture
for row in symbol_grid:
	print (''.join(row))