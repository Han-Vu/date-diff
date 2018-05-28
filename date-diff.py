install_requires=['dateutil']
from dateutil.parser import parse
from dateutil import rrule
from datetime import datetime
import math

"""
This script finds the difference between two dates/datetimes, with the option to convert the result to seconds, minutes, hours or years.

values entered may contain dates, times and timezones

First prompt is for the starting datetime
Second prompt is for the end datetime

Output will contain the number of days between the two dates, number of weekdays between dates, and number of complete weeks between dates

The user can then optionally format these results (format options: 's', 'm', 'h', 'y' for seconds, minutes, hours, years respectively)

valid dates:
check_date('20180522T20:50:10 +0930')
check_date('20180522T20:50:10+0930')

"""

#validate the selection
def selection(option) :
	valid = ['D', 'd', 'W', 'w', 'C', 'c', 'Q', 'q']
	if option in valid :
		return option.upper()
	else :
		print('Invalid selection, please try again\n')
		return		
		
# calculates number of days dates	
def day_diff(start_date, end_date):
	return (end_date-start_date).days
	
# calculates weekdays between dates	
# assumes Monday - Friday but can be changed
# list of public holidays to exclude?
def weekday_diff(start_date, end_date):
	no_work = 5, 6 # Sat and Sun
	work = [x for x in range(7) if x not in no_work]
	days = rrule.rrule(rrule.DAILY, dtstart=start_date, until = end_date, byweekday = work)
	return days.count()
	
# calculates number of complete weeks between dates	
def week_diff(start_date, end_date):
	return(math.floor(day_diff(start_date, end_date)/7))
	
#Checks if a given string corresponds to a datetime string
def check_date(date_string) :
	try:
		val = parse(date_string)
	except ValueError:
		print('Invalid date format\n')
		print('Quitting...\n')
		raise SystemExit
	return val
	
#does not factor in difference in time, due to requirement (convert result of (1,2,3) into seconds)	
def days_in_secs(days) :
	return days*24*60*60
def days_in_mins(days) :
	return days*24*60
def days_in_hrs(days) :
	return days*24
def days_in_yrs(days) :
	return days/365
	
start = input('Enter a starting datetime\n')
parse_start = check_date(start)

end = input('Enter an end datetime\n')
parse_end = check_date(end)


select = input('Select a date difference to be calculated.\n [D]ays, [W]eekdays, [C]omplete weeks, [Q]uit\n')
case = selection(select)
#while True :
if case == 'D' :
	val = str(day_diff(parse_start, parse_end))
	print(val + ' days')
elif case == 'W' :
	val = str(weekday_diff(parse_start, parse_end))
elif case == 'C' :
	val = str(week_diff(parse_start, parse_end))
elif case == 'Q' :
	print('Quitting...\n')
	#break
	raise SystemExit
else :
	print('Please enter a selection\n')
		
#display results