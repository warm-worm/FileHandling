###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file , 'r', encoding='utf-8') as file:
    email_content = file.read()


# regular expression pattern
# for amounts
pattern = r'\$?\d{1,3}(?:,\d{3})*(?:\.\d{2})?'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email_content)

# calculate the total purchases
total = 0
for amount in amounts:
    amount = amount.replace('$', '').replace(',', '') # removing $ and commas before converting to float
    total += float(amount)

total_rounded = round(total , 2)
# print result
print(f'Total amount spent: ${total_rounded}')