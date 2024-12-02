from PIL import image
import numpy as np

def list_to_image(img_list):
    #convert a 2d list to an image
    img_arr = np.uint8(np.asarray(img_list))
    img = image.fromarray(img_arr)
    return img

def image_to_list(img):
    '''Converts an image to a 2D list.'''
    img_arr = np.uint8(np.asarray(img))
    pixels = img_arr.tolist()
    for row in range(len(pixels)):
        for col in range(len(pixels[row])):
            pixels[row][col] = (pixels[row][col][0], pixels[row][col][1], pixels[row][col][2])
    return pixels
