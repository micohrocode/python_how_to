# Chapter 2 Processing and Format Strings

``` python
tasks = ["homework", "laundry", "grocery shopping"]
assert f"First Task: {tasks[0]}" == 'First Task: homework'
```

F string places non string values into the string

Assert checks to make sure something is true before proceeding

for readability check how long it would take a new persong reading it to understand what is happening

``` python
task_ids = [1, 2, 3]
task_names = ['Do homework', 'Laundry', 'Pay bills']
task_urgencies = [5, 3, 4]
for i in range(3):
 print(f'{task_ids[i]:^12}{task_names[i]:^12}{task_urgencies[i]:^12}')
# Output the following lines:
1 Do homework 5
2 Laundry 3
3 Pay bills 4
```

After the expression to be placed in the string a : can be placed and then the text can be aligned with < or ^ or > with the number after being how far it expands

``` python
large_prime_number = 1000000007
print(f"Use commas: {large_prime_number:,d}")
# output: Use commas: 1,000,000,007

decimal_number = 1.23456
print(f"Two digits: {decimal_number:.2f}")
# output: Two digits: 1.23
print(f"Four digits: {decimal_number:.4f}")
# output: Four digits: 1.2346

print(f"Sci notation: {sci_number:.2e}")
# output: Sci notation: 4.13e-09
```

Numbers can have commas added or floating point numbers can be rounded and formatted, e for scientific notation

``` python
good_username = "1a2b3c"
assert good_username.isalnum() == True

assert "Homework".isalpha() == True

assert "123".isnumeric() == True
```

Check that a string is numbers and letters, only letters or only numbers

``` python
float("3.25")

int("-5")

def cast_number(number_str):
try:
    casted_number = float(number_str)
except ValueError:
    print(f"Couldn't cast {repr(number_str)} to a number")
else:
    print(f"Casting {repr(number_str)} to {casted_number}")
```

Convert a string to a float or an integer. Use try except when trying to cast in order to prevent the program from haulting if there is an error

``` python
style_settings = ["font-size=large", "font=Arial", "color=black",
➥ "align=center"]
merged_style = ", ".join(style_settings)
print(merged_style)
# output: font-size=large, font=Arial, color=black, align=center
```

Join strings together stored in list using join, they are joined by the delimiter before the join call

``` python
processed_tasks = []
for data_line in task_data.split("\n"):
    processed_task = data_line.split(",")
    processed_tasks.append(processed_task)
```

The split function finds the delimiter and splits the string into a list where that delimiter is found

``` python
separated_words0 = []
for word in messy_data.split(","):
    if word.find("_") < 0:
        separated_words0.append(word)
    else:
        separated_words0.extend(word.split("_"))
```

The extend function adds the entire split list to the other list here

``` python
ask_pattern = re.compile("\\\\task")
texts = ["\task", "\\task", "\\\task", "\\\\task"]
for text in texts:
    print(f"Match {text!r}: {task_pattern.match(text)}")
```

Create the pattern, attempt to match it to the items in the list

``` python
task_pattern_r = re.compile(r"\\task")
```

It can also be written as such to use the raw string to be matched

^hi starts with hi

task$ ends with task

^hi task$ starts and ends with "hi task", and thus exact matching

392.4 What are the essentials of regular expressions?

hi? h followed by zero or one i

hi* h followed by zero or more i

hi+ h followed by one or more i

hi{3} h followed by iii

hi{1,3} h followed by i, ii, or iii

hi{2,} h followed by 2 or more i

\d any decimal digit

\D any character that is not a decimal digit

\s any whitespace, including space, \t, \n, \r, \f, \v

\S any character that isn't a whitespace

\w any word character, means alphanumeric plus underscores

\W any character that is not a word character

. any character except a newline

[] a set of defined characters

a|b a or b

(abc) abc as a group

[^a] any character other than a

``` python
match = re.search(r"(\w\d)+", "xyza2b1c3dd")
print(match)
# output: <re.Match object; span=(3, 9), match='a2b1c3'>
print("matched:", match.group())
# output: matched: a2b1c3
print("span:", match.span())
# output: span: (3, 9)
print(f"start: {match.start()} & end: {match.end()}")
# output: start: 3 & end: 9
```

The match object gives where the match was found by index and the string that was matched

``` python
regex = re.compile(r"(?P<task_id>\d{3}), (?P<task_title>\w+);
(?P<task_desc>.+)")

tasks = []
for line in text_data.split("\n"):
    match = regex.match(line)
    if match:
        task = (match.group('task_id'), match.group('task_title'),
        ➥ match.group('task_desc'))
        tasks.append(task)
```

Use ?P<group_name> to assign a name to the group to be used later, for better readability

[Index](/README.md)