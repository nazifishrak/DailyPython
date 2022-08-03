import datetime


import datetime as dt

# dt is the module
# dt has a class called datetime
# so we can say dt.datetime to get the datetime class

# datetime has a class method called now()
# To call the class method we will directly use the dot operator on the class

time_now = dt.datetime.now()
# print(time_now) --> prints out the datetime obj

# time_now.year() --> returns the current year (int)\

# To create our own datetime object

my_dob = dt.datetime(year = 2001, month=12, day=3)

