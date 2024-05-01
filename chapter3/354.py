"""Jennifer is learning Python because she’s pursuing a data science career. She has
learned that a dict object can’t have duplicate keys because of the underlying hash
table implementation. Suppose that she creates a dict object: numbers = {1: "one",
1.0: "one point one"}. What values do you expect the numbers to have?"""

print(hash(1))
print(hash(1.0))