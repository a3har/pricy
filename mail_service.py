from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(address, subject, message):
    print('Starting mail client')
    CLIENT_SECRET_FILE = 'client_secret_1041291564289-k0r0de67l1dd1aq3h7fbhopf9re8u0i7.apps.googleusercontent.com.json'
    API_NAME = 'gmail'
    API_VERSION = 'v1'
    SCOPES = ['https://mail.google.com/']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    emailMsg = message
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = address
    mimeMessage['subject'] = subject
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(
        userId='me', body={'raw': raw_string}).execute()
    print(message)


if __name__ == '__main__':
    message = 'This is to notify you that the item has reduced its price. Login to the website to buy'
    address = 'azharmuham13@hotmail.com'
    subject = 'PRICY : ALERT !!! ITEM HAS DROPPED PRICE'
    send_email(address, subject, message)
