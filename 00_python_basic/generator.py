"""Python basic syntax and topics!"""

# Generator Comprehensions expressions
gen = (n for n in range(5))
print(list(gen))

pairs = ((x, y) for x in range(3) for y in range(3))
print(list(pairs))

numbers = [1,1,2,2,3,3,4,4,5,5,6,6]
gen = (n for n in numbers)
print(set(gen))

unsorted_values = (n for n in range(10, 0, -1))
# print(list(unsorted_values))
print(list(sorted(unsorted_values)))

even_or_odd = map(lambda n: f"{n+1} is even" if (n+1) % 2 == 0 else f"{n+1} is odd", range(10))
print(list(even_or_odd))

def deshi_chai():
    """Generator function to yield deshi chai options."""
    yield "Masala Chai"
    yield "Dudh Chai"
    yield "Lemon Chai"

def imported_chai():
    """Generator function to yield imported chai options."""
    yield "Earl Grey"
    yield "Assam"
    yield "Darjeeling"

def full_menu():
    """Generator function to yield the full menu."""
    yield from deshi_chai()
    yield from imported_chai()

def chai_stall():
    """Generator function to simulate a chai stall."""
    print("Welcome to the chai stall! What chai would you like?")
    try:
        while True:
            order = yield
            print(f"Your order: {order}")
    except GeneratorExit:
        print("Chai stall closed.")
    finally:
        print("Thank you for visiting the chai stall!")

# ---- execution ----
stall = chai_stall()
next(stall)  # prime coroutine

for chai in full_menu():
    stall.send(chai)

stall.close()
