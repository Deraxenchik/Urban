calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(a):
    f = (len(a), a.upper(), a.lower())
    count_calls()
    return f
def is_contains(c, d):
    count_calls()
    d = [e.lower() for e in d]
    if c.lower() in d:
        return True
    else:
        return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)