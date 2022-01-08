## Import Packages
import smtplib, ssl, getpass, email, time

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

## 1. Establish global variables that are the same for all emails
subject = ""
sender_email = ""
password = getpass.getpass()
attachment_files = [] # this will be a list of strings containing the path to each file (ex: "files/statement1.pdf")

## 2. Establish a dictionary for each lender you work with (change variable names as needed, cc_email should be a list of strings)
abc_cap = {"name": "", "submission_email": "", "cc_email": []}
get_funded = {"name": "", "submission_email": "", "cc_email": []}
xyz_vent = {"name": "", "submission_email": "", "cc_email": []}

## 3. Create a list only including the lenders you want this specific email to go to
lenders = []


## Function to loop through lenders list and send emails to each one
def send_message():
    ## Establish some local variables
    i = 0
    receiver_email_final = []

    ## Loop through list of lenders to grab their respective email addresses
    while i < len(lenders):
        receiver_email = lenders[i]["submission_email"]
        receiver_email_final.append(receiver_email)

        ## Cc emails are added to receiver_email_final to ensure they all actually receive the message
        ## They are added to cc_list_str in order to have them properly listed in the Cc section of the email header
        cc_list = lenders[i]["cc_email"]
        cc_list_str = ""
        for cc in cc_list:
            cc_list_str += cc + ", "
            receiver_email_final.append(cc)

        ## 4. Create email body and customize the lender's name to keep a personalized feel
        lender_name = lenders[i]["name"]
        body = f"{lender_name}"

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
