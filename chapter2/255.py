import re

text_data = """101, Homework; Complete physics and math
some random nonsense
102, Laundry; Wash all the clothes today
54, random; record
103, Museum; All about Egypt
1234, random; record
Another random record"""

regex = re.compile(r"(?P<task_id>\d{3}), (?P<task_title>\w+);(?P<task_desc>.+)\n")

match = regex.findall(text_data)

print(match)