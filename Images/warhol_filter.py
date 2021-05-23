"""
This program generates the Warhol effect based on the original image.
"""

import random

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'
MAX_RANDOM = 1.5

def make_recolored_patch(red_scale, green_scale, blue_scale):
    # making and returning colored patch
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch

def place_patch(pos_x, pos_y, final_image, patch):
    # placing the patch in passed initial coordinates in the matrix
    for x in range (patch.width):
        for y in range (patch.height):
            final_image.set_pixel(x + pos_x, y + pos_y, patch.get_pixel(x, y))

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    for x in range (N_COLS):
        for y in range (N_ROWS):
            # applying colorization to the patch
            patch = make_recolored_patch(random.uniform(0, MAX_RANDOM), random.uniform(0, MAX_RANDOM), random.uniform(0, MAX_RANDOM))
            # placing the colored patch to the final matrix passing initial coordinates to the function
            place_patch(x * PATCH_SIZE, y * PATCH_SIZE, final_image, patch)
    final_image.show()

if __name__ == '__main__':
    main()
