# Python Email Automation Script

This script was designed to solve a time consuming issue that a business loan broker faces on a daily basis: sending the same email separately to multiple lending companies.

As a loan broker, you'll often need to submit a signed application and bank statements to various lenders that the business may qualify with.  It is a simple task that can quickly take up an hour or two of the workday depending on how many applications you have to submit.

I thought it would be interesting to explore how much of this process could be automated via scripting.  While it is all technically possible, it is worth mentioning that this specific script couldn't be used in production as it.  It requires the user to lower the security on their gmail account, which conflicts with the higher security settings most Financial Services companies abide by.

Google offers an API to address this problem, and down the road I plan to incorporate that into this script so it can be production ready.

---
## Instructions for Use

To use this script, you'll need to fill in a few variables with some of the email specific information.  I've set this up to try and create as little work as possible for the user. If you'd like to see examples of the following variables, switch over to the branch titled "example" as that is a fully functioning version of this script.

1. - global variables (the subject line may need to be updated for each application depending on how customized you want it.
    subject: Fill in the empty string with whatever you'd like the subject line of the email to say.
    sender_email: Fill in the empty string with the email address that you will be sending the emails from.
    attachment_files: This will be a list of strings, each string shoudl be a file path to that attachment file.  Assuming you put all the files in the "files"           directory, this would be something like: "files/statement1.pdf"
2. - lender dictionaries (one and done)
    The basic structure of three dictionaries is set up for your convenience, you can copy and paste those to match the number of lenders you work with (you'll need to change those variable names to the lender's name).  If you set up a dictionary for each lender you work with this will only need to be done once, simply adding more as you establish partnerships.
3. - create list for each email
    Fill the empty list with the variable names you want this applicant to be sent to.  This ensures you aren't sending applicants to lenders they won't qualify with instead of sending every applicant to every lender every time.
4. - in the loop of the function
    Within the function there is a variable simply called "body" which is set up as an f-string only containg the lenders name.  Put whatever wording around it as you see fit.  The lender name is in there assuming you want something along the lines of "meets (lender's name)'s requirements.

---
### References

The project started by going through a Real Python article by Joska de Langen called "Sending Emails With Python" and was then adapted and expanded to meets the scope of this project.  (link: https://realpython.com/python-send-email/)

I'd also like to reference a GitHub project by user carnal0wnage titled "Python code for sending HTML email (Attachments + Multiple Recipients)".  This script helped me visualize the logic needed to re-package much of my simple script into a function so the script could go from sending to one recipient to multiple. (link: https://gist.github.com/carnal0wnage/c44df39bd3b45c7d87351b1ce87fe8fe)
