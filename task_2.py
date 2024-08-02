import turtle
import math

# Функція для малювання дерева Піфагора
def draw_pythagoras_tree(length, level):
    if level == 0:
        return
    
    # Малюємо стовбур
    turtle.forward(length)
    
    # Малюємо ліву гілку
    turtle.left(45)
    draw_pythagoras_tree(length * math.sqrt(2) / 2, level - 1)
    turtle.right(45)
    
    # Малюємо праву гілку
    turtle.right(45)
    draw_pythagoras_tree(length * math.sqrt(2) / 2, level - 1)
    turtle.left(45)
    
    # Повертаємося до початкової точки стовбура
    turtle.backward(length)

# Функція для налаштування екрану та запуску малювання
def main():
    screen = turtle.Screen()
    turtle.speed('fastest')  # Максимальна швидкість малювання
    turtle.left(90)          # Поворот черепахи, щоб почати малювання знизу вверх
    turtle.up()
    turtle.backward(200)     # Зміщення вниз для кращої видимості
    turtle.down()
    turtle.color("red")
    turtle.pensize(8)
    level = int(screen.numinput("Введіть рівень рекурсії", "Рівень рекурсії (0-10):", default=5, minval=0, maxval=10))
    length = 200
    
    draw_pythagoras_tree(length, level)
    turtle.done()

# Запуск програми
if __name__ == "__main__":
    main()
