import time

# get a timestamp for "now"
timestamp = time.time()
print("Timestamp since epoch:", timestamp)

# convert to a date/time object
dateTime = time.localtime(timestamp)
print(dateTime)

print("The hour is", dateTime.tm_hour)

# format the date/time for a user
formattedDate = time.strftime("%m/%d/%Y", dateTime)
print("The date is:", formattedDate)
formattedDate = time.strftime("%m-%d-%y", dateTime)
print("The date is:", formattedDate)

while True:
    timestamp = time.time()
    dateTime = time.localtime(timestamp)
    formattedDate = time.strftime("%I:%M:%S%p", dateTime)
    print("The time is:", formattedDate)

    time.sleep(1)

