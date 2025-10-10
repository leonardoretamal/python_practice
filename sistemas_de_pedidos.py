# Sistema de pedidos de comida.

italian_food = ["Pasta Bolognese", "Pepperoni pizza", "Margherita pizza", "Lasagna"]

indian_food = ["Curry", "Chutney", "Samosa", "Naan"]


def find_meal(name, menu):
    return name if name in menu else None


def select_meal(name, food_type):
    if food_type == "Italiana":
        return find_meal(name, italian_food)
    elif food_type == "India":
        return find_meal(name, indian_food)
    else:
        return None


def display_available_meals(food_type):
    if food_type == "Italia":
        print("Comidas italianas disponibles: ")
        for meal in italian_food:
            print(meal)
    elif food_type == "India":
        print("Comida indus disponible: ")
        for meal in indian_food:
            print(meal)
    else:
        print("Tipo de comida invalida.")


def create_summary(name, amount, food_type):
    order = select_meal(name, food_type)
    if order:
        return f"Tu orden {amount} {name}"
    else:
        return "Comida no encontrada."


print("Bienvenido al Sistema de orden de comidas")
type_input = input("Escribe el tipo de comida que quieres: ")
display_available_meals(type_input)
name_input = input("Selecciona la comida: ")
amount_input = input("Cantidad de ordenes del pedido pedido: ")

result = create_summary(name_input, amount_input, type_input)
print(result)
