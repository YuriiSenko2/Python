def singleton(cls):
    instance = {}

    def wrapper(*args, **kwargs):
        if cls not in instance.keys():
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper


@singleton
class EternalTriplePassword:
    def __init__(self, first_part: int, second_part: str, third_part):
        self.digits = first_part
        self.letters = second_part
        self.special_symbols = third_part


password1 = EternalTriplePassword(21, 'JimmyButler', '#$%')
print(password1.digits, password1.letters, password1.special_symbols)
password2 = EternalTriplePassword(3, 'DwyaneWade', '^@#')
print(password1 == password2)