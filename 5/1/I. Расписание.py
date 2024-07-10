def is_leap ( year ):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 1
    return 0

def week_day(day, month, year, day_of_week):
    weekday = day_of_week + day - 1
    dict_of_monthday = {
        'January': 31,
        'February': 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'October': 31,
        'November': 30,
        'December': 31
    }
    for i in dict_of_monthday:
        if i == month:
            break
        if i == 'February':
            weekday += is_leap(year)
        weekday += dict_of_monthday[i]

    return weekday % 7

N = int(input())
year = int(input())
holidays = []
for i in range(N):
    day, month = map(str, input().split())
    holidays.append([int(day), month])
day_of_week = input()

days_in_year = 365 + is_leap(year)
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
start = 0
for i in range(7):
    if weekdays[i] == day_of_week:
        start = i
        break

weekdays_count = [days_in_year // 7 for i in range(7)]
days_in_year = days_in_year % 7
i = 0
while days_in_year:
    weekdays_count[(i + start) % 7] += 1
    days_in_year -= 1
    i += 1


for [x, y] in holidays:
    weekdays_count[week_day(x, y, year, start)] -= 1

worst_chose = 0
worst_chose_day = 0
best_chose = 90
best_chose_day = 0
for i in range(7):
    if weekdays_count[i] > worst_chose:
        worst_chose = weekdays_count[i]
        worst_chose_day = i
    if weekdays_count[i] < best_chose:
        best_chose = weekdays_count[i]
        best_chose_day = i
print(weekdays[worst_chose_day], end=' ')
print(weekdays[best_chose_day])
