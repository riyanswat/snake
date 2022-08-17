from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
# Screen stuff
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# screen.onkey(snake.grow, 'space') # something to think about


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)  # changing it to a value below 0.1 will make the snake move too fast...
# think about incorporating this feature into the Snake class to make levels i.e. easy, hard etc
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with the border
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
