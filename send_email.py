## Import Packages
import smtplib, ssl, getpass, email

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

## Establish email variables
subject = "Hello, World! (Attached)"
body = "This email should have an attachment included."
sender_email = "laigaard.dev@gmail.com"
receiver_email = "laigaard.dev@gmail.com"
cc_email = "laigaard.dev+cc@gmail.com, laigaard.dev+cc2@gmail.com"
password = getpass.getpass()
filename = ["testDoc.pdf", "testDoc2.pdf", "testDoc3.pdf", "testDoc4.pdf"]

## Create multipart message headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Cc"] = cc_email

## Add body to message
message.attach(MIMEText(body, "plain"))

# Open PDF file in binary mode
for file in filename:
    with open(file, "rb") as attachment:
        # Add file as application/octet-stream
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {file}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)


## NEXT STEPS:
## send to multiple CC emails (can't use list, "'list' object has no attribute 'encode'")
## try larger attachments, the size of typical bank statements
## Establish dictionary of 'lenders' --> main and CC emails
## Send the same email multiple times (same exact email, different recipients) --> Use  a loop?
