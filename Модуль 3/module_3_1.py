def count_calls() -> None:
    global calls
    calls += 1


def string_info(string: str) -> tuple:
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string: str, list_to_search: list) -> bool:
    count_calls()
    return string.lower() in [x.lower() for x in list_to_search]


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
