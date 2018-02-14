import datetime, calendar

"""
function for displaying definite month of definite year

$ print create_calendar_page(1)
'--------------------
MO TU WE TH FR SA SU
--------------------
01 02 03 04 05 06 07
08 09 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31'


$ print create_calendar_page()
'--------------------
MO TU WE TH FR SA SU
--------------------
         01 02 03 04
05 06 07 08 09 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28'

$ print create_calendar_page(4, 1992)

'--------------------
MO TU WE TH FR SA SU
--------------------
      01 02 03 04 05
06 07 08 09 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30'



"""

def create_calendar_page(month = 2, year = 2018) :	#default values of month and year are today's month and year
	begin = 20 * '-' + '\nMO TU WE TH FR SA SU\n' + 20 * '-' + '\n'	#preparation
	result = begin
	days = calendar.monthrange(year, month)[1]	#variable for storing number of days in that month
	day = datetime.datetime(year, month, 1)	#variable for day
	current_day = 1	#first day of month
	for d in range(days) :	#iterate through all month
		day_week = day.weekday()	#variable for day of week
		if current_day <= 9 :	#if day is 1..9 
			str_day = '0' + str(current_day)	#add '0' and convert to str-type
		else :
			str_day = str(current_day)	#convert to str-type
		
		if current_day == 1 :	#if it is first day of month
			result += 3 * ' ' * day_week + str_day
		else :
			result += str_day
		
		if day_week != 6 and d != days - 1:	#if the day is not the last in the week and in the month
			result += ' '
		
		if day_week == 6 :	#if the day is sunday
			result += '\n'
		

		current_day += 1	#increment the variable of day
		if current_day in range(days + 1) : #search currend_day in days
			day = datetime.datetime(year, month, current_day) 	#update day-variable
	return result
