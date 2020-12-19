#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tkinter as tk

class Game(tk.Frame):
    """Игровой экземпляр, подкласс Tkinter.Frame, заданный в Tkinter.Tk() root."""
    def __init__(self, master):
        """Создать родительский Tkinter.Frame() и задать игровые параметры."""
        # Init parent - Tkinter.Frame(Frame instance, Tk instance)
        tk.Frame.__init__(self, master)
        self.levels = 1
        self.lives = 20
        self.width = 610
        self.height = 400
        self.paddle_speed = 15
        # Tkinter.Canvas() занимает площадь рамки
        self.canvas = tk.Canvas(self, bg='#aaaaff', width=self.width,
                                height=self.height)

        self.canvas.pack()
        self.pack(expand = 1)

        self.items = {}
        self.ball = None
        self._paddle_y_start = 326
        self.paddle = Paddle(self.canvas, self.width / 2, self._paddle_y_start)

        # e.g. self.items = {'32345': Paddle, }
        # свойство .item (int) возвращает уникальные ссылки на
        # на элементы, созданные с помощью метода canvas (e.g. canvas.create_oval() or
        # canvas.create_rectangle())
        # Данный список будет содержать только ссылки на объекты canvas items, которые сталкиваются с мячом
        self.items[self.paddle.item] = self.paddle

        # Create the brick layout
        for x in range(5, self.width - 5, 75):  # 75 px step
            #self.add_brick(x + 37.5, 50, 2)
            #self.add_brick(x + 37.5, 70, 1)
            self.add_brick(x + 37.5, 90, 1)

        self.hud = None
        self.hudx = None

        # set up game entities
        self.setup_game()

        # Привязка ключевых событий к методам перемещения
        self.canvas.focus_set()  

        # Здесь мы используем анонимные функции в качестве обработчиков событий.
        # '_' просто заполнитель для игнорирования первого данного параметра
        # для нас (a Tkinter event by bind()).
        
        self.canvas.bind('<Left>', lambda _: self.paddle.move(self.paddle_speed * -1))
        self.canvas.bind('<Right>', lambda _: self.paddle.move(self.paddle_speed))

    def setup_game(self):
        """Подстройка всех необходимых параметров для начала игры."""
        self.add_ball()
        self.update_lives_text()
        self.update_levels_text()
        self.text = self.draw_text(300, 200, "Press Spacebar to start")
        # Bind only here otherwise would call start_game() each time pressed
        self.canvas.bind('<space>', lambda _: self.start_game())

    def add_ball(self):
        """Создать экземпляр мяч (Ball) и сохранить также ссылку на него в self.Paddle."""
        if self.ball is not None:
            self.ball.delete()
        paddle_coords = self.paddle.get_position()
        # set the ball on top of player's paddle at start
        x = (paddle_coords[0] + paddle_coords[2]) * 0.5
        self.ball = Ball(self.canvas, x, 310)
        self.paddle.set_ball(self.ball)  # store reference to it
        
    def bricks(self):
        for x in range(5, self.width - 5, 75):
            self.add_brick(x + 37.5, 90, 1)

    def add_brick(self, x, y, hits):
        """
        Создать объект Brick.

        :param x: x-axis int location to create Brick.
        :param y: y-axis int location to create Brick.
        :param hits: int number of hits before Brick breaks.
        """
        brick = Brick(self.canvas, x, y, hits)
        # brick.item will be int that uniquely ID's that brick on canvas
        self.items[brick.item] = brick

    def draw_text(self, x, y, text, size='40'):
        """
        Текст, который отображается на холсте.

        :param x: int x-координата начала текста
        :param y: int y-координата конца текста
        :param text: текст, который нужно отобразить
        :param size: default 40. Int размер текста
        """
        font = ('Helvetica', size)
        return self.canvas.create_text(x, y, text=text, font=font)

    def update_lives_text(self):
        """Отображает количество жизней на холсте canvas."""
        text = "Lives: {}".format(self.lives)
        if self.hud is None:
            self.hud = self.draw_text(50, 20, text, 15)
        else:
            self.canvas.itemconfig(self.hud, text=text)
            
    def update_levels_text(self):
        """Отображает количество уровней на холсте canvas."""
        text = "Level: {}".format(self.levels)
        if self.hudx is None:
            self.hudx = self.draw_text(550, 20, text, 15)
        else:
            self.canvas.itemconfig(self.hudx, text=text)

    def start_game(self):
        """Начать главный цикл игры"""
        # unbind pressing space to call start_game()
        self.canvas.unbind('<space>')
        self.canvas.delete(self.text)
        self.paddle.ball = None
        if self.levels == 2:
            self.paddle_speed = 30
        elif self.levels == 3:
            self.paddle_speed = 35
        elif self.levels == 4:
            self.paddle_speed = 40
        elif self.levels == 5:
            self.paddle_speed = 38
        self.game_loop()

    def game_loop(self):
        """Главный цикл игры."""
        self.check_collisions()
        # get how many Bricks left
        num_bricks = len(self.canvas.find_withtag('brick'))
        if num_bricks == 0:
            self.levels += 1
            self.update_levels_text()
            if self.levels < 6:
                self.after (500, self.setup_game)
                self.after(500, self.bricks) 
            else: 
                self.ball.speed = None
                self.draw_text(300, 200, "You've won!")
        elif self.ball.get_position()[3] >= self.height:
            # bottom of screen, lose a life
            self.ball.speed = None
            self.lives -= 1
            if self.lives < 0:
                self.draw_text(300, 200, "Game Over")
            else:
                self.after(1000, self.setup_game)
        else:
            self.ball.update()  # update position
            if self.levels == 2:
                self.ball.speed = 15
            elif self.levels == 3:
                self.ball.speed = 18
            elif self.levels == 4:
                self.ball.speed = 23
            elif self.levels == 5:
                self.ball.speed = 27
            # use Tkinter .after() method to call game loop again
            # after(delay in ms, callback)
            self.after(50, self.game_loop)

    def check_collisions(self):
        """
        "Процесс столкновений" шара.

        Ball.collide получает список игровых объектов, и
        canvas.find_overlapping() возвращает лист ссылок на эти объекты
        с заданными позициями. Потом мы их используем чтобы перевести
        каждый canvas item в соответствующий game object.

        Game.items будет содержать только объекты canvas items, о которые мог
        столкнуться мяч. Поэтому, нам нужно только передать
        items из Game.items dict.

        We filter the canvas items that cannot collide with the ball,
        как текстовые объекты, и затем извлекаем каждый game objects по
        его ключу.
        """
        ball_coords = self.ball.get_position()
        items = self.canvas.find_overlapping(*ball_coords) # list
        # list comprehension to filter down to only objects that
        # can collide with the ball
        collideables = [self.items[x] for x in items if x in self.items]
        self.ball.collide(collideables)


class GameObject():
    """Базовый класс игровых объектов, существующих на Tkinter.Canvas()."""
    def __init__(self, canvas, item):
        """
        Stores the canvas and item parameters as properties of this instance
        for reference.

        :param canvas: a Tkinter.Canvas instance
        :param item: an entity/shape, e.g. a Canvas.create_oval reference
        """
        self.canvas = canvas
        self.item = item

    def get_position(self):
        """
        Возвращает ограничителные координаты элемента экземпляра.

        :rtype: list of integers
        """
        return self.canvas.coords(self.item)

    def move(self, x, y):
        """
        Перемещение координат элемента экземпляра по x горизонтально, и по y вертикально.

        :param x: расстояние, на которое self.item горизонтально перемещается, в пикселях
        :param y: расстояние, на которое self.item вертикально перемещается, в пикселях
        """
        self.canvas.move(self.item, x, y)

    def delete(self):
        """Удалить self.item экземпляра."""
        self.canvas.delete(self.item)


class Ball(GameObject):
    """
    Шар, отскакивающий от "твердых" объектов на экране. Содержит информацию о
    скорости, направлении движения и радиусе шара.
    """
    def __init__(self, canvas, x, y):
        """Creates ball shape using canvas.create_oval()."""
        self.radius = 10
        self.direction = [1, -1]  # вверх и вниз
        self.speed = 10

        # self.item value will be an integer, which is ref num returned by method
        item = canvas.create_oval(x - self.radius, y - self.radius,
                                  x + self.radius, y + self.radius,
                                  fill='white')
        # вызов родительского конструктора с нашим требуемым item
        GameObject.__init__(self, canvas, item)

    def update(self):
        """Логика изменения направления перемещения шара Ball во время столкновения."""

        # ---------------------------------------------------------
        # BOUNDS COLLISIONS
        # ---------------------------------------------------------
        ball_coords = self.get_position()
        width = self.canvas.winfo_width()

        if ball_coords[0] <= 0 or ball_coords[2] >= width:
            self.direction[0] *= -1  # обращение x вектора
        if ball_coords[1] <= 0:
            self.direction[1] *= -1  # обращение y вектора
        x = self.direction[0] * self.speed  # scale by Ball's speed
        y = self.direction[1] * self.speed
        self.move(x, y) 


    def collide(self, game_objects):
        """
       Обрабатывает результат столкновения с одним или несколькими объектами.

        :param game_objects: список объектов, с которыми сталкивается мяч.

        Объяснение кода:
        # Сперва возьмём центр x Мяча (Ball)
        # x0, y0 - это верхний левый угол, x1, y1 - это нижний правый угол
        ball_coords = self.get_position() # -> [x0, y0, x1, y1]
        # мы добавляем начальные и конечные позиции по x и умножаем на 0.5 чтобы получить midx
        ball_center_x = (ball_coords[0] + coords[2]) * 0.5  # центр
        brick_coords = brick.get_position() # -> [x0, y0, x1, y1]
        # если ball_center больше, чем нижняя правая часть кирпича, то значит, что
        # ball center должен находится справа от нижней правой части кирпича во время столкновения
        if ball_center_x > brick_coords[2]:
            self.direction[0] = 1  # координата мяча по x находится по правую сторону
        # проверка, не находится ли центр мяча слева от левой стороны кирпича
        # во время столкновения
        elif ball_center_x < brick_coords[0]:
            self.direction[0] = -1  # ball x to the left
        # else case means ball_center is between left and right x of brick
        # что означает верхний/нижний удар, поэтому мы просто обращаем y-вектор полета шара
        else:
            self.direction[1] *= -1

        Вышесказанное справедливо для тех случаев, когда шар ударяется о платформу или об один кирпич. Но если
        шар ударится о два кирпича, то тут нужно будет подумать. Мы решили упростить этот случай 
        в предположениии, что удары о несколько кирпичей могут происходить либо вверху, либо внизу.
        Это значит, что мы меняем ось y полёта шара без расчета положения кирпичей, о которые он ударяется.

        Таким образом, мы просто смотрим на то, какое количество объектов (с которыми сталкивается шар)
        находится в аргументе game_objects, и если их 2 и более, то мы просто обращаем направление полета
        шара по оси y и всё.
        Если нет, то надо отдельно рассмотреть такой случай и провести те же действия, о которых сказано выше.
        """
        ball_coords = self.get_position()
        ball_center_x = (ball_coords[0] + ball_coords[2]) * 0.5  # same as / 2

        if len(game_objects) > 1:  # 2+ collisions, just flip y-axis and done
            self.direction[1] *= -1
        elif len(game_objects) == 1:  # investigate more if just one collision
            game_object = game_objects[0]
            coords = game_object.get_position()
            if ball_center_x > coords[2]:
                self.direction[0] = 1
            elif ball_center_x < coords[0]:
                self.direction[0] = -1
            else:
                self.direction[1] *= -1
        for game_object in game_objects:
            if isinstance(game_object, Brick):
                game_object.hit() 


class Paddle(GameObject):
    """
    Описывает платформу. Метод set_ball сохраняет ссылку на мяч,
    которая может перемещаться ещё до начала игры.
    """
    def __init__(self, canvas, x, y):
        """
        Создать экземпляр платформы Paddle, используя canvas.create_rectangle().

        :param canvas: a Tkinter.Canvas() instance
        :param x: the horizontal axis location (int)
        :param y: the vertical axis location (int)
        """
        self.width = 80
        self.height = 10
        self.ball = None

        # item will be int ref num returned by create_rectangle()
        item = canvas.create_rectangle(x - self.width / 2,
                                       y - self.height / 2,
                                       x + self.width / 2,
                                       y + self.height / 2,
                                       fill='blue')
        # вызов родительского класса требуемым аргументом item 
        GameObject.__init__(self, canvas, item)

    def set_ball(self, ball):
        """Сохранить ссылку на шар в этом экземпляре."""
        self.ball = ball

    def move(self, offset):
        """
        Перемещение платформы на Tkinter.Canvas в пределах границ холста.

        Здесь содержится логика предварительного перемещения. Фактически
        это происходит вызовом родительского метода GameObject.move().

        :param offset: integer. сумма перемещения направо и налево.
        """
        coords = self.get_position()  # e.g., [int, int, int, int]
        width = self.canvas.winfo_width()
        # проверка соблюдения границ
        if coords[0] + offset >= 0 and coords[2] + offset <= width:
            GameObject.move(self, offset, 0)  # 0 is y-axis
            # Ниже случай, когда игра ещё не началсь; движения мяча
            if self.ball is not None:
                self.ball.move(offset, 0)  


class Brick(GameObject):
    """Ball объекты должны уничтожать canvas rectangle объекты (кирпичи) при ударе."""
    COLORS = {1: '#999999', 2: '#555555', 3: '#222222'}

    def __init__(self, canvas, x, y, hits):
        """
        Инициализация объекта Brick.

        :param canvas: a Tkinter.Canvas() instance
        :param x: где разместить объект по оси x 
        :param y: где разместить объект по оси y
        :param hits: количество ударов, которые объект Brick может принять, прежде чем он 'сломается'
        """
        self.width = 75
        self.height = 20
        self.hits = hits
        color = Brick.COLORS[hits]  # hits arg must be int 1,2, or 3

        # tags - ключевое слово, на которое мы можем легко ссылаться на canvas
        item = canvas.create_rectangle(x - self.width / 2,
                                       y - self.height / 2,
                                       x + self.width / 2,
                                       y + self.height / 2,
                                       fill=color, tags='brick')
        # теперь вызвать родительский класс с нашим требуемым item
        GameObject.__init__(self, canvas, item)

    def hit(self):
        """Счетчик, сколько осталось попаданий. Удалить экземпляр, если он равен 0."""
        self.hits -= 1
        if self.hits == 0:
            self.delete()  # наследование от GameObject()
        else:  # repaint next color to indicate Brick was hit
            self.canvas.itemconfig(self.item, fill=Brick.COLORS[self.hits])



if __name__ == "__main__":
    # Создать root и создать Game instance (a tk.Frame())
    ROOT = tk.Tk()
    ROOT.title('Tkinter Breakout')
    # Frame() нуждается в Tk() экземпляре в качестве родительского, мы передаем его root
    GAME = Game(ROOT)
    GAME.mainloop()


# In[ ]:





# In[ ]:




