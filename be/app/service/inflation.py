# inflation in per cents from 2018 to 1999. Data from RosStat
INFLATION_RATE = [4.3, 2.5, 5.4, 12.90, 11.36, 6.45, 6.58, 6.10, 8.78, 8.80, 13.28,
                  11.87, 9, 10, 91, 11.74, 11.99, 15.06, 18.8, 20.1, 36.6]
CURRENT_YEAR = 2019


def calc_inflation(income, year):
    year_diff = CURRENT_YEAR - year
    for i in range(0, min(year_diff, 20)):
        income = income / (1 + INFLATION_RATE[i] / 100.0)

    return income
