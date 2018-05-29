from dateutil.parser import parse
from dateutil import rrule
from datetime import datetime
import math
import pytz

# parse the user inputted string into a datetime object
# if no timezone offset is specified set it to UTC
# returns a datetime object
def validate_date(date)	:
	ret = parse(date)
	if ret.tzinfo is None or ret.tzinfo.utcoffset(ret) is None :
		return ret.replace(tzinfo=pytz.utc)
	else :
		print('timezone info exists')
		return ret

# returns the timedelta object of two datetime objects
# allows end result to be formatted in seconds or days, depending on what is needed
def day_diff(start_date, end_date):
	return end_date-start_date

# calculates weekdays between dates, assumes a work week of Monday - Friday
def weekday_diff(start_date, end_date):
	no_work = 5, 6 # Sat and Sun
	work = [x for x in range(7) if x not in no_work]
	if start_date > end_date :
		days = rrule.rrule(rrule.DAILY, dtstart=end_date, until = start_date, byweekday = work)
	else :	
		days = rrule.rrule(rrule.DAILY, dtstart=start_date, until = end_date, byweekday = work)
	return int(days.count())

# calculates number of complete weeks between dates	
def week_diff(start_date, end_date):
	days = abs(day_diff(start_date, end_date).days)
	return(math.floor(days/7))

#format numbers so they are more readable, with commas every 1000	
def format_num(num) :
	return "{:,}".format(num)
	
#validate the selection, to be used for any menu options
def selection(option, valid) :	
	if option in valid :
		return option.upper()
	else :
		print('Invalid selection, please try again!\n')
		return False		

def exit() :
	print('Exiting Date-Diff...\n')
	raise SystemExit
		
# conversion of days into various units as specified by requirements
def days_in_secs(days) :
	return format_num(days*24*60*60)
	
def days_in_mins(days) :
	return format_num(days*24*60)
	
def days_in_hrs(days) :
	return format_num(days*24)
	
def days_in_yrs(days) :
	return format_num(round(days/365, 2)) #rounding? assumed 2 decimal places

print('Welcome to Date-Diff, for all your date calculations!')	
	
while True :	
	try :	
		start = input('Enter a starting datetime:\n')
		parse_start = validate_date(start)	
		break
	except ValueError:
		print('Invalid date format!\n')

while True :	
	try :	
		end = input('Enter an end datetime:\n')
		parse_end = validate_date(end)		
		break
	except ValueError:
		print('Invalid date format!\n')		

#initial calculations as specified by requirements
days = abs(day_diff(parse_start, parse_end).days)
weekdays = weekday_diff(parse_start, parse_end)
weeks = week_diff(parse_start, parse_end)

#format inputted datetimes for output
fstart = parse_start.strftime("%Y-%m-%d %H:%M:%S %z")
fend = parse_end.strftime("%Y-%m-%d %H:%M:%S %z")

#print out all calculations as originally specified
print('Between the dates '+ fstart + ' and ' + fend + '...\n')
print('There are ' + format_num(days) + ' days, ' + format_num(weekdays) + ' weekdays and ' + format_num(weeks) + ' complete weeks\n')

#prompt for optional conversion of result into different units
while True :
	option = input('View results in a different unit?\n [Y]es [N]o\n')	
	valid = ['Y', 'y', 'N', 'n']
	check = selection(option, valid)
	if check == 'Y' :
		seconds = abs(day_diff(parse_start, parse_end).total_seconds())
		while True :
			unit = input('Select a unit to display results\n [S]econds, [M]inutes, [H]hours, [Y]ears, [Q]uit\n')
			list = ['S', 's', 'M', 'm', 'H', 'h', 'Y', 'y', 'Q', 'q']
			valid = selection(unit, list)		
			if valid :			
				if valid == 'S' :
					val = format_num(int(seconds))
					textunit = ' seconds'
					wval = days_in_secs(weekdays)
					cval = days_in_secs(weeks*7)
				elif valid == 'M' :
					val = format_num(int(seconds/60))
					textunit = ' minutes'
					wval = days_in_mins(weekdays)
					cval = days_in_mins(weeks*7)
				elif valid == 'H' :
					val = format_num(int(seconds/60/60))
					textunit = ' hours'
					wval = days_in_hrs(weekdays)
					cval = days_in_hrs(weeks*7)				
				elif valid == 'Y' :
					val = format_num(round(seconds/60/60/24/365, 2))
					textunit = ' years'
					wval = days_in_yrs(weekdays)
					cval = days_in_yrs(weeks*7)
				elif valid == 'Q' :
					exit()
				
				print('Displaying results in' + textunit + '...\n')		
				print('Between the dates '+ fstart + ' and ' + fend + '...\n')		
				print('There are ' + val + textunit + ',\n')
				print(format_num(weekdays) + ' weekdays, or ' + wval + textunit + '\n')
				print('and ' + format_num(weeks) + ' complete weeks, or ' + cval + textunit + '\n')
			else :
				#print out all calculations as originally specified
				print('Between the dates '+ fstart + ' and ' + fend + '...\n')
				print('There are ' + format_num(days) + ' days, ' + format_num(weekdays) + ' weekdays and ' + format_num(weeks) + ' complete weeks\n')
	elif check == 'N' :
		exit()