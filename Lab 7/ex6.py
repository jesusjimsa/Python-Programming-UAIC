# Write a script that writes the day of the week for the New Year Day,
# for the last x years (x is given as argument)

def datetoday(day, month, year):
	d = day
	m = month
	y = year
	
	if m < 3:
		z = y - 1
	
	else:
		z = y
	
	dayofweek = (23 * m//9 + d + 4 + y + z//4 - z//100 + z//400)
   
	if m >= 3:
		dayofweek -= 2
	
	dayofweek = dayofweek % 7
	
	return dayofweek

days =[ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' ]

years = int(raw_input("Write the number of years you want to visit "))

for y in reversed(range(2017 - years, 2018)):
	dayofweek = days[datetoday(1, 1, y) - 1]

	print y, "->", dayofweek