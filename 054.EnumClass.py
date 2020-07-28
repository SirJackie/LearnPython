from enum import Enum, unique

#
# Create Enum Class
#

Month = Enum("Month",
             ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sept", "Oct", "Nov", "Dec")
             )

print(Month)  # Result : <enum 'Month'>


#
# Iterate A Enum Class
#

for name, member in Month.__members__.items():
    print(name, member, member.value)
    # Result :
    # Jan Month.Jan 1
    # Feb Month.Feb 2
    # ...
    # Dec Month.Dec 12

#
# Further Customized Enum Class
#

@unique  # Make sure there is no Repeating Property
class Weekday(Enum):  # Inherit from "Enum" class
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# Access These Enums
print(Weekday.Tue)        # Result : Weekday.Tue
print(Weekday["Tue"])     # Result : Weekday.Tue
print(Weekday.Tue.value)  # Result : 2
print(Weekday(2))         # Result : Weekday.Tue

# Iterate Weekday Enum Class
for name, member in Weekday.__members__.items():
    print(name, member)
    # Result :
    # Sun Weekday.Sun
    # Mon Weekday.Mon
    # ...
    # Sat Weekday.Sat
