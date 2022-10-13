# Optimal area coverage
Implementation of the algorithm for calculating the optimal area coverage
by base stations with specified power.

### Usage

`python3 coverage.py -w WIDTH -l LENGTH -p POWER -pmin POWER_MIN`

```
options:
  -h, --help            show this help message and exit
  -w WIDTH, --width WIDTH
                        Width of the area to cover
  -l LENGTH, --length LENGTH
                        Length of the area to cover
  -p POWER, --power POWER
                        Stations power
  -pmin POWER_MIN, --power_min POWER_MIN
                        Stations minimal power acceptable for users
  -i, --image           Show an image with optimal location of base stations in the area
```