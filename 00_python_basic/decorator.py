"""Simple logging decorator"""
import time
from functools import wraps

def log_activity(func):
    """A decorator that logs the activity of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function completed: {func.__name__}")
        return result
    return wrapper

def timer(func):
    """A decorator that times the execution of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Took {end - start:.4f}s")
        return result
    return wrapper

def require_login(func):
    """A decorator that requires a user to be logged in."""
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        is_logged_in = user.get("is_logged_in", False) if isinstance(user, dict) else getattr(user, "is_logged_in", False)
        if not is_logged_in:
            raise PermissionError("Login required")
        return func(user, *args, **kwargs)
    return wrapper

def repeat(times):
    """A decorator that repeats the execution of a function."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@log_activity
@timer
@require_login
def my_function(user, name):
    """A simple function to demonstrate the logging decorator."""
    print("Inside the function")
    for _ in range(1000000):
        pass
    print(f"hey {name}, your login status is {user.is_logged_in}")

@repeat(3)
def hello():
    """A simple function to demonstrate the repeat decorator."""
    print("Hello, world!")
hello()

@require_login
def test_class(_user):
    """A simple function to demonstrate the require_login decorator."""
    print("Inside the test_class function")

try:
    test_class({"name":"Bob", "is_logged_in": False})
except PermissionError as exc:
    print(exc)

# Assuming we have a user object with an is_logged_in attribute
class User:
    """A simple user class."""
    def __init__(self, is_logged_in):
        self.is_logged_in = is_logged_in

current_user = User(is_logged_in=True)
my_function(current_user, "Alice")
