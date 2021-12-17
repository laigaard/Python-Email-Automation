## Import Packages
import smtplib, ssl, getpass, email, time

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Start script timer
start = time.time()

## Establish email variables
subject = "New Funding Submission from Laigaard Capital"
body = "ISO Laigaard Capital would like to submit a funding application from a business we feels meets your qualifications, please let me know if you need anything else.\n\nThank you!"
sender_email = "laigaard.dev@gmail.com"
receiver_email = "laigaard.dev@gmail.com"
cc_email = "laigaard.dev+cc@gmail.com, laigaard.dev+cc2@gmail.com"
password = getpass.getpass()
filename = ["testDoc.pdf", "statement1.pdf", "statement2.pdf", "statement3.pdf",]

# Log in to server using secure context and send email || Create Function to send message.
def send_message():
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

## Create MIMEMultipart message headers
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

send_message()

# End script timer and print results
end = time.time()
result = end - start
print("Email Sent.")
print(f"It took {result} seconds to send.")


## NEXT STEPS:
## Build email in script, use function to actually send email - this will make loop easier
## Establish dictionary of 'lenders' --> main and CC emails
## Send the same email multiple times (same exact email, different recipients) --> Use  a loop?
## create readme file for github - what this script does, why it was made, references that influenced the code (real python, github project)
