import re

string = 'search inside this text please'
print(re.search('that', string))

pattern = re.compile('This is a string compiled as pattern')
print(pattern.match('This is a string compiled as pattern This is a string compiled as pattern'))

email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
password_pattern = re.compile(r"[a-zA-Z0-9@#$%&]{7,}[0-9]")