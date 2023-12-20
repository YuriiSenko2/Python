import re

# Check if the line contains only letters, integers and underlines

print('Do not use anything apart from letters, integers and underlines ')
text = input('Enter anything: ')
pattern = r'^[A-Za-z0-9_]+$'
if re.match(pattern, text):
    print(text)
else:
    print('The rules were not followed')

# Remove an area of brackets

text = "example (.com) github (.com) stackoverflow (.com)"
text_old = r'\(.*?\)'
text_new = r''
result = re.sub(text_old, text_new, text)
print(result)

# Insert a space before upper case letters

text = "Example.comGithub.comStackoverflow.com"
text_old = r"\B([A-Z])"
text_new = r' \1'
res = re.sub(text_old, text_new, text)
print(res)

