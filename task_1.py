import pulp

# Створення моделі
# Визначаємо задачу максимізації
model = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)

# Визначення змінних
# Кількість "Лимонаду" (ціле, невід'ємне число)
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
# Кількість "Фруктового соку" (ціле, невід'ємне число)
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Цільова функція
# Максимізуємо загальну кількість вироблених продуктів
model += lemonade + fruit_juice, "Total_Products"

# Додавання обмежень
# Обмеження на ресурси згідно з умовами завдання
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
model += 1 * lemonade <= 50, "Sugar_Constraint"
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Розв'язання задачі
model.solve()

# Виведення результатів
print(f"Статус розв'язку: {pulp.LpStatus[model.status]}")
print("-" * 30)
print("Оптимальна кількість продуктів для виробництва:")
print(f"Лимонад: {pulp.value(lemonade)}")
print(f"Фруктовий сік: {pulp.value(fruit_juice)}")
print("-" * 30)
print(f"Максимальна загальна кількість продуктів: {pulp.value(model.objective)}")
