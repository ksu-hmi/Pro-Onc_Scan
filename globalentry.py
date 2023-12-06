import pandas as pd
from datetime import datetime, timedelta
import smtplib
from email.message import EmailMessage
from getpass import getpass

def get_email_secure():
    email = input("Enter program email:")
    password = getpass("Enter password")
    return email, password

def get_password():
    return getpass("Enter your email password: ")

def send_email(Location, Date, Time, email, password):
    text = "Hello. There is an available radiology appointment at {Date} {Time} at {Location}."

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
    csv_path = r'C:\Users\grete\OneDrive - Kennesaw State University\HMI 7540-Hlthcare Info Sys. Fall 2023\mock_appointments.csv'
    last_check = datetime.now() - timedelta(seconds=1)
    
    try:
        appts_df = pd.read_csv(csv_path)
        if not appts_df.empty:
            appt = appts_df.iloc[0]
            Location = appt['Location']
            Date = appt['Date']
            Time = appt['Time']

            print("There is an appointment available: Location=", Location + "Date= "+Date, "Time= "+ Time)
            
            send_email(location, date, time, email, password)
        else:
            print("No Appointment found.")
    except Exception as e:
        print("Error during appointment check:{e}")
        
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

