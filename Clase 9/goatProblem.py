# Joan Jaramillo - 2159930
import random
import matplotlib.pyplot as plt

def monty_hall_simulation_with_plot(n_trials):
    win_switch = 0
    win_stay = 0

    for _ in range(n_trials):
        doors = [0, 0, 1]
        random.shuffle(doors)
        
        initial_choice = random.randint(0, 2)
        remaining_doors = [i for i in range(3) if i != initial_choice and doors[i] == 0]
        opened_door = random.choice(remaining_doors)
        remaining_door = [i for i in range(3) if i != initial_choice and i != opened_door][0]
        
        if doors[remaining_door] == 1:
            win_switch += 1
        if doors[initial_choice] == 1:
            win_stay += 1

    prob_switch = win_switch / n_trials
    prob_stay = win_stay / n_trials

    # Imprimir resultados
    print(f"Estrategia de cambiar: {win_switch} victorias ({prob_switch:.2%} de probabilidad)")
    print(f"Estrategia de quedarse: {win_stay} victorias ({prob_stay:.2%} de probabilidad)")

    # Graficar resultados
    strategies = ['Cambiar', 'Quedarse']
    wins = [win_switch, win_stay]
    probabilities = [prob_switch, prob_stay]

    fig, ax1 = plt.subplots()

    # Barra de victorias
    ax1.bar(strategies, wins, color=['skyblue', 'lightcoral'], label='Victorias')
    ax1.set_xlabel('Estrategias')
    ax1.set_ylabel('Número de Victorias', color='black')
    ax1.tick_params(axis='y', colors='black')

    # Línea de probabilidades
    ax2 = ax1.twinx()
    ax2.plot(strategies, probabilities, color='darkgreen', marker='o', label='Probabilidad')
    ax2.set_ylabel('Probabilidad', color='darkgreen')
    ax2.tick_params(axis='y', colors='darkgreen')
    ax2.set_ylim(0, 1)

    # Título y leyendas
    plt.title('Resultados de la Simulación de Monty Hall')
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    
    plt.show()

# Ejecutar la simulación con gráfico
monty_hall_simulation_with_plot(100_000)
