import re

word = "Django"
# pattern = "((" + "ang" + ")+)"
# found = re.findall(pattern, word)
# if(found):
#     print(found)
#     for i in range(len(found)):
#         print(found[i])

items = ["CSS", "Django", "Git", "HTML", "Python"]
for item in items:
    if re.search('it', item, re.IGNORECASE):
        print(item)