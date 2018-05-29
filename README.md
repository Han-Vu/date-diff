# Date-Diff
The purpose of this script is to find the difference between two dates/datetimes. It can also be treated as a script to familiarise myself with Python.

Date-Diff accepts datetime values containing dates, times and timezones.

Initial output will display the following:
1. The number of days between two dates
2. The number of days between two dates, excluding weekends
3. The number of complete weeks between two dates

The user can then optionally view these results in either seconds, minutes, hours or years.

## Getting Started
This script requires Python >=3.6.5

### Prerequisites
This script makes use of the [dateutil](https://pypi.org/project/python-dateutil/) and [pytz](https://pypi.org/project/pytz/) modules. They can be installed using the following commands:
``` 
pip install python-dateutil 
```
``` 
pip install pytz 
```
## Usage
Run the script from the command prompt:
```
directory\to\the\script\python date-diff.py
```

The user will be prompted for a starting and ending date time. Date-Diff accepts both dates and datetimes. For example:

* 20180529T20:15:00
* 29/05/2018 8:15PM
* 29 May 2018 8:15PM +0930

### Considerations
dateutil will reverse the timezone offset sign when parsing datetime strings with UTC offset. For example, 29/05/2018 20:15:00 UTC+0930 will be parsed as 29/05/2018 20:15:00 -0930. As such, it is not suggested that timezones be specified in this manner.