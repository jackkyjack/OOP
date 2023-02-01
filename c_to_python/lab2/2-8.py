day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
def day_of_year(day, month ,year):
    day_of_years = 0
    if (is_leap(year)):
        day_in_month[2] = 29
    else:
        day_in_month[2] = 28
    for i in range(month):
        day +=day_in_month[i]
    day_of_years += day
    return day_of_years
def date_diff(date1,date2):
    start = [int(x) for x in date1.split("-")]
    last = [int(x) for x in date2.split("-")]
    day = 0
    for i in range(start[2],last[2]):
        day +=day_in_year(i)
    dayday = day - day_of_year(start[0],start[1],start[2]) + day_of_year(last[0],last[1],last[2])
    return dayday + 1
def day_in_year(year):
    if is_leap(year): return 366
    else : return 365
def is_leap(year):
    return year % 4 ==0 and (year %100 != 0 or year%400 == 0)