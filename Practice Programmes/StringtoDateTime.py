from datetime import datetime
# from dateutil import parser

datet = "Mar 11 2011 11:31AM"
# newdate = parser(datet)

newdate = datetime.strptime(datet, '%b %d  %Y %I:%M%p')
print(newdate)


print("python", end=' ')
print("Its a easy language")