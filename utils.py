import argparse


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-w', '--width', help='Width of the area to cover', required=True, type=int)
    parser.add_argument('-l', '--length', help='Length of the area to cover', required=True, type=int)
    parser.add_argument('-p', '--power', help='Stations power', required=True, type=float)
    parser.add_argument('-pmin', '--power_min', help='Stations minimal power acceptable for users',
                        required=True, type=float)

    args = parser.parse_args()

    return args.width, args.length, args.power, args.power_min
