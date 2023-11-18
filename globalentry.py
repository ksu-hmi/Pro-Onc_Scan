import requests
from datetime import datetime, timedelta

def program_email(subject, body):
    system_email_address = "Scans4U@ ProScan.com"
    system_password= "Password7540fa"
    patient_email= "Patient23@gmail.com"

    print("Notification as requested to email", patient_email + ":\n Subject" +"\n Body:",body)

# To find locations with available appts, will need to scrape location availability or create list

you = ''
"""
Uncomment this section if you wanted to query for the next N days instead of the soonest available.
"""
# N = 30
# start = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M')
# end = (datetime.datetime.now() + datetime.timedelta(days=N)).strftime('%Y-%m-%dT%H:%M')

URL = "https://radiologyassist.com/ra-search-results/".format("")

init = datetime.now() - timedelta(seconds=1)

# working on the email functionality
# def sendEmail(appt):
  #     date = datetime.strptime(appt[0]['startTimestamp'], '%Y-%m-%dT%H:%M')
  #     text = "Hello! There is an available appointment at Boston Logan Airport at {wkday}, {mth} {d} at {time}.".format(wkday=date.strftime('%A'), mth=date.strftime('%B'), d=date.strftime('%d'), time=date.strftime('%I:%M %p'))
  #     msg = EmailMessage()
  #     msg.set_content(text)
  #     msg['Subject'] = f'Global Entry Appointment Alert!'
  #     msg['From'] = 'alert@globalentry.com'
  #     msg['To'] = you
  #     s = smtplib.SMTP('localhost')
  #     s.send_message(msg)
  #     s.quit()

while True:
    if (datetime.now() - init > timedelta(seconds=1)):
        appt = requests.get(URL).json()
        # there exists an appointment
        init = datetime.now()
        if len(appt) > 0:
            print("There is an appointment available.")
        if len(appt) > 0:
            #sendEmail(appt)
            break
        else: 
            print("No Appointment found.",appt, init)
            break