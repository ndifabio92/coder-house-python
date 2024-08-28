from entities.Article import Article
from entities.Client import Client

if __name__ == "__main__":
    client = Client("Nicolas",32,"calle falsa 123", "callefalsa@gmail.com")

    item = Article("Notebook", 1500000)
    item2 = Article("Teclado", 15000)

    client.add_cart(item)
    client.add_cart(item2)

    # print(client.list_shopping_cart())
    print(client)