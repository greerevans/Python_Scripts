#! python3
#script for finding dates in text and changing them to a single format
import re,pyperclip
#Copy text from clipboard 
text = str(pyperclip.paste())
#Regex for dates

dateRegex = re.compile(r'''(
(\()? #1
(\d{1,2}) #2
([\/\-\,]) #3                      
(\d{1,2}) #4
([\/\-\,]) #5                      
(\d{4}) #6
(\))? #7           
           )''',re.VERBOSE)
#Find Valid matches and Format matches to single format

formDates = []
for dates in dateRegex.findall(text):
    a = int(dates[2])
    b = int(dates[4])
    c = int(dates[6])

    if a > 12:
        formatted = f'{b}/{a}/{c}'

    else:
        formatted = f'{a}/{b}/{c}'
    
    formDates.append(formatted)

#Paste matches to clipboard
if not formDates:
    print('No dates found')

else:
    pyperclip.copy('\n'.join(formDates))
    print(f'{len(formDates)} dates found')

