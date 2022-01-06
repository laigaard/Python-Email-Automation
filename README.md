# Python Email Automation Script

This script was designed to solve a time consuming issue that a business loan broker faces on a daily basis: sending the same email separately to multiple lending companies.

As a loan broker, you'll often need to submit a signed application and bank statements to various lenders that the business may qualify with.  It is a simple task that can quickly take up an hour or two of the workday depending on how many applications you have to submit.

I thought it would be interesting to explore how much of this process could be automated via scripting.  While it is all technically possible, it is worth mentioning that this specific script couldn't be used in production as it.  It requires the user to lower the security on their gmail account, which conflicts with the higher security settings most Financial Services companies abide by.

Google offers an API to address this problem, and down the road I plan to incorporate that into this script so it can be production ready.

---
## Instructions for Use

TODO: add instructions

---
### References

The project started by going through a Real Python article by Joska de Langen called "Sending Emails With Python" and was then adapted and expanded to meets the scope of this project.  (link: https://realpython.com/python-send-email/)

I'd also like to reference a GitHub project by user carnal0wnage titled "Python code for sending HTML email (Attachments + Multiple Recipients)".  This script helped me visualize the logic needed to re-package much of my simple script into a function so the script could go from sending to one recipient to multiple. (link: https://gist.github.com/carnal0wnage/c44df39bd3b45c7d87351b1ce87fe8fe)
