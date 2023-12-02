def repeat(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Before")
            for in range(count):
                func(*args, **kwarg)
            print("After")
        return wrapper

    return decorator

@repeat(3)
def say_hi(name: str) -> None:
    print(f"Hi my name is {name}!")

say_hi(name="Arthur")