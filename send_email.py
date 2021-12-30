## Import Packages
import smtplib, ssl, getpass, email, time

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

## Start script timer
start = time.time()

## Establish email variables that are the same for all emails
subject = "New Funding Submission from Laigaard Capital"
body = "Laigaard Capital would like to submit a funding application from a business we feels meets your qualifications, please let me know if you need anything else.\n\nThank you!"
sender_email = "laigaard.dev@gmail.com"
password = getpass.getpass()
attach_files = ["files/testDoc.pdf", "files/statement1.pdf", "files/statement2.pdf", "files/statement3.pdf"]

## Establish a dictionary for each lender you work with
abc_cap = {"name": "ABC Capital", "submission_email": "laigaard.dev@gmail.com", "cc_email": ["test.dev7105@gmail.com"]}
get_funded = {"name": "123 GetFunded", "submission_email": "test.dev7105@gmail.com", "cc_email": ["laigaard.dev@gmail.com",""]}
xyz_vent = {"name": "XYZ Ventures", "submission_email": "", "cc_email": ["laigaard.dev@gmail.com", "test.dev7105@gmail.com", ""]}

## Add the lenders to a list, only add lenders you want to send this specific email to
lenders = [abc_cap, get_funded, xyz_vent]


## Function to loop through lender list and send an email to each one
def send_message():
    i = 0
    while i < len(lenders):
        receiver_email = lenders[i]["submission_email"]
        cc_list = lenders[i]["cc_email"]
        cc_email_str = ''
        for cc in cc_list:
            if len(cc_list) == 1:
                cc_email_str += cc
            else:
                cc_email_str += cc + ','
        print(cc_email_str)

        ## Create MIMEMultipart message headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Cc"] = cc_email_str

        ## Add body to message
        message.attach(MIMEText(body, "plain"))

        ## Add attachment to message
        for file in attach_files:
            with open(file, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {file}",
                )
                message.attach(part)
                text = message.as_string()

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
        i += 1

send_message()

## End script timer and print results
end = time.time()
result = end - start
print("Email Sent.")
print(f"It took {result} seconds to send.")
