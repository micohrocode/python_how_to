'''In this chapter, you learned to sort tasks by using their urgency levels, as shown in list-
ing 3.4. Can you come up with a solution to order the tasks by their descriptions’
lengths? The longer the description is, the higher the task’s rank.'''

tasks = [{'title': 'Homework', 'desc': 'Physics + Math', 'urgency': 5},
{'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 3},
{'title': 'Museum', 'desc': 'Egyptian things', 'urgency': 2}]

def using_desc_len(task):
    return len(task['desc'])

tasks.sort(key=using_desc_len, reverse=True)

print(tasks)