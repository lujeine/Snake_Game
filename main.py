from turtle import *
import time
from Snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # eat food
    if snake.head.distance(food) < 20:
        food.refresh()
        score_board.increase_score()
        snake.extend()

    # detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    # detect collision with snake body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            score_board.reset()
            snake.reset()

screen.exitonclick()
