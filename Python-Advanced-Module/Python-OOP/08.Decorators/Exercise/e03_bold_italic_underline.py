def make_bold(func_ref):
    def wrapper(*text):
        result = f"<b>{func_ref(*text)}</b>"
        return result
    return wrapper


def make_italic(func_ref):
    def wrapper(*text):
        result = f"<i>{func_ref(*text)}</i>"
        return result
    return wrapper


def make_underline(func_ref):
    def wrapper(*text):
        result = f"<u>{func_ref(*text)}</u>"
        return result
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))
