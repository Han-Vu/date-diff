# Date-Diff
This script finds the difference between two dates/datetimes, with the option to convert the result to seconds, minutes, hours or years.

Values entered may contain dates, times and timezones.

Output will display the number of days between the two dates, number of weekdays between dates, and number of complete weeks between dates.

The user can then optionally format these results in either seconds, minutes, hours or years.

## Getting Started
This script was developed using Python 3.6.5

### Prerequisites
This script makes use of the [dateutil](https://pypi.org/project/python-dateutil/) and [pytz](https://pypi.org/project/pytz/) modules. They can be installed using the following:
``` 
pip install python-dateutil 
```
``` 
pip install pytz 
```
## Usage
The script can be run by either by opening the date-diff.py file, or by running it from the command prompt:
```
directory\to\the\script\date-diff.py
```

The user will be prompted for a starting and ending date time. Date-Diff accepts both dates and datetimes. For example:

20180529T20:15:00
29/05/2018 8:15PM
29 May 2018 8:15PM +0930

### Considerations
dateutil will reverse the timezone offset sign when parsing datetime strings with UTC offset. For example, 29/05/2018 20:15:00 UTC+0930 will be parsed as 29/05/2018 20:15:00 -0930. As such, it is not suggested that timezones be specified in this manner.