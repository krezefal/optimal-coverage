# Optimal area coverage
Implementation of the algorithm for calculating the optimal area coverage
by base stations with specified power.

### Usage

`python3 coverage.py -w WIDTH -l LENGTH -p POWER -pmin POWER_MIN`

```
Usage: coverage.py -w WIDTH -l LENGTH -p POWER -pmin POWER_MIN [-i] [-h]

Options:
  -w WIDTH, --width WIDTH
                        Width of the area to cover.
  -l LENGTH, --length LENGTH
                        Length of the area to cover.
  -p POWER, --power POWER
                        Stations power.
  -pmin POWER_MIN, --power_min POWER_MIN
                        Stations minimal power acceptable for users.
  -i, --image           Show an image with optimal location of base stations in the area.
  -h, --help            Show this help message and exit.
```

### Image meaning

1. **Black points** -- base stations on the area;
2. **Bright green area** -- area generated by user parameters (scale 1:1pix);
3. **Dark green area** -- area on which it is necessary to place part of 
the base stations to cover the area specified by the user (bright green 
area). This area ends where the signal from the extreme base stations for
the end user becomes less than the specified minimum (P<sub>t</sub> < 
P<sub>min</sub>).

<p align="center">
    <img src="example-img/test_img.bmp" alt/>
</p>

<p align="center">
    <em> Test image </em>
</p>
