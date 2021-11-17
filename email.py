## Import Packages
import smtplib, ssl

## Establish email variable
port = 465
sender_email = ""
receiver_email = ""
password = input("Please enter your password: ")
#  ^^Use getpass module to make this more secure?
message = """\
Subject: Hello World

I sent this email using a Python script.
"""


# Create Secure SSL Context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


## NEXT STEPS:
##finish basic email script and test
## Expand to multiple email addresses
## Include attachments
## Update message variables to the Lender Submission Template
## Establish dictionary of lenders --> main and CC emails
## Send the same email multiple times (same exact email, different recipients) --> Use  a loop?
