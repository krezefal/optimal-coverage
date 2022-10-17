from math import sqrt, floor
from colorama import Fore, Style

from utils import parse_args, render_image


def main():
    width, length, P, Pmin, image_flag = parse_args()

    if width == 0 or length == 0:
        print('0 STATION(S) ARE NEEDED TO COVER THIS AREA')
        return

    r_outer = floor(sqrt(P / Pmin))  # Round down
    r_inner = round(sqrt(0.75 * (r_outer ** 2)))  # Round to the nearest

    print(f'Radius of the base station at which Pt >= Pmin: {Fore.RED}{r_outer}{Style.RESET_ALL}')
    print(f'Inner circle radius of the hexagon inscribed in coverage circle: {Fore.RED}{r_inner}{Style.RESET_ALL}')

    # HORIZONTAL

    width_remainder = width % (2 * r_inner)

    stations_in_odd_row = width // (2 * r_inner)
    if width_remainder != 0:
        stations_in_odd_row += 1

    stations_in_even_row = stations_in_odd_row
    if width_remainder == 0 or width_remainder > r_inner:
        stations_in_even_row += 1

    print(f'Number of base stations in an odd row: {Fore.RED}{stations_in_odd_row}{Style.RESET_ALL}')
    print(f'Number of base stations in an even row: {Fore.RED}{stations_in_even_row}{Style.RESET_ALL}')

    # VERTICAL

    length_remainder = length % r_outer
    r_outer_num = length // r_outer

    if r_outer_num % 3 == 0:
        row_num = r_outer_num - (r_outer_num // 3 - 1)
    elif (r_outer_num + 1) % 3 == 0:
        row_num = r_outer_num - ((r_outer_num + 1) // 3 - 1)
    else:  # (r_outer_num + 2) % 3 == 0:
        row_num = r_outer_num - ((r_outer_num + 2) // 3 - 1)

    if length_remainder != 0 and r_outer_num != 0:
        if (r_outer_num + 1) % 3 == 0 and length_remainder > (r_outer / 2):
            row_num += 1
        elif r_outer_num % 3 == 0:
            row_num += 1
        elif (r_outer_num + 2) % 3 == 0:
            row_num += 1

    print(f'Number of rows: {Fore.RED}{row_num}{Style.RESET_ALL}')

    # FINAL CALCULATION && IMAGE CREATION

    optimal_station_num = (stations_in_odd_row + stations_in_even_row) * int(row_num / 2)
    if row_num % 2 != 0:
        optimal_station_num += stations_in_odd_row

    if image_flag is True:
        render_image(width, length, r_outer, r_inner, stations_in_odd_row, stations_in_even_row, row_num)

    print('-------------------------------------------------')
    print(f'{Fore.RED}{optimal_station_num}{Style.RESET_ALL} STATION(S) ARE NEEDED TO COVER THIS AREA')


if __name__ == "__main__":
    main()
