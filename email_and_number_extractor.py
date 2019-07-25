#!python3
# email_and_number_extactor.py - finds emails and phone numbers in the clipboard and returns the emails and phone numbers in your clipboard

import pyperclip
import re

phone_regex = re.compile(r'''(
    (\+\d{2} | \(\+\d{2}\) | \d)       #Area Code
    (\s|-|\.)?                         #Separator
    (\d{3})                            #First 3 digits
    (\s|-|\.)?                         #Separator
    (\d{3})                            #Next 3 digits
    (\s|-|\.)?                         #Separator
    (\d{4})                            #Last 4 digits
    )''', re.VERBOSE)

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                  #Username
    @                                  #@ symbol
    [a-zA-Z0-9.-]+                     #Domain name
    (\.[a-zA-Z]{2,4})                  #End of domain
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for group in phone_regex.findall(text):
    number = ''.join([group[1], group[3], group[5], group[7]])
    matches.append(number)
for group in email_regex.findall(text):
    print(group)
    matches.append(group[0])

if len(matches) > 0:
    output = '\n'.join(matches)
    pyperclip.copy(output)
    print('Copied to clipboard: ')
    print(output)
else:
    print('No matches found!')
