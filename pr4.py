#my python program salary 1.0. program calculates ur weekly salary. it pays you 1.5 times extra money for extra hours (above 40 hours)
print 'Step 2\n', 'I gonna calculate ur salary,\n'
try:
    hours = raw_input('Enter hours u worked this week\n')
    hours = float(hours)
    rate = raw_input('Enter ur rate\n')
    rate = float(rate)
except:
    print 'Only numbers are allowed. do again,\n'
    hours = raw_input('Enter hours u worked this week\n')
    hours = float(hours)
    rate = raw_input('Enter ur rate\n')
    rate = float(rate)
print 'your hours worked: ', hours, ' hours ', 'ur rate is: ', rate, ' per hour, '
if hours <= 40:
    sal = hours * rate
    print 'ur salary this week is \n\n', sal
else: 
    hours_extra = hours - 40
    rate_extra = rate * 1.5
    sal = hours * rate
    sal_extra = hours_extra * rate_extra
    sal = sal + sal_extra
print 'congrats Mr, u worked ', hours, ' hours\n', ' ur salary is ', sal, ' european dollars\n'