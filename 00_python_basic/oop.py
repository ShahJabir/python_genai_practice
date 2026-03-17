"""Basic OOP concepts in Python"""

class BaseChai:
    """A base class for different types of chai."""
    def __init__(self, type_):
        self.type = type_
    def prepare(self):
        """Prepare the chai."""
        print(f"Preparing {self.type} chai.")

class MasalaChai(BaseChai):
    """A class for preparing masala chai."""
    def add_spices(self):
        """Add spices to the masala chai."""
        print("Adding spices to the masala chai.")

class ChaiShop:
    """A class for managing a chai shop."""
    chai_cls = BaseChai
    def __init__(self):
        self.chai = self.chai_cls("Regular")
    def serve(self):
        """Serve the chai."""
        print(f"Serving {self.chai.type} chai in the shop.")
        self.chai.prepare()

class FancyChai(ChaiShop):
    """A class for managing a fancy chai shop."""
    chai_cls = MasalaChai

shop = ChaiShop()
fancy_shop = FancyChai()
shop.serve()
fancy_shop.serve()
fancy_shop.chai.add_spices()

class ChaiUtils:
    """A class containing utility methods for chai."""
    def cleaned_ingredients(self, text):
        """cleaned ingredients"""
        return [item.strip() for item in text.split(",")]

ingredients = ChaiUtils().cleaned_ingredients(" sugar, milk, tea leaves, water, masala")
print(ingredients)

class UserData:
    """A class for managing user data."""
    def __init__(self, name, email):
        self.name = name
        self.email = email
    @classmethod
    def dict_data(cls, user_data):
        """Create a UserData instance from a dictionary."""
        return cls(**user_data)
    def print_user(self):
        """Print the user's information."""
        print(f"Name: {self.name}, Email: {self.email}")

user = UserData.dict_data({"name": "Alice", "email": "alice@example.com"})
user.print_user()
user2 = UserData("Bob", "bob@example.com")
user2.print_user()

class TeaLeaf:
    """Basic Tea Leaf class."""
    def __init__(self, age):
        if age > 0:
            self._age = age
        else:
            raise ValueError("Age cannot be negative.")
    @property
    def age(self):
        """Get the age of the tea leaf."""
        return self._age
    @age.setter
    def age(self, value):
        """Set the age of the tea leaf."""
        if value > 0:
            self._age = value
        else:
            raise ValueError("Age cannot be negative.")

sylati_leaf = TeaLeaf(5)
print(sylati_leaf.age)
india_leaf = TeaLeaf(-1)
print(india_leaf.age)
