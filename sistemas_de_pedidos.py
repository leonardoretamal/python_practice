# Sistema de pedidos de comida.

italian_food = ["Pasta Bolognese", "Pepperoni pizza", "Margherita pizza", "Lasagna"]


def find_meal(name, menu):
    return name if name in menu else None


def select_meal(name):
    find = find_meal(name, italian_food)
    return find


def display_available_meals():
    print("Comidas italianas disponibles: ")
    i = 0
    for meal in italian_food:
        i += 1
        print(f"{i}. {meal}")


def create_summary(name, amount):
    order = select_meal(name)
    if order:
        return f"Tu orden {amount} {name}"
    else:
        return "Comida no encontrada."


print("Bienvenido al Sistema de orden de comidas")
display_available_meals()
name_input = input("Selecciona la comida: ")
amount_input = input("Cantidad de ordenes del pedido pedido: ")

result = create_summary(name_input, amount_input)
print(result)
