# simple python programm to return the age of my Linux system

from datetime import datetime , timedelta

# enter time of system install as UTC time
installtime = datetime(2023, 10, 31, 22, 5, 8 )

diff = datetime.now() - installtime

def chop_microseconds(delta):
    return delta - timedelta(microseconds=delta.microseconds)

print(chop_microseconds(diff))
