import requests
from datetime import datetime, timedelta
import smtplib
from email.message import EmailMessage
from getpass import getpass

def get_email_secure():
    email = input("Enter program email:")
    password = getpass("Enter password")
    return email, password


def send_email(appt, email, password):
    date = datetime.strptime(appt[0]['startTimestamp'], '%Y-%m-%dT%H:%M')
    text = "Hello. There is an available radiology appointment at {wkday}, {mth} {d} at {time}.".format(wkday=date.strftime('%A'), mth=date.strftime('%B'), d=date.strftime('%d'), time=date.strftime('%I:%M %p'))

    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = "Radiology Appointment Availability"
    msg['From'] = "testmailbox2024.com"
    msg['To'] = "glawre19@students.kennesaw.edu"

try:  
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(email, password)
        server.send_message(msg)
except Exception as e:
    print('An error occurred while sending email:')

def check_appointment():
    URL = "None"
    last_check = datetime.now() - timedelta(seconds=1)
    
    while True:
        if (datetime.now() - last_check > timedelta(seconds=1)):
            try:
                appt = requests.get(URL).json()
             # there exists an appointment
                last_check = datetime.now()
                
                if len(appt) > 0:
                    print("There is an appointment available.")
                    send_email(appt, email, password)
                    break
                else: 
                    print("No Appointment found.",appt, last_check)
                    break
            except requests.RequestException as e:
                print("Error during API request:{e}")
if __name__ == "__main __":
    email, password = get_email_secure()
    check_appointment()

## To find locations with available appts, will need to scrape location availability or create list
#replace 'smtp.example.com' with the appropriate SMTP server for your email provider
#find correct SMTP server and port number (587) email provider, you usually need to consult the documentation online
#create and add email address

#you = ''
"""
Uncomment this section if you wanted to query for the next N days instead of the soonest available.
"""
# N = 30
# start = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M')
# end = (datetime.datetime.now() + datetime.timedelta(days=N)).strftime('%Y-%m-%dT%H:%M')

