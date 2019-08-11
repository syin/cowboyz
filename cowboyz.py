#!/usr/bin/env python

import json
import math

from PIL import Image

COORDINATES_PATH = "assets/coordinates.json"
COWBOY_HAT_PATH = "assets/cowboy-hat.png"


def read_image(emoji_name):
    image = Image.open('static/assets/ios/{name}.png'.format(name=emoji_name))
    return image


def transform_image(emoji_name, image, coordinates):
    hat_image = Image.open(COWBOY_HAT_PATH)

    image_width, image_height = coordinates[emoji_name]["size"]
    image = image.resize((image_width, image_height), resample=Image.BICUBIC)
    # images with mode 'P' get converted to black background
    # https://github.com/scrapy/scrapy/issues/1037
    image = image.convert('RGBA')

    canvas_width = 160
    canvas_height = 160
    base_image = Image.new(image.mode, (canvas_width, canvas_height))

    offset_x, offset_y = coordinates[emoji_name]["offset"]
    base_image.paste(image, (offset_x, offset_y))

    if coordinates[emoji_name].get("hat_size"):
        hat_width, hat_height = coordinates[emoji_name]["hat_size"]
        hat_image = hat_image.resize((hat_width, hat_height), resample=Image.BICUBIC)

    if coordinates[emoji_name].get("rotation"):
        hat_image = hat_image.rotate(
            coordinates[emoji_name]["rotation"], resample=Image.BICUBIC, expand=1)

    if coordinates[emoji_name].get("hat_offset"):
        hat_offset = coordinates[emoji_name]["hat_offset"]
    else:
        hat_offset = (0, 0)

    base_image.paste(hat_image, hat_offset, hat_image)
    return base_image


def resize_image(image, max_image_size):
    ratio = image.size[0] / image.size[1]
    new_width = min(max_image_size, image.size[0])
    new_height = math.floor(new_width / ratio)
    return image.resize((new_width, new_height))


def write_output_image(image, in_filename):
    filename_base = ".".join(in_filename.split(".")[:-1])
    filename_ext = in_filename.split(".")[-1]
    out_filename = "{filename_base}_cowboyz.{filename_ext}"\
        .format(filename_base=filename_base, filename_ext=filename_ext)
    image.save(out_filename, optimize=True)


def cowboize(emoji_name):
    coordinates_file = open(COORDINATES_PATH, "r")
    coordinates = json.load(coordinates_file)
    coordinates_file.close()
    image = read_image(emoji_name)
    cowboyfied_image = transform_image(emoji_name, image, coordinates)
    write_output_image(cowboyfied_image, "static/output/{name}.png".format(name=emoji_name))
    return True
