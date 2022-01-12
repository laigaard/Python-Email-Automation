# Python Email Automation Script

This script was designed to solve a time consuming issue that a business loan broker faces on a daily basis:  **Sending the same email separately to multiple lending companies.**

As a loan broker, you'll often need to submit a signed application and bank statements to various lenders that the business may qualify with.  It is a simple task that can quickly take up an hour or two of the workday depending on how many applications you have to submit.

It is worth mentioning that this specific script is more of an exercise in automation and would need some tweaks before using in production.  It requires the user to lower the security on their gmail account, which conflicts with the higher security standards most Financial Services companies abide by.

Google offers an API that is supposed to address this problem.

---
## Instructions for Use

To use this script you'll need to fill in a few variables to customize the email to your needs.  I've prefixed the comment above each area with a number (ex: "1.") to make them easier to find.  If you'd like to see examples of the following, switch over to the branch titled "example" as that is a fully functioning version of this script.

1. Global Variables
   - `subject`: Fill in the empty string with whatever you'd like the subject line of the email to say.
   - `sender_email`: Fill in the empty string with the email address that you will be sending the emails from.
   - `attachment_files`: This will be a list of strings, each string should be a file path to that attachment file.  Assuming you put all the files in the "files"           directory, one example would be: `"files/statement1.pdf"`
2. Lender Dictionaries
   - The basic structure of three dictionaries is set up for your convenience, you can copy and paste those to match the number of lenders you work with (you'll likely want to change those variable names to the lender's name).  This will only need to be done once if you set up a dictionary for each lender you work with, simply adding more as you establish partnerships.
3. Create lender list for the email
   - Fill the empty list with the variables corresponding to the lenders you want this applicant to be sent to.  This ensures you aren't sending applicants to lenders they won't qualify with.  This makes it easy to quickly update the list for each applicant, instead of setting up the dictionaries everytime.
4. Body of the email (just above where the MIMEMultipart headers are created)
   - Within the function there is a variable simply called `body` which is set up as an f-string only containing the lenders name.  Put whatever wording around the lender's name as you see fit.  The lender name variable is in there assuming you want something along the lines of "meets (lender's name)'s requirements".  You can remove that and just use a regular string if you prefer.


Once the above has been completed, the script can be run easily from the command line or certain code editors.  On my personal Mac I tested it on both the built-in terminal application as well as VS Code for Mac with the Python Extension.
1. If using a program like VS Code, you can just run the script.  When using the terminal you may need to navigate to the proper directory first, then run the script with the following command:
   - Windows: `python send_email.py` 
   - Mac: `python3 send_email.py`
2. Once you run the script, it will prompt you to enter the password for the email you used in the `sender_email` variable.  Enter your password and then wait for the script to complete.
3. After each email is sent, a string will print in the terminal to let you know - with one final string confirming the process is done.

---
### References

The project started by going through a Real Python article by Joska de Langen called "Sending Emails With Python" and was then adapted and expanded to meet the scope of this project.  (link: https://realpython.com/python-send-email/)

I'd also like to reference a GitHub project by user carnal0wnage titled "Python code for sending HTML email (Attachments + Multiple Recipients)".  This script helped me visualize the logic needed to re-package much of my simple script into a function so the script could go from sending to one recipient to multiple.  (link: https://gist.github.com/carnal0wnage/c44df39bd3b45c7d87351b1ce87fe8fe)
