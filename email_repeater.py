__author__ = 'Lothilius'

import smtplib
import sys
import authentication
import csv
import time
import numpy as np


#Pull data from CSV file
def array_from_file(filename):
    """Given an external file containing numbers,
            create an array from those numbers."""
    dataArray = []
    with open(filename, 'rU') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            dataArray.append(row)
    return dataArray

# Create email addresses.
def create_email_address(name):
    email = name.replace(' ', '.')
    email = email + '@gmail.com'

    return email

# Create the body of the message
def create_body():
    body = """This is the OOO test!!!

Martin A Valenzuela
Business Applications Administrator
m:  915.217.8558
Martin.Valenzuela@bazaarvoice.com"""

    return body


# Build and send the emails
def send_message(smtp_object, subject, body, receiver='martin.valenzuela@bazaarvoice.com',
                  sender='martin.valenzuela@bazaarvoice.com'):

    full_message = """From:""" + sender + '\n' + 'To:' + receiver + '\n' \
              + 'Subject: ' + subject + '\n\n' + body


    smtp_object.sendmail(sender, [receiver], full_message)
    print "Successfully sent email to " + receiver


if __name__ == '__main__':
    try:
        smtp_object = smtplib.SMTP('smtp.office365.com', 587)
        smtp_object.ehlo()
        smtp_object.starttls()
        username, password = authentication.smtp_login()
        smtp_object.login(username, password)
    except Exception, exc:
        sys.exit("mail failed; %s" % str(exc)) # give a error message

    i = 0
    emails = ['danieltest213']
    for each in range(0, 15):
        body = create_body()
        receiver = create_email_address(emails[0])
        try:
            send_message(smtp_object, 'Testing June 30th 1st', body, receiver)
        except smtplib.SMTPServerDisconnected:
            print 'Server Disconnected'
            try:
                smtp_object = smtplib.SMTP('smtp.office365.com', 587)
                smtp_object.ehlo()
                smtp_object.starttls()
                username, password = authentication.smtp_login()
                smtp_object.login(username, password)
                send_message(smtp_object, 'License usage in SFDC', body, receiver)
            except Exception, exc:
                sys.exit("mail failed1; %s" % str(exc)) # give a error message
        except Exception, exc:
            sys.exit("mail failed2; %s" % str(exc)) # give a error message

        #time.sleep(3)

        i += 1
        print i