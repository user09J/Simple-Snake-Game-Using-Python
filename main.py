from snake import Snake
import time
from turtle import Screen
from food import Food
from score_board import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600) 
screen.bgcolor =("white")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
	screen.update()
	time.sleep(0.1)
	snake.move()

	#if snake meet the Food we have to add extra segment to the snake
	if snake.head.distance(food) < 15:
		food.refresh()
		snake.extend()
		scoreboard.increase_score()

	#Detect Collision With Wall
	if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		scoreboard.reset()
		snake.reset()


	#Detect Collision With Tail
	for segment in snake.segments[1:]:		
		if segment == snake.head:
			pass
		elif snake.head.distance(segment) < 10:
			scoreboard.reset()
			snake.reset()



screen.exitonclick()