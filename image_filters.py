from PIL import Image
from image_converter import list_to_image, image_to_list
import random
import numpy as np

# Example filter
def darken(pixels):
    new_pixels = []
    for row in range(len(pixels)):
        new_row = []
        for col in range(len(pixels[row])):
            r, g, b = pixels[row][col]
            new_row.append((r / 2, g / 2, b / 2))
        new_pixels.append(new_row)
    return new_pixels

# Add your functions here.
def rotated_180(pixels):
    new_pixels = []
    for row in range(len(pixels)):
        new_row = []
        for col in range(len(pixels[row])):
            rotation = pixels[len(pixels) - 1 - row][len(pixels) - 1 - col]
            new_row.append(rotation)
            #r, g, b = pixels[row][col]
            #new_row.append((r / 2, g / 2, b / 2))
        new_pixels.append(new_row)
    return new_pixels

def rotated_90(pixels):
    new_pixels = []
    for row in range(len(pixels)):
        new_row = []
        for col in range(len(pixels[row])):
            rotation = pixels[len(pixels) - 1 - col][len(pixels) - 1 - row]
            new_row.append(rotation)
        new_pixels.append(new_row)
    return new_pixels


def red_vert_stripe(pixels, length):
    new_pixels = []
    for row in range(len(pixels)):
        new_row = []
        for col in range(len(pixels[row])):
            r, g, b = pixels[row][col]
            if (col // length) % 2 == 0:
                stripes = (255, g, b)
            else:
                stripes = (r,g,b)
            new_row.append(stripes)
        new_pixels.append(new_row)
    return new_pixels

def invert(pixels):
    new_pixels = []
    for row in range(len(pixels)):
        new_row = []
        for col in range(len(pixels[row])):
            r, g, b = pixels[row][col]
            invertion = (255 - r, 255 - g, 255 - b)
            new_row.append(invertion)
        new_pixels.append(new_row)
    return new_pixels

def checker_stripe(pixels, length):
    new_pixels = []
    for row in range(len(pixels)):
        new_row = []
        for col in range(len(pixels[row])):
            r, g, b = pixels[row][col]
            if (col // length) % 2 == 0:  
                stripes = (255, g, b)
            else:
                if (row // length) % 2 == 0:
                    stripes = (225, g, b)
                else:
                    stripes = (r,g,b)
            new_row.append(stripes)

        new_pixels.append(new_row)
    return new_pixels


def red_hor_stripe(pixels, length):
    new_pixels = []
    for row in range(len(pixels)):
        new_row = []
        for col in range(len(pixels[row])):
            r, g, b = pixels[row][col]
            if (row // length) % 2 == 0:
                stripes = (255, g, b)
            else:
                stripes = (r,g,b)
            new_row.append(stripes)

        new_pixels.append(new_row)
    return new_pixels

def pink_flush(pixels):
    new_pixels = []
    for row in range(len(pixels)):
        new_row = []
        for col in range(len(pixels[row])):
            r, g, b = pixels[row][col]
            pink = (225 - r, 225 - g, 225 - b)
            new_row.append(pink)
        new_pixels.append(new_row)
    return new_pixels

def distort_image(pixels):
    new_pixels = []
    for row in range(len(pixels)):
        new_row = []
        for col in range(len(pixels[row])):
            r, g, b = pixels[row][col]
            pink = (r, g, b)
            #pink = (r - 225, g - 225, b - 225)
            new_row.append(pink)
        shuffle = random.shuffle(new_row)
        new_pixels.append(new_row)
    return new_pixels


# Open an image
pb_img = Image.open("bears.png")
pixels = image_to_list(pb_img)


# CALL YOUR FUNCTION HERE TO TEST IT OUT.
changed_pixels = darken(pixels)
rotate_pixels_180 = rotated_180(pixels)
rotate_pixels_90 = rotated_90(pixels)
red_vert_stripe = red_vert_stripe(pixels,5)
invert_img = invert(pixels)
checker_stripe = checker_stripe(pixels, 5)
red_hor_stripe = red_hor_stripe(pixels, 5)
pink_flush = pink_flush(pixels)
distort = distort_image(pixels)



# Save an image
new_pb_img = list_to_image(changed_pixels)
new_pb_img.save("filtered.png")

new_pb_img = list_to_image(rotate_pixels_180)
new_pb_img.save("rotate_img_180.png")

new_pb_img = list_to_image(rotate_pixels_90)
new_pb_img.save("rotate_img_90.png")

new_pb_img = list_to_image(red_vert_stripe)
new_pb_img.save("vertical red stripe.png")

new_pb_img = list_to_image(invert_img)
new_pb_img.save("Invert.png")

new_pb_img = list_to_image(checker_stripe)
new_pb_img.save("checker stripe.png")

new_pb_img = list_to_image(red_hor_stripe)
new_pb_img.save("horizontal red stripe.png")

new_pb_img = list_to_image(pink_flush)
new_pb_img.save("pink flush.png")

new_pb_img = list_to_image(distort)
new_pb_img.save("destroyed image.png")
