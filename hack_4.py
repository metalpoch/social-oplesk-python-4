from os import system
from sys import exit, platform
from random import randint


class PochBurguers:
    def __init__(self) -> None:
        self.__request = ""
        self.__menu = {
            "normal": {
                "name": "Burger Normal",
                "price": 3,
                "qty": randint(5, 20)
            },
            "special": {
                "name": "Burger Especial",
                "price": 5,
                "qty": randint(5, 20)
            },
            "super": {
                "name": "Burguer Super Especial",
                "price": 10,
                "qty": randint(5, 20)
            },
            "small_soda": {
                "name": "Refresco Pequeño",
                "price": 1,
                "qty": randint(5, 20)
            },
            "big_soda": {
                "name": "Refresco Grande",
                "price": 3,
                "qty": randint(5, 20)
            }
        }

    def show_stock(self) -> None:
        normal = self.__menu["normal"]
        special = self.__menu["special"]
        super_ = self.__menu["super"]
        s_soda = self.__menu["small_soda"]
        b_soda = self.__menu["big_soda"]

        print()
        print("N   Burguers\t\tCantidad\tPrecio")
        print(f"1 - {normal['name']}\t\t{normal['qty']}\t\t${normal['price']}")
        print(f"2 - {special['name']}\t\t{special['qty']}\t\t${special['price']}")
        print(f"3 - {super_['name']}\t{super_['qty']}\t\t${super_['price']}")
        print("-"*57)
        print("    Bebidas\t\t\tCantidad\tPrecio")
        print(f"4 - {s_soda['name']}\t\t{s_soda['qty']}\t\t${s_soda['price']}")
        print(f"5 - {b_soda['name']}\t\t{b_soda['qty']}\t\t${b_soda['price']}")
        print("-"*57)
        print()


    def show_menu(self) -> None:
        normal = self.__menu["normal"]
        special = self.__menu["special"]
        super_ = self.__menu["super"]
        s_soda = self.__menu["small_soda"]
        b_soda = self.__menu["big_soda"]

        print()
        print("N   Burguers\t\tPrecio")
        print(f"1 - {normal['name']}\t\t{normal['price']}")
        print(f"2 - {special['name']}\t\t{special['price']}")
        print(f"3 - {super_['name']}\t{super_['price']}")
        print()
        print("    Bebidas\t\tPrecio")
        print(f"4 - {s_soda['name']}\t\t{s_soda['price']}")
        print(f"5 - {b_soda['name']}\t\t{b_soda['price']}")
        print()


    def __validate_purchase(self, qty: int) -> tuple:
        request = self.__request
        exist_in_stock = self.__menu[request]["qty"] >= qty
        cost = self.__menu[request]["price"] * qty

        if exist_in_stock:
            return True, cost
        else:
            print("No queda suficientes Burguers")
            return False, 0

    def validate_purchase(self, option: str, qty: int) -> tuple:
        if qty < 1:
            print("Cantidad invalida\nCancelando operación")
            return False, 0

        option = option.lower()
        if option == "5" or "grande" in option:
            self.__request = "big_soda"
        elif option == "4" or "pequeñ" in option:
            self.__request = "small_soda"
        elif option == "3" or "super" in option:
            self.__request = "super"
        elif option == "2" or "especial" in option:
            self.__request = "special"
        elif option == "1" or "normal" in option:
            self.__request = "normal"
        else:
            print("Opción invalida")
            return False, 0

        return self.__validate_purchase(qty=qty)

    def update_stock(self, qty: int):
        request = self.__request
        self.__menu[request]["qty"] -= qty

    def get_products(self) -> str:
        request = self.__request
        return self.__menu[request]["name"]


class Client:
    def __init__(self, name: str, payment_type: str) -> None:
        self.name = name
        self.__payment_type = payment_type
        self.__balance = randint(50, 200)
        self.__shopping = {}

    def get_balance(self) -> tuple:
        name  = self.name
        balance = self.__balance
        payment_type = self.__payment_type

        msg = f"el saldo de tu cuenta {payment_type} es de: ${balance}"
        msg = f"{name.title()}, {msg}"
        return balance, msg

    def change_balance(self, cost: int|float) -> bool:
        if self.__balance >= cost:
            self.__balance -= cost
            return True
        else:
            print("Saldo insuficiente")
            return False

    def shopping_cart(self):
        return self.__shopping

    def shopping_clear(self):
        self.__shopping = {}

    def shopping_cart_append(self, product: str, qty: int, price: int):
        if self.__shopping.get(product):
            self.__shopping[product]["qty"] += qty
            self.__shopping[product]["price"] += price
        else:
            self.__shopping[product] = {"qty": qty, "price": price}

def clear_terminal():
    if platform in ("linux", "darwin"):
        system("clear")
    else:
        system("cls")
    print("*" * 20, "NASA Burguer's", "*" * 20)


def main() -> None:
    clear_terminal()
    # cocinar hamburguesas con amor
    restaurant = PochBurguers()

    print("Bienvenido a NASA Burguer's")
    print("Por favor ingrese a su nombre")
    name = str(input("*> "))
    clear_terminal()
    print(f"Hola {name}! Indique su metodo de pago")
    payment_type = str(input("*> "))

    clear_terminal()
    client = Client(name, payment_type)

    while True:
        _, msg_balance = client.get_balance()
        print(msg_balance)
        print("En que podemos servirle?")
        print("a) Mostrar Stock")
        print("b) Añadir al carrito")
        print("c) Ver carrito")
        print("x) Salir")
        opt = str(input("*> "))
        print()

        match opt:
            case "a":
                clear_terminal()
                restaurant.show_stock()
            case "b":
                clear_terminal()
                restaurant.show_menu()
                print("Indique el nombre o ID del producto")
                option = str(input("*> "))
                print("Cuantos deseas comprar?")
                qty = int(input("*> "))
                exist_stock, cost = restaurant.validate_purchase(option, qty)
                if not exist_stock:
                    clear_terminal()
                    print("\nPerdone, no disponemos de ese producto")
                    print()
                    continue
                print(f"El costo de su pedido es de {cost}. Deseas continuar?")
                _continue = str(input("(y/N) *> "))
                _continue = True if _continue in ("Y", "y") else False
                if not _continue:
                    clear_terminal()
                    continue

                restaurant.update_stock(qty)
                product = restaurant.get_products()
                client.shopping_cart_append(product, qty, cost)
                clear_terminal()
                print("\nCompra añadida al carrito")
                print()
                continue

            case "c":
                clear_terminal()
                balance, msg = client.get_balance()
                print(msg)
                shopping_cart = client.shopping_cart()
                print("_"*54)
                print("\nEn su carrito posee:")
                print("Item\tProducto\t\tCantidad\tPrecio")
                index = 1
                total = 0
                for item, data in shopping_cart.items():
                    total += data['price']
                    if len(item) > 15:
                        print(f"{index}\t{item}\t{data['qty']}\t\t${data['price']}")
                    else:
                        print(f"{index}\t{item}\t\t{data['qty']}\t\t${data['price']}")
                    index += 1
                print("_"*54)
                print(f"Saldo    : ${balance}")
                print(f"Total    : ${total}")
                print(f"Reembolso: ${balance-total}")
                print()
                print("Deseas pagar su cuenta ahora?")
                opt = str(input("(y/N) *> "))
                if opt in ("Y", "y"):
                    success = client.change_balance(total)
                    if success:
                        clear_terminal()
                        client.shopping_clear()
                    else:
                        print("Monto insuficiente")
                        print(f"Hasta luego {client.name}")
                        print("Gracias por preferirnos")
                        print("Vuelva pronto.")
                        exit()

                clear_terminal()
            case "x":
                print(f"Hasta luego {client.name}")
                print("Gracias por preferirnos")
                print("Vuelva pronto.")
                exit()
            case _:
                clear_terminal()


if __name__ == "__main__":
    main()
