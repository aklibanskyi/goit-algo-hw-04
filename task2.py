import turtle

def koch_curve(t, length, level):
    """Рекурсивна функція для малювання однієї кривої Коха."""
    if level == 0:
        # Базовий випадок: малюємо пряму лінію
        t.forward(length)
    else:
        # Розбиваємо лінію на 3 частини та викликаємо рекурсію для кожної
        length /= 3.0
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)

def draw_snowflake(level, size=300):
    """Функція для налаштування екрану та малювання 3-х кривих (сніжинки)."""
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title(f"Сніжинка Коха - Рівень {level}")
    
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання
    t.color("blue")
    
    # Піднімаємо перо і зміщуємо черепашку, щоб сніжинка була по центру
    t.penup()
    t.goto(-size/2, size/3)
    t.pendown()
    
    # Сніжинка Коха складається з трьох кривих Коха, з'єднаних у трикутник
    for _ in range(3):
        koch_curve(t, size, level)
        t.right(120)
        
    # Ховаємо курсор черепашки та залишаємо вікно відкритим
    t.hideturtle()
    screen.mainloop()

def main():
    while True:
        try:
            level = int(input("Введіть рівень рекурсії для сніжинки Коха (наприклад, 0, 1, 2, 3, 4): "))
            if level < 0:
                print("Рівень рекурсії не може бути від'ємним.")
                continue
            break
        except ValueError:
            print("Будь ласка, введіть ціле число.")
            
    draw_snowflake(level)

if __name__ == "__main__":
    main()
