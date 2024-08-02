import random
import matplotlib.pyplot as plt

# Функція симулює кидки двох кубиків та обчислює ймовірності сум
def monte_carlo_simulation(num_rolls: int):
    # Ініціалізуємо словник для підрахунку кількості кожної суми від 2 до 12
    sums_count = {i: 0 for i in range(2, 13)}
    
    # Виконуємо симуляцію кидків
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)  
        dice2 = random.randint(1, 6)  
        roll_sum = dice1 + dice2  # Обчислюємо суму
        sums_count[roll_sum] += 1  # Збільшуємо лічильник для цієї суми

    # Обчислюємо ймовірності у відсотках
    probabilities = {sum_val: count / num_rolls * 100 for sum_val, count in sums_count.items()}
    return probabilities

# Функція для виведення результатів у вигляді таблиці
def print_results(sums, probabilities, analytical_probabilities):
    def print_row(values):
        print("│", end='')
        for value in values:
            print(f"{value:^18}", end='│')
        print()

    header = ["Сума", "Монте-Карло (%)", "Аналітична (%)"]
    width = 58
    print("┌" + "─" * (width - 2) + "┐")
    print_row(header)
    print("├" + "─" * (width - 2) + "┤")
    
    for sum_value in sums:
        row = [sum_value, f"{probabilities[sum_value]:.2f}", f"{analytical_probabilities[sum_value]:.2f}"]
        print_row(row)
    
    print("└" + "─" * (width - 2) + "┘")

def main():
    num_rolls = 1000000  # Кількість кидків
    probabilities = monte_carlo_simulation(num_rolls)  

    # Аналітичні ймовірності
    analytical_probabilities = {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
        7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }

    # Вивід результатів у вигляді таблиці
    sums = list(range(2, 13))
    print_results(sums, probabilities, analytical_probabilities)

    # Побудова графіку
    plt.figure(figsize=(10, 6))
    # Гістограма для Монте-Карло
    plt.bar(sums, [probabilities[sum_value] for sum_value in sums], width=0.8, label='Монте-Карло', color='blue', alpha=0.4)
    # Графік для аналітичних ймовірностей
    plt.plot(sums, [analytical_probabilities[sum_value] for sum_value in sums], 'ro-', label='Аналітичні')

    plt.xlabel('Сума на кубиках') 
    plt.ylabel('Імовірність (%)')  
    plt.title('Ймовірності сум при киданні двох кубиків')  
    plt.legend()  
    plt.grid(True)  
    plt.xticks(ticks=sums, labels=[str(sum_value) for sum_value in sums])

    
    plt.show()

if __name__ == "__main__":
    main()  
