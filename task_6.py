def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    chosen_items = []
    
    # Проходимо через кожну страву в порядку з найбільшим співвідношенням калорій до вартості
    for item, details in sorted_items:
        # Перевіряємо, чи можемо ми додати цю страву до нашого списку обраних, не перевищуючи бюджет
        if total_cost + details['cost'] <= budget:
            chosen_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']
    
    return chosen_items, total_calories, total_cost


def dynamic_programming(items, budget):
    # Створюємо масив dp, де dp[i] - максимальна кількість калорій при бюджеті i
    dp = [0] * (budget + 1)
    selected_items = [[] for _ in range(budget + 1)]
    
    for item, details in items.items():
        cost = details['cost']
        calories = details['calories']
        
        # Проходимо через всі можливі бюджети від budget до cost в зворотньому порядку
        for b in range(budget, cost - 1, -1):
            # Якщо додавання поточної страви збільшує максимальну кількість калорій
            if dp[b - cost] + calories > dp[b]:
                dp[b] = dp[b - cost] + calories
                selected_items[b] = selected_items[b - cost] + [item]
    
    # Знаходження сумарного бюджету для обраних страв
    total_cost = sum(items[item]['cost'] for item in selected_items[budget])
    
    return selected_items[budget], dp[budget], total_cost


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Виведення результатів для різних бюджетів
for budget in [70, 110, 165]:
    print(f"Бюджет: {budget}")
    
    chosen_items, total_calories, total_cost = greedy_algorithm(items, budget)
    print(f"Жадібний алгоритм: Обрані страви: {chosen_items}, Сумарна калорійність: {total_calories}, Затрачений бюджет: {total_cost}")
    
    chosen_items, total_calories, total_cost = dynamic_programming(items, budget)
    print(f"Алгоритм динамічного програмування: Обрані страви: {chosen_items}, Сумарна калорійність: {total_calories}, Затрачений бюджет: {total_cost}\n")



