import argparse
import os
# import pathlib
# import subprocess
import PIL.Image

GREEN = (23, 125, 54)
DARK_GREEN = (17, 91, 39)
BLACK = (0, 0, 0)


class CapitalisedHelpFormatter(argparse.HelpFormatter):
    def add_usage(self, usage, actions, groups, prefix=None):
        if prefix is None:
            prefix = 'Usage: '
        return super(CapitalisedHelpFormatter, self).add_usage(
            usage, actions, groups, prefix)


def dir_path(path: str):
    if not os.path.exists(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"File {path} already exists")


def parse_args() -> tuple[int, int, float, float, str]:
    parser = argparse.ArgumentParser(add_help=False, formatter_class=CapitalisedHelpFormatter)
    parser._optionals.title = 'Options'

    parser.add_argument('-w', '--width', help='Width of the area to cover.',
                        required=True, type=int, metavar='WIDTH')
    parser.add_argument('-l', '--length', help='Length of the area to cover.',
                        required=True, type=int, metavar='LENGTH')
    parser.add_argument('-p', '--power', help='Stations power.',
                        required=True, type=float, metavar='POWER')
    parser.add_argument('-pmin', '--power_min', help='Stations minimal power acceptable for users.',
                        required=True, type=float, metavar='POWER_MIN')
    parser.add_argument('-i', '--image', help='Create an image with optimal location of base stations in the area '
                                              'and save it under the provided name (with specified extension).',
                        required=False, type=dir_path, metavar='FILENAME')
    parser.add_argument('-h', '--help', help='Show this help message and exit.', default=argparse.SUPPRESS,
                        action='help')

    args = parser.parse_args()
    return args.width, args.length, args.power, args.power_min, args.image


def render_image(width: int, length: int, r_outer: int, r_inner: int,
                 stations_in_odd_row: int, stations_in_even_row: int, row_num: int, image_path: str):

    if stations_in_odd_row < stations_in_even_row and row_num > 1:
        img_width = r_inner + 2 * r_inner * stations_in_odd_row
    else:
        img_width = 2 * r_inner * stations_in_odd_row

    img_len = r_outer // 2 + row_num * round(r_outer * 1.5)

    stations_location_img = PIL.Image.new(mode="RGB", size=(img_width, img_len), color=DARK_GREEN)

    for i in range(length):
        for j in range(width):
            stations_location_img.putpixel((j, i), GREEN)

    row_counter = 1
    for i in range(r_outer // 2, img_len, round(r_outer * 1.5)):
        if row_counter % 2 != 0:
            for j in range(r_inner, img_width, r_inner * 2):
                stations_location_img.putpixel((j, i), BLACK)
        else:
            for j in range(0, img_width, r_inner * 2):
                stations_location_img.putpixel((j, i), BLACK)
        row_counter += 1

    stations_location_img.save(image_path)

    # Execute an external program for rendering the Voronoi diagram for saved image
    # (https://github.com/krezefal/voronoi-diagram)

    # USE ONLY WITH ABSOLUTE PATH

    # subprocess.call(['python', 'voronoi-diagram/voronoi.py', image_path], cwd=pathlib.Path.home())
