'''
Jerry is a graduate student. One of his projects requires him to extract data from text.
Suppose that the text data is "abc_,abc__,abc,,__abc_,_abc", where abc stands for
the needed data values. That is, the data values are separated by one or more separa-
tors. How can he use regular expressions to extract the data values?
'''
import re

match = re.findall(r"([a-z]+)", "abc_,abc__,abc,,__abc_,_abc")


print(match)

