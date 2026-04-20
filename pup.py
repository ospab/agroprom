import turtle

def draw_sharp_grain(t, x, y, angle, size):
    """Рисует острое стилизованное боковое зерно."""
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()
    t.begin_fill()
    t.circle(size, 70)
    t.left(110)
    t.circle(size, 70)
    t.end_fill()

def draw_logo():
    screen = turtle.Screen()
    screen.setup(600, 750)
    screen.bgcolor("white")
    screen.tracer(0)
    
    t = turtle.Turtle()
    t.hideturtle()
    
    # Тот же золотистый цвет
    gold_color = "#D4AF37" 
    t.color(gold_color)
    
    # 1. ЖИРНЫЙ КРУГ
    t.pensize(10)
    t.penup()
    t.goto(0, -180)
    t.setheading(0)
    t.pendown()
    t.circle(180, steps=100)
    
    # 2. ЖИРНЫЙ СТЕБЕЛЬ (СДВИНУТ ВНИЗ для центровки)
    t.penup()
    t.goto(0, -140) 
    t.setheading(90)
    t.pensize(12) 
    t.pendown()
    
    # Определяем длину стебля до верхнего зерна
    stem_length = 265 
    t.forward(stem_length) 
    
    # Фиксируем точку конца стебля
    top_of_stem_y = -140 + stem_length
    
    # 3. БОКОВЫЕ ЗЕРНА (СДВИНУТЫ ВНИЗ вместе со стеблем)
    y_starts = [-80, -25, 30, 85]
    grain_size = 75 
    
    for y in y_starts:
        # Правое зерно (чуть сдвинули к центру для плотности)
        draw_sharp_grain(t, 2, y, -10, grain_size)
        # Левое зерно (зеркально)
        draw_sharp_grain(t, -2, y, 120, grain_size)
        

    adjusted_x = -13 
    adjusted_y = top_of_stem_y - 1 # Плотная стыковка

    draw_sharp_grain(t, adjusted_x, adjusted_y, 45, 50)

    t.penup()
    t.color(gold_color)
    t.goto(0, -260)
    t.write("AGRO", align="center", font=("Arial", 50, "bold"))
    t.goto(0, -300)
    t.write("INDUSTRY & AGRICULTURE", align="center", font=("Arial", 14, "bold"))
    
    screen.update()
    screen.mainloop()

if __name__ == "__main__":
    draw_logo()