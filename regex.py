import re

d = re.finditer("\s((?!nome:)[^:])+", line)
for i in d:
	print(i.group(0))
