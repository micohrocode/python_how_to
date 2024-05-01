# Chapter 3 Built in Data Containers

List for when changes are expected to the stored data, tuples for data that is not be changed later in the program

``` python
numbers = [12, 4, 1, 3, 7, 5, 9, 8]
numbers.sort()
print(numbers)
# output: [1, 3, 4, 5, 7, 8, 9, 12]
names = ['Danny', 'Aaron', 'Zack', 'Jennifer', 'Mike', 'David']
names.sort(reverse=True)
print(names)
# output: ['Zack', 'Mike', 'Jennifer', 'David', 'Danny', 'Aaron']
```

Sort lists using built in understanding


``` python
mixed = [3, 1, 2, 'John', ['c', 'd'], ['a', 'b']]
mixed.sort(key=str)
print(mixed)
# output: [1, 2, 3, 'John', ['a', 'b'], ['c', 'd']]
```

Key used to give understanding to how the data should be sorted

``` python
def using_urgency_level(task):
    return task['urgency']
tasks.sort(key=using_urgency_level, reverse=True)
print(tasks)
# output the following lines (re-arranged for readability):
[{'title': 'Homework', 'desc': 'Physics + Math', 'urgency': 5},
{'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3},
{'title': 'Museum', 'desc': 'Egyptian things', 'urgency': 2}]
```

Sort each item in the lsit using its value for urgency

``` python
from collections import namedtuple

Task = namedtuple('Task', 'title desc urgency')
task_nt = Task('Laundry', 'Wash clothes', 3)
assert task_nt.title == 'Laundry'
assert task_nt.desc == 'Wash clothes'
```

A named tuple can be used to give meaning to data without all of the code needed for a class. They support dot notation to access data

``` python
urgencies = {"Laundry": 3, "Homework": 5, "Museum": 2}
urgen_keys = urgencies.keys()
urgen_values = urgencies.values()
urgen_items = urgencies.items()
print(urgen_keys, urgen_values, urgen_items, sep="\n")
# output the following lines:
dict_keys(['Laundry', 'Homework', 'Museum'])
dict_values([3, 5, 2])
dict_items([('Laundry', 3), ('Homework', 5), ('Museum', 2)])
```

Accessing keys, values and items from a dictionary

``` python
if "Homework" in urgencies:
    urgency = urgencies["Homework"]
else:
    urgency = "N/A"

def retrieve_urgency(task_title):
if task_title in urgencies:
    urgency = urgencies[task_title]
else:
    urgency = "N/A"
return urgency
```

Check that they key is in the object before attempting to access the value

``` python
urgencies.get("Homework")
# output: 5
urgencies.get("Homeworks", "N/A")
# output: 'N/A'
urgencies.get("Homeworks")
# output: None (None is automatically hidden in an interactive console)
```

Get will check for the key before accessing to avoid the same issue'

``` python
from collections.abc import Hashable
def check_hashability():
    items = [{"a": 1}, [1], {1}, 1, 1.2, "test", (1, 2), True, None]
    for item in items:
        print(f"{str(type(item)): <18} | {isinstance(item, Hashable)}")
        print(f"{'Data Type': <18} {'Hashable'}")

hash(1)
```

Check that items of different types are hashable. All immutable types are hashable

``` python
def all_contained_in_recommended(recommended, personal):
    print(f"Is {personal} contained in {recommended}?")
    for stock in personal:
        if stock not in recommended:
            return False
    return True
```

Check that all items in one list are contained within another

``` python
good_stocks_set = set(good_stocks)
contained0 = good_stocks_set.issuperset(client0)
print(f"Is {client0} contained in {good_stocks}? {contained0}")
# output: Is ['GOOG', 'AMZN'] contained in
➥ ['AAPL', 'GOOG', 'AMZN', 'NVDA']? True
```

Make the larger list a set and check if that is a super set of the smaller list

76

[Index](/README.md)