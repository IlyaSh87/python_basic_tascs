import turtle

sn = turtle.Screen()
sn.title('TraficLight by @ilyashegurov')
sn.bgcolor('black')


class TraficLight:
    color = 'red', 'green', 'yellow'
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.color('yellow')
        self.pen.goto(x=-30, y=60)
        self.pen.down()
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(120)
        self.pen.rt(90)
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(120)

        self.red_light = turtle.Turtle()
        self.yellow_light = turtle.Turtle()
        self.green_light = turtle.Turtle()

        self.red_light.speed(0)
        self.yellow_light.speed(0)
        self.green_light.speed(0)

        self.red_light.color('grey')
        self.yellow_light.color('grey')
        self.green_light.color('grey')

        self.red_light.shape('circle')
        self.yellow_light.shape('circle')
        self.green_light.shape('circle')

        self.red_light.penup()
        self.yellow_light.penup()
        self.green_light.penup()

        self.red_light.goto(x=0, y=40)
        self.yellow_light.goto(x=0, y=0)
        self.green_light.goto(x=0, y=-40)

    def change_color(self, color):
        self.red_light.color('red')
        self.red_light.color('green')
        self.red_light.color('yellow')

        if color == 'red':
            self.red_light.color('red')
        elif color == 'yellow':
            self.yellow_light.color('yellow')
        elif color == 'green':
            self.green_light.color('green')

    def timer(self):
        if self.color == 'red':
            self.change_color('green')
            sn.ontimer(self.timer, 3000)
        elif self.color == 'yellow':
            self.change_color('red')
            sn.ontimer(self.timer, 2000)
        elif self.color == 'green':
            self.change_color('yellow')
            sn.ontimer(self.timer, 1000)


stop_light = TraficLight()
stop_light.change_color('red')
stop_light.timer()

sn.mainloop()
