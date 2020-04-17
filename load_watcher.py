# Checks tail of the data file, possibly 100 seconds worth?
# Extract the loadWatts values
# If a consequitive number of load values are very high, send an email
# Check the email wait timeout before sending, to limit the number of emails
# sent to 1 per 5 mins...

import SimpleEmailer
import os

# last_string = os.popen('tail -n 100 %s' % filename).read()

# sender = Emailer()
# emailSubject = "Inverter Update outdated"
# emailContent = "Hi<br>\
# It's been %5.2f seconds since MQTT delivered\
# an update to the Raspberry Pi. <br>\
# Regards, Raspberry Pi Emailer %s" % (timeDifference, socket.gethostname())
# sender.sendmail(emailSubject, emailContent)

