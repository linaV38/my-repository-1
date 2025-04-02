def find_average(*, numbers: list) -> float:
    return sum(numbers) / len(numbers)

try:
    print(find_average(numbers=[]))
except ZeroDivisionError as error:
    print(f"Something goes wrong: {error}")

print("we are here")
