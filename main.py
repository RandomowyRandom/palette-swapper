from imageloader import getColors, getPixelMap
from pixelconverter import getNewPixelMap
from PIL import Image
import os


def main():

    # load input image
    image_pixel_map, image_width, image_height = getPixelMap(
        "./input/testImage.png")

    # load target color palette
    color_palette = getColors("./input/palette.png")

    # convert input image to use target color palette
    new_pixel_map = getNewPixelMap(
        image_pixel_map, color_palette, image_width, image_height)

    # save converted image
    new_image = Image.new("RGB", (image_width, image_height))

    for x in range(image_width):
        for y in range(image_height):
            new_image.putpixel((x, y), new_pixel_map[x, y])

    # check if output folder exists, if not create it
    if not os.path.exists("./output"):
        os.makedirs("./output")

    new_image.save("./output/output.png")


if __name__ == '__main__':
    main()
