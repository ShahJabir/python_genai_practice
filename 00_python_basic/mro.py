"""Method Resolution Order (MRO) Example"""
class A:
    """A base class."""
    def __init__(self, *, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)
    def method(self):
        """A method in class A.""" 
        print(f"Method from class A: {self.name}")

class B(A):
    """A derived class from A."""
    def __init__(self, *, age, **kwargs):
        self.age = age
        super().__init__(**kwargs)
    def method(self):
        """A method in class B.""" 
        print(f"Method from class B: {self.name}, Age: {self.age}")

class C(A):
    """A derived class from A."""
    def __init__(self, *, city, **kwargs):
        self.city = city
        super().__init__(**kwargs)
    def method(self):
        """A method in class C.""" 
        print(f"Method from class C: {self.name}, City: {self.city}")

class D(C, B):
    """A derived class from B and C."""
    def __init__(self, name, age, city):
        super().__init__(name=name, age=age, city=city)

    def d_method(self):
        """A method in class D."""
        print(f"{self.name}, {self.age}, {self.city}")

# Create an instance of class D
obj = D("Alice", 30, "New York")
obj.d_method()
obj.method()
# Print the MRO of class D
print(D.__mro__)
