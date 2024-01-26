input_month = input('Enter month: ')
input_day = int(input('Enter day of month: '))
final_season = ''

# Lists for months

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

spring_months = ['March', 'April', 'May', 'June']

summer_months = ['June', 'July', 'August', 'September']

autumn_months = ['September', 'October', 'November', 'December']

winter_months = ['December', 'January', 'February', 'March']

# Input Check

if (input_day < 1 or input_day > 31 or input_month not in months or
        (input_month in [months[1], months[3], months[5], months[8], months[10]] and input_day == 31)):

    print('Invalid')
else:

    # Spring

    if input_month in spring_months[1:3]:
        print('Spring')
        final_season = 'Spring'
    elif input_month == spring_months[0]:
        if input_day >= 20:
            print('Spring')
            final_season = 'Spring'
    elif input_month == spring_months[3]:
        if input_day <= 20:
            print('Spring')
            final_season = 'Spring'

    # Summer

    if input_month in summer_months[1:3]:
        print('Summer')
        final_season = 'Summer'
    elif input_month == summer_months[0]:
        if input_day >= 21:
            print('Summer')
            final_season = 'Summer'
    elif input_month == summer_months[3]:
        if input_day <= 21:
            print('Summer')
            final_season = 'Summer'

    # Autumn

    if input_month in autumn_months[1:3]:
        print('Autumn')
        final_season = 'Autumn'
    elif input_month == autumn_months[0]:
        if input_day >= 22:
            print('Autumn')
            final_season = 'Autumn'
    elif input_month == autumn_months[3]:
        if input_day <= 20:
            print('Autumn')
            final_season = 'Autumn'

    # Winter

    if input_month in winter_months[1:3]:
        print('Winter')
        final_season = 'Winter'
    elif input_month == winter_months[0]:
        if input_day >= 21:
            print('Winter')
            final_season = 'Winter'
    elif input_month == winter_months[3]:
        if input_day <= 19:
            print('Winter')
            final_season = 'Winter'

print('The season for {}, {} is {}'.format(input_month, input_day, final_season))
