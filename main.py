#!/usr/bin/env python
import glob
import subprocess


def main():
    input_files_all = glob.glob("images/*.png")
    input_files = [
        x for x in input_files_all if "-resized.png" not in x and
        'cowboy-canvas' not in x and 'cowboy-hat' not in x]

    for filename in input_files:
        out_filename = filename.replace(".png", "-resized.png")
        print(filename, out_filename)
        cmd = 'convert {input} -gravity Center -background transparent -extent 100x100 {output}'\
            .format(input=filename, output=out_filename)

        subprocess.call(cmd, shell=True)

        composite_filename = "images_out/{base_filename}".format(base_filename=out_filename.split("/")[-1])
        print(composite_filename)
        cmd2 = 'convert {input} images/cowboy-canvas2.png -composite {output}'\
            .format(input=out_filename, output=composite_filename)

        subprocess.call(cmd2, shell=True)


if __name__ == '__main__':
    main()
