## Import Packages
import smtplib, ssl, getpass, email, time

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

## Establish email variables that are the same for all emails
applicant_name = "A Small Business Co."
subject = f"New Funding Submission from Laigaard Capital - {applicant_name}"
# body = "Laigaard Capital would like to submit a funding application from a business we feels meets your qualifications, please let me know if you need anything else.\n\nThank you!"
sender_email = "laigaard.dev@gmail.com"
password = getpass.getpass()
attach_files = ["files/testDoc.pdf", "files/statement1.pdf", "files/statement2.pdf", "files/statement3.pdf"]

## Establish a dictionary for each lender you work with
abc_cap = {"name": "ABC Capital", "submission_email": "", "cc_email": ["", ""]}
get_funded = {"name": "123 GetFunded", "submission_email": "", "cc_email": ["", ""]}
xyz_vent = {"name": "XYZ Ventures", "submission_email": "", "cc_email": ["", ""]}

## Add the lenders to a list, only add lenders you want to send this specific email to
lenders = [abc_cap, get_funded, xyz_vent]

## Function to loop through lender list and send an email to each one
def send_message():
    i = 0
    receiver_email_final = []
    while i < len(lenders):
        receiver_email = lenders[i]["submission_email"]
        cc_list = lenders[i]["cc_email"]
        cc_list_str = ""
        receiver_email_final.append(receiver_email)
        for cc in cc_list:
            cc_list_str += cc + ", "
            receiver_email_final.append(cc)

        lender_name = lenders[i]["name"]
        body = f"Laigaard Capital would like to submit a funding application from a business we feel meets {lender_name}'s qualifications, please let me know if you need anything else.\n\nThank you!"

        ## Create MIMEMultipart message headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Cc"] = cc_list_str
        message["Subject"] = subject

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

        # receiver_email_final =
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email_final, text)
        i += 1

send_message()
