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
body = "Laigaard Capital would like to submit a funding application from a business we feels meets your qualifications, please let me know if you need anything else.\n\nThank you!"
sender_email = "laigaard.dev@gmail.com"
receiver_email = "laigaard.dev@gmail.com"
cc_email = "laigaard.dev+cc@gmail.com, laigaard.dev+cc2@gmail.com"
password = getpass.getpass()
filename = ["files/testDoc.pdf", "files/statement1.pdf", "files/statement2.pdf", "files/statement3.pdf"]


# testing lender data structures, need to update receive/cc emails in script
abc_cap = {"name": "ABC Capital", "submission_email": "laigaard.dev@gmail.com", "cc_email": ["laigaard.dev+cc@gmail.com"]}
get_funded = {"name": "123 GetFunded", "submission_email": "laigaard.dev@gmail.com", "cc_email": ["laigaard.dev+cc@gmail.com","laigaard.dev+cc2@gmail.com"]}
xyz_vent = {"name": "XYZ Ventures", "submission_email": "laigaard.dev@gmail.com", "cc_email": ["laigaard.dev+cc@gmail.com", "laigaard.dev+cc2@gmail.com", "laigaard.dev+cc3@gmail.com"]}

lenders = [abc_cap, get_funded, xyz_vent]


# Create Function to send message.
def send_message():
    i = 0
    while i < len(lenders):
        # receiver_email = lenders[i]["submission_email"]
        # cc_email = lenders[i]["cc_email"]                 this is a list, strip/split list?  can't use list in email script
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
        i += 1

        # todo - MIMEMultipart message created in the function, may be easiest to just create whole header in the function

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


# TODO: Create readme for github
