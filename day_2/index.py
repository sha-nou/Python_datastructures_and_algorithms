#this is used to comment any code that is unused
"""
this 
will not 
be read
"""
print('hello world')
#User input age and it is displayed in days
#case 1 
x = input('enter your age ')

#Age is multiplied by 365 days which is total number of days in a year

age_in_days = int(x)*365

#display the age  in days
print('your age in days is :', age_in_days)

#case 2 Using datetime method

#import datetime
import datetime
birth_date ='2006 06 12'
#define the date format
date_format='%Y %M %d'
#convert the string birth date to datetime format
birth_date_obj = datetime.datetime.strptime(birth_date, date_format)
current_date =datetime.datetime.now()
#calculate the age in days by subtracting birth date from current date
age_in_days = (current_date - birth_date_obj).days

print(age_in_days)