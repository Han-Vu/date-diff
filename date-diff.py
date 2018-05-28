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
		
# calculates number of seconds between dates	
def day_diff_seconds(start_date, end_date):
	return int((end_date-start_date).total_seconds())

# calculates number of days between dates	
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
	
# does not factor in time differences, due to requirement (convert result of (1,2,3) into seconds, not 
# the original datetime parameters)	
def days_in_secs(days) :
	return days*24*60*60
def days_in_mins(days) :
	return days*24*60
def days_in_hrs(days) :
	return days*24	
def days_in_yrs(days) :
	return round(days/365, 2) #rounding?

#format numbers so they are more readable, with commas every 1000	
def format_num(num) :
	return "{:,}".format(num)
	
while True :	
	try :	
		start = input('Enter a starting datetime:\n')
		parse_start = parse(start)
		end = input('Enter an end datetime:\n')
		parse_end = parse(end)		
		break
	except ValueError:
		print('Invalid date format\n')

#initial calculations as specified by requirements		
days = day_diff(parse_start, parse_end)
weekdays = weekday_diff(parse_start, parse_end)
weeks = week_diff(parse_start, parse_end)
seconds = day_diff_seconds(parse_start, parse_end)

#format inputted datetimes for output
fstart = parse_start.strftime("%Y-%m-%d %H:%M:%S %z")
fend = parse_end.strftime("%Y-%m-%d %H:%M:%S %z")

#print out all calculations as originally specified
print('There are ' + str(days) + ' days between ' + fstart + ' and ' + fend)
print('There are ' + str(weekdays) + ' weekdays between ' + fstart + ' and ' + fend)
print('There are ' + str(weeks) + ' complete weeks between ' + fstart + ' and ' + fend)

#prompt for optional conversion of result into different formats
while True :
	option = input('View results in different unit?\n[Y]es [N]o\n')
	if option in ['Y', 'y'] :
		unit = input('Select a unit to display results\n [S]econds, [M]inutes, [H]hours, [Y]ears, [Q]uit\n')
		val = str(days)
		textunit = ' days'
		wsecs = str(weekdays)
		csecs = str(weeks)
		if unit in ('S', 's') :
			val = str(seconds)
			textunit = ' seconds'
			wsecs = str(days_in_secs(weekdays))
			csecs = str(days_in_secs(weeks*7))
		elif unit in ('M', 'm') :
			val = str(seconds/60)
			textunit = ' minutes'
			wsecs = str(days_in_mins(weekdays))
			csecs = str(days_in_mins(weeks*7))
		elif unit in ('H', 'h') :
			val = str(seconds/60/60)
			textunit = ' hours'
			wsecs = str(days_in_hrs(weekdays))
			csecs = str(days_in_hrs(weeks*7))				
		elif unit in ('Y', 'y') :
			val = str(round(seconds/60/60/24/365, 2))
			textunit = ' years'
			wsecs = str(days_in_yrs(weekdays))
			csecs = str(days_in_yrs(weeks*7))
		elif unit in ('Q', 'q') :
			print('Exiting Date-Diff...\n')
			raise SystemExit
		else :
			print('Invalid selection, please try again')
		print('There are ' + val + textunit + ' between ' + fstart + ' and ' + fend)
		print('There are ' + str(weekdays) + ' weekdays, or ' + wsecs + textunit + ' between ' + fstart + ' and ' + fend)
		print('There are ' + str(weeks) + ' complete weeks, or ' + csecs + textunit + ' between ' + fstart + ' and ' + fend)
		
	elif option in ['N', 'n'] :
		print('Exiting Date-Diff...\n')
		raise SystemExit
	else :
		print('Invalid selection, please try again')