from PIL import Image

image = Image.open('out copy.jpg')

# Get the image pixel values
pix_val = list(image.getdata())
# Start at the beginning of the list, step through pixels by desired height value
splited = [pix_val[i::92] for i in range(92)]

# Set height and width
h, w = 92, 304
# Create new image
new_image = Image.new("RGB",(w, h))
pix = new_image.load()
# Tell the program how to split by height
for y in range(h):
    line = splited[y]
# For each split line set the r g b values
    for x in range(w):
        r, g, b = line[x]
        pix[x, y] = (r, g, b)
new_image.save("out1.jpg", "JPEG")
