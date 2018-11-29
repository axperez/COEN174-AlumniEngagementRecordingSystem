'''
Alumni Engagement Recording System | Developers: Axel Perez, Brendan Watamura, & Matt Wong

helper.py

Helper functions to be able to send emails, create qr codes, and generate confirmation codes.
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import secrets
import string
import qrcode
import os

def create_qrcode(link):
    '''
    Create qrcode from a given link.
    '''
    qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
    )

    # Add data
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image()

    # Save it somewhere, change the extension as needed:
    img.save("image.jpg")

def sendmail(name, toaddr, status, confcode=None, link=None):
    '''
    Send an email from coen174aers@gmail.com to specific alumni with necessary
    elements.
    '''
    fromaddr = 'coen174aers@gmail.com'
    gmail_password = 'COEN174AERSTEST'
    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = 'Alumni Event Status Response'

    # string to store the body of the mail
    if status == 'Accepted':
        body = "Event: %s\nEvent Status: %s\nConfirmation Code: %s\nCheck-In Link: %s\nQR Code Attached" % (name, status, confcode, link)
    else:
        body = "Event: %s\nEvent Status: %s" % (name, status)

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    if status == 'Accepted':
        create_qrcode(link)

        # open the file to be sent
        filename = "image.jpg"
        attachment = open(os.getcwd() +"/image.jpg", "rb")

        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        p.set_payload((attachment).read())

        # encode into base64
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # attach the instance 'p' to instance 'msg'
        msg.attach(p)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()   # optional
        server.login(fromaddr, gmail_password)
        server.sendmail(fromaddr, toaddr, text)
        server.close()

    except Exception as e:
        print(e)
        print ('Something went wrong...')
        if status == 'Accepted':
            os.remove('image.jpg')
        return False

    if status == 'Accepted':
        os.remove('image.jpg')
    return True

def generate_code():
    '''
    Generate secure 20 character code from secrets python library.
    '''
    alphabet = string.ascii_letters + string.digits
    confcode = ''.join(secrets.choice(alphabet) for i in range(20))
    return confcode

def unique_conf_code(events):
    '''
    Check if code is unique against the already listed event conf codes.
    '''
    confcode = generate_code()
    for event in events:
        if confcode == event.ConfCode:
            confcode = unique_conf_code(events)
            break

    return confcode
