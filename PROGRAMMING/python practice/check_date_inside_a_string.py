import re

text = '12-12-2235 Testing 12345'
verify=re.findall('\d{2}-\d{2}-\d{4}' , text) or re.match('\d{2}-\d{4}-\d{2}' , text) or re.match('\d{2}-\d{2}-\d{4}' , text)

print(verify)