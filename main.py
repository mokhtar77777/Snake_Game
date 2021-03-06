from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

dt = 0.1
prev_repeat = False
prev_score = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(dt)
    snake.move()
    screen.onkey(fun=snake.right, key='Right')
    screen.onkey(fun=snake.left, key='Left')
    screen.onkey(fun=snake.up, key='Up')
    screen.onkey(fun=snake.down, key='Down')

    if snake.segments[0].distance(food) < 17:
        scoreboard.update_score()
        snake.add_new_segment()
        food.generate_new_location()

    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        # game_is_on = False
        snake.reset_snake()
        scoreboard.high_score_trigger()
        dt = 0.1
        prev_score = 0

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) <= 10:
            # game_is_on = False
            snake.reset_snake()
            scoreboard.high_score_trigger()
            dt = 0.1
            prev_score = 0

    if scoreboard.score % 5 == 0 and round(dt, 5) > 0.04:
        if prev_score != scoreboard.score:
            dt -= 0.01
            print(dt)
            prev_score = scoreboard.score


screen.exitonclick()

# list_of_words = ["hello", "maroon", "baba", "haidi", "host", "hehe"]
# predicted_words = []
# user_response = input().lower()
# num_of_char = len(user_response)
# for word in list_of_words:
#     exist = True
#     for char_number in range(num_of_char):
#         if user_response[char_number] != word[char_number]:
#             exist = False
#     if exist:
#         predicted_words.append(word)
# print(predicted_words)

