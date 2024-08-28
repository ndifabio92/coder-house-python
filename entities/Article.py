class Article:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    def __str__(self) -> str:
        return f"{self.name} (${self.price})"