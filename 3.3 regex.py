import re

text = 'Alice was born on March 12, 1992. Her brother, John, was born on June 5, 1988. They have a mutual friend named Mike, whose phone number is 555-123-4567. In their hometown, which has a population of 1,234 or 1,235 people, a holiday festival is held every year on December 25. Alice works in an office with 30 employees. Her phone number is 555-765-4321.'

dates_pattern = r'[A-Za-z]+ \d{1,2}, \d{4}'
dates = re.findall(date_pattern, text)

phone_numbers_pattern = r'\d{3}-\d{3}-\d{4}'
phone_numbers = re.findall(phone_pattern, text)

thousands_numbers_pattern = r'\d{1,3}(?:,\d{3})*' #non-capturing group that matches zero or more occurrences of a comma followed by three digits
thousands_numbers = re.findall(thousands_pattern, text)

names_pattern = r'\b(?!March|June|December|Her|They|In)[A-Z][a-z]+\b'
names = re.findall(name_pattern, text)

whole_numbers_pattern = r'\b\d+\b'
whole_numbers = re.findall(whole_number_pattern, text)

print("Dates:", dates)
print("Phone Numbers:", phone_numbers)
print("Thousand Separated Numbers:", thousand_numbers)
print("Names:", names)
print("Whole Numbers:", whole_numbers)
