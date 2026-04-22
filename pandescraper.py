#!python3
#phoneAndEmail.py - finds phone numbers and email addresses on the clipboard
import pyperclip, re
# TODO: create regex for phone numbers
phoneRegex = re.compile(r''' 
(
((\d\d\d) | (\(\d\d\d\)))? # area code (optional)
(\s|-|\.)                           # first seperator 
\d\d\d                                 # first 3 digits
(\s|-|\.)                                      # seperator
\d\d\d\d                               # last 4 digits 
(((ext(\.)?\s)|x)              # extension word (optional)
(\d{2,5}))?                     # extension numbers (optional)
)    
''', re.VERBOSE)
# TODO: create a regex object for email addresses
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+ #name  part
@ #@ symbol
[a-zA-Z0-9_.+]+ #domain name

''', re.VERBOSE)
# TODO: Get the text off the clipboard
text = pyperclip.paste()
# TODO: Extract the email and phone number from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumbers in extractedPhone:
    allPhoneNumbers.append(phoneNumbers[0])

# TODO: Copy the extracted phone/email to the clipboard
if not allPhoneNumbers and not extractedEmail:
    print('No matches found')
else:
    results ='\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
    pyperclip.copy(results)
    print(f'{len(allPhoneNumbers)} numbers found and {len(extractedEmail)} emails found')