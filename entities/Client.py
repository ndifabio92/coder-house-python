from typing import List
from .Article import Article

class Client:
    def __init__(self, name: str, age: int, address: str, email: str):
        self.name = name
        self.age = age
        self.address = address
        self.email = email
        self.shopping_cart: List[Article] = []


    def add_cart(self, item:Article) -> str:
        self.shopping_cart.append(item)
        return f"Agregado con exito"

    def list_shopping_cart(self) -> str:
        shopping_cart = ", ".join([str(item) for item in self.shopping_cart])
        return shopping_cart

    def __str__(self) -> str:
        shopping_cart = ", ".join([str(item) for item in self.shopping_cart])
        return f"Client: {self.name}, Age: {self.age}, Address: {self.address}, Email: {self.email}, Shopping Cart: {shopping_cart}"
    
