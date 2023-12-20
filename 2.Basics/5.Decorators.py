# Decorator that returns operation result and name of the function called

def to_add(a, b):
    def mid_level(func):
        def adding(*args):
            result = a + b
            return result, func(*args)
        return adding
    return mid_level


def to_multiply(a, b):
    def mid_level(func):
        def multiplying(*args):
            result = a * b, func(*args)
            return result
        return multiplying
    return mid_level


@ to_multiply(10, 20)
def just_function():
    return 'function name: ' + just_function.__name__


outcome = just_function()
print(outcome)