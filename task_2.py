import random
import scipy.integrate as spi

# 1. Реалізація методу Монте-Карло

# Визначення функції для інтегрування
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Визначення обмежуючого прямокутника
# Висота прямокутника - максимальне значення функції на інтервалі
y_max = f(b)
rect_area = (b - a) * y_max

# Кількість випадкових точок для симуляції
num_points = 1000000

# Лічильник точок, що потрапили під криву
points_under_curve = 0

for _ in range(num_points):
    # Генеруємо випадкову точку всередині прямокутника
    rand_x = random.uniform(a, b)
    rand_y = random.uniform(0, y_max)
    
    # Перевіряємо, чи точка лежить під графіком функції
    if rand_y <= f(rand_x):
        points_under_curve += 1

# Розрахунок площі (інтеграла) за методом Монте-Карло
monte_carlo_integral = (points_under_curve / num_points) * rect_area

print(f"Обчислення інтеграла f(x) = x^2 від {a} до {b}:")
print("-" * 40)
print(f"Результат методом Монте-Карло ({num_points} точок): {monte_carlo_integral}")


# 2. Порівняльний аналіз

# Аналітичний розрахунок
# Інтеграл від x^2 це (x^3)/3
analytical_result = (b**3 / 3) - (a**3 / 3)
print(f"Аналітичний результат: {analytical_result}")

# Розрахунок за допомогою scipy.integrate.quad
quad_result, quad_error = spi.quad(f, a, b)
print(f"Результат за допомогою SciPy quad: {quad_result}")
print("-" * 40)
