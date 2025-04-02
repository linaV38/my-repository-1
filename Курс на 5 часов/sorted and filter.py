people = [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 19},
    {"name": "David", "age": 40},
]


def is_adult(person: dict) -> bool:
    return person["age"] >= 18


filtered_people = list(filter(is_adult, people))
print(filtered_people)
