''' James works in a wholesale company’s IT department and is preparing a template
of price tags. Suppose that the product’s data is saved as a dict object: {"name":
"Vacuum", "price": 130.675}. How can James write an f-string if the desired output is
Vacuum: {130.68}? Note that the price requires two-digit precision and that the out-
put includes curly braces, which are coincidentally the characters for string interpola-
tion in f-strings.
'''

object = {"name":
"Vacuum", "price": 130.675}

print(f'{object["name"]}:{{{object["price"]}}}')
