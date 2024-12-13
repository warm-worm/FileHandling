# email_sender()
# email_recipient()
# email_subject()
# email_body()
import re

def email_sender(content):
    match = re.search(r'From:.*<([^>]+)>', content)
    return match.group(1) if match else None

def email_recipient(content):
    match = re.search(r'To:.*<([^>]+)>', content)
    return match.group(1) if match else None

def email_subject(content):
    match = re.search(r'Subject: (.*)', content)
    return match.group(1) if match else None


def email_body(content):
    match = re.search(r'\n{2,}(.*)', content, re.DOTALL) #needs the re.dotall to print the whole thing
    return match.group(1).strip() if match else None