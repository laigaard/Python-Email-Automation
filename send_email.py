## Import Packages
import smtplib, ssl, getpass, email, time

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

## Establish global variables that are the same for all emails
applicant_name = "A Small Business Co."
subject = f"New Funding Submission from Laigaard Capital - {applicant_name}"     # set this up with an f-string to potentially expand code to send multiple applicants to various lenders all at once
sender_email = "laigaard.dev@gmail.com"
password = getpass.getpass()
attachment_files = ["files/testDoc.pdf", "files/statement1.pdf", "files/statement2.pdf", "files/statement3.pdf"]

## Establish a dictionary for each lender you work with
abc_cap = {"name": "ABC Capital", "submission_email": "laigaard.dev@gmail.com", "cc_email": ["test.dev7105@gmail.com"]}
get_funded = {"name": "123 GetFunded", "submission_email": "test.dev7105@gmail.com", "cc_email": ["laigaard.dev@gmail.com", "test.dev7501@gmail.com"]}
xyz_vent = {"name": "XYZ Ventures", "submission_email": "test.dev7501@gmail.com", "cc_email": ["laigaard.dev@gmail.com", "test.dev7105@gmail.com", "test.dev7501+cc@gmail.com"]}

## Create a list with all the lenders you want this email to go to
lenders = [abc_cap, get_funded]


## Function to loop through lenders list and send emails to each one
def send_message():
    ## Establish local variables
    i = 0
    receiver_email_final = []

    ## Loop through list of lenders to grab their respective email addresses
    while i < len(lenders):
        receiver_email = lenders[i]["submission_email"]
        receiver_email_final.append(receiver_email)

        ## Cc emails are added to receiver_email_final to ensure they all receive the message
        ## They are added to cc_list_str in order to have them properly listed in the Cc section of the email header
        cc_list = lenders[i]["cc_email"]
        cc_list_str = ""
        for cc in cc_list:
            cc_list_str += cc + ", "
            receiver_email_final.append(cc)

        ## Create email body and customize the lender's name to keep a personalized feel
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

        ## Add attachment(s) to message
        for file in attachment_files:
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

        ## Login to mail server and send message to recipient list via SMTP, this can be left as is if using gmail
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email_final, text)

        ## Print confirmation message and increment index variable
        print(f"Email sent to {lender_name}")
        i += 1


send_message()
print("All messages have been sent.")
