from PIL import Image


def getPixelMap(imagePath: str):

    image = Image.open(imagePath).convert('RGB')
    pixel_map = image.load()
    image.getpalette()
    width, height = image.size

    return pixel_map, width, height


def getColors(imagePath: str):

    with Image.open(imagePath).convert('RGB') as image:
        pixel_map = image.load()

    width, height = image.size

    pixel_array = [[]]
    for x in range(width):
        for y in range(height):
            pixel_array[x] = [pixel_map[x, y][0],
                              pixel_map[x, y][1], pixel_map[x, y][2]]

        pixel_array.append([])

    pixel_array.pop()

    return pixel_array
