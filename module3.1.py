calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    a = (len(string), string.upper(), string.lower())
    return a


def is_contains(d, c):
    count_calls()
    f = []
    for i in c:
        f.append(i.lower())
    if d.lower() in f:
        return True
    else:
        return False


print(string_info('Кукуруза'))
print(string_info('Песец'))
print(is_contains('Банер', ['бан', 'БаНаН', 'баНЕР']))
print(is_contains('лира', ['лирика', 'лирик']))
print(calls)