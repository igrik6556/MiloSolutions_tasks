import itertools
import datetime


DAYS_IN_MONTH = {1: 31, 2: [28, 29],
                 3: 31, 4: 30,
                 5: 31, 6: 30,
                 7: 31, 8: 31,
                 9: 30, 10: 31,
                 11: 30, 12: 31}


def form_nums(raw_nums):
    nums = raw_nums.split("/")
    possible_dates = []
    for item in itertools.permutations(nums, len(nums)):
        (year, month, day) = item
        try:
            needed_year = is_year(year)
            needed_month = is_month(month)
            needed_day = is_day(day, needed_month, needed_year)
            possible_dates.append("%d-%02d-%02d" % (needed_year, needed_month, needed_day))
        except ValueError:
            continue
    if possible_dates:
        possible_dates = sorted(possible_dates, key=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
        needed_date = possible_dates[0]
    else:
        needed_date = "%s is illegal" % (raw_nums)

    return needed_date


def is_year(y):
    int_year = int(y)
    if len(y) != 4:
        int_year += 2000
        
    if int_year in range(2000, 3000):
        return int_year

    raise ValueError


def is_month(m):
    int_month = int(m)
    if int_month in range(1, 13):
        return int_month

    raise ValueError


def is_day(d, m, y):
    int_day = int(d)
    max_days = DAYS_IN_MONTH[m]
    if m == 2:
        if leap_year(y):
            max_days = 29
        else:
            max_days = 28
    if int_day in range (1, max_days+1):
        return int_day

    raise ValueError


def leap_year(year):
    year = int(year)
    if year % 4 == 0 and year % 100 != 0:
        is_leap = True
    elif year % 400 == 0:
        is_leap = True
    else:
        is_leap = False
    return is_leap
    

if __name__ == '__main__':
    f = open('date.txt', 'r')
    s = f.read().strip()
    date = form_nums(s)
    print('%s' % (date))
