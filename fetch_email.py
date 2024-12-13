##
# program that uses regular expressions to fetch and print:
# sender email address
# recipient email address
# email subject
# email body

import emails

def read_email(file_name): # to read the raw email content from the file
    with open(file_name, 'r') as file:
        return file.read()

email_content = read_email('email.txt') # read email content from email.txt

sender = emails.email_sender(email_content)
recipient = emails.email_recipient(email_content)
subject = emails.email_subject(email_content)
body = emails.email_body(email_content)

print(f'Sender: {sender}')
print(f'Recipient: {recipient}')
print(f'Subject: {subject}')
print(f'Body:\n{body}') # \n cause it looks better

