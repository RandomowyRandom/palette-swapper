import numpy


def getClosestColor(color_palette, color):

    color_palette = numpy.array(color_palette)
    color = numpy.array(color)

    distances = numpy.sqrt(numpy.sum((color_palette-color)**2, axis=1))
    index_of_smallest = numpy.where(distances == numpy.amin(distances))
    smallest_distance = color_palette[index_of_smallest]
    return smallest_distance


def getNewPixelMap(pixel_map, color_palette, width, height):

    # iterate through each pixel in the image
    for x in range(width):
        for y in range(height):
            # get the closest color in the palette to the current pixel
            closest_color = getClosestColor(color_palette, pixel_map[x, y])
            # set the pixel to the closest color
            pixel_map[x, y] = (
                closest_color[0][0], closest_color[0][1], closest_color[0][2])

    return pixel_map
