import random

player_wins = 0
bot_wins = 0

while player_wins < 3 and bot_wins < 3:
    player_choice = input("Escoge piedra, papel o tijeras: ").lower()

    choices = ["piedra", "papel", "tijeras"]

    if player_choice not in choices:
        print("\nOpción invalida. Intentelo denuevo")
        continue

    bot_choice = random.choice(choices)

    print("---------------------------------------")
    print(f"La computadora escogio: {bot_choice}")
    print(f"Tu escogiste: {player_choice}")
    print("---------------------------------------")

    if (
        (player_choice == "piedra" and bot_choice == "tijeras")
        or (player_choice == "tijeras" and bot_choice == "papel")
        or (player_choice == "papel" and bot_choice == "piedra")
    ):
        player_wins += 1
        print(f"Ganaste")
    elif player_choice == bot_choice:
        print("Empate")
    else:
        bot_wins += 1
        print("Gano la maquina")

    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print(f"Puntaje actual - Jugador: {player_wins}, computadora: {bot_wins}")
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

if player_wins > bot_wins:
    (
        f"\nFelicidades! al mejor de tres, puntaje Jugador: {player_wins} - Computadora: {bot_wins}"
    )
else:
    print("\nLa computadora gano al mejor de tres :( mejor suerte para la proxima.")
    print(f"puntaje Computadora: {bot_wins} - Jugador {player_wins}")
