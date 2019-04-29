#!/usr/bin/env python

import glob
import json
import math
import subprocess

from PIL import Image

COORDINATES_PATH = "assets/coordinates.json"
COWBOY_HAT_PATH = "assets/cowboy-hat.png"


def read_image(emoji_name):
    image = Image.open('assets/ios/{name}-2.png'.format(name=emoji_name))
    return image


def transform_image(emoji_name, image, coordinates):
    hat_image = Image.open(COWBOY_HAT_PATH)

    image_width, image_height = coordinates[emoji_name]["size"]
    image = image.resize((image_width, image_height), resample=Image.BICUBIC)

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


def main():
    coordinates_file = open(COORDINATES_PATH, "r")
    coordinates = json.load(coordinates_file)
    coordinates_file.close()

    faces = ["1f600", "1f603", "1f604", "1f601", "1f606", "1f605", "1f923", "1f602", "1f642", "1f643", "1f609", "1f60a", "1f607", "1f970", "1f60d", "1f929", "1f618", "1f617", "263a", "1f61a", "1f619", "1f60b", "1f61b", "1f61c", "1f92a", "1f61d", "1f911", "1f917", "1f92d", "1f92b", "1f914", "1f910", "1f928", "1f610", "1f611", "1f636", "1f60f", "1f612", "1f644", "1f62c", "1f925", "1f60c", "1f614", "1f62a", "1f924", "1f634", "1f637", "1f912", "1f915", "1f922", "1f92e", "1f927", "1f975", "1f976", "1f974", "1f635", "1f92f", "1f920", "1f973", "1f60e", "1f913", "1f9d0", "1f615", "1f61f", "1f641", "2639", "1f62e", "1f62f", "1f632", "1f633", "1f97a", "1f626", "1f627", "1f628", "1f630", "1f625", "1f622", "1f62d", "1f631", "1f616", "1f623", "1f61e", "1f613", "1f629", "1f62b", "1f624", "1f621", "1f620", "1f92c", "1f608", "1f47f", "1f480", "2620"]

    for face_unicode in faces:
        emoji_name = next(k for k in coordinates.keys() if k.endswith(face_unicode))
        image = read_image(emoji_name)
        cowboyfied_image = transform_image(emoji_name, image, coordinates)
        write_output_image(cowboyfied_image, "test/{name}.png".format(name=emoji_name))

    # for filename in input_files:
    #     out_filename = filename.replace(".png", "-resized.png")
    #     print(filename, out_filename)
    #     cmd = 'convert {input} -gravity Center -background transparent -extent 100x100 {output}'\
    #         .format(input=filename, output=out_filename)

    #     subprocess.call(cmd, shell=True)

    #     composite_filename = "images_out/{base_filename}".format(base_filename=out_filename.split("/")[-1])
    #     print(composite_filename)
    #     cmd2 = 'convert {input} images/cowboy-canvas2.png -composite {output}'\
    #         .format(input=out_filename, output=composite_filename)

    #     subprocess.call(cmd2, shell=True)


if __name__ == '__main__':
    main()
