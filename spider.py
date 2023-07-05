# Tic Tac Toe in python
# Python version 3.9.1
# by @Maturana
# date: 06/26/2022

import turtle
import tkinter as tk
from turtle import Screen, Turtle
from functools import partial
import os
import logging
from game_logic import GameLogic
import time

logging.basicConfig(filename="log.txt", encoding='utf-8', level=logging.INFO)

# Global Variable
GAME_ON = True
SCORE1 = 0
SCORE2 = 0


logging.info("Starting Tic-Tac-Toe Spider")
# Main Window
wn = turtle.Screen()
wn.title("Tic Tac Toe")
wn.bgcolor("purple")
wn.setup(width= 800, height=640)
wn.tracer(0)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)


# Second Layer: Field of play
# Field
border= turtle.Turtle()
border.speed(0)
border.shape("square")
border.shapesize(stretch_wid=24.1,stretch_len=24.1)
border.color("white")
border.penup()
border.goto(0,0)

field_ = turtle.Turtle()
field_.speed(0)
field_.shape("square")
field_.shapesize(stretch_wid=23.5,stretch_len=23.5)
field_.color("green")
field_.penup()
field_.goto(0,0)

border2 = turtle.Turtle()
border2.speed(0)
border2.shape("square")
border2.shapesize(stretch_wid=0.3,stretch_len=24)
border2.color("white")
border2.penup()
border2.goto(0,0)

border3 = turtle.Turtle()
border3.speed(0)
border3.shape("square")
border3.shapesize(stretch_wid=24,stretch_len=0.3)
border3.color("white")
border3.penup()
border3.goto(0,0)

border4 = turtle.Turtle()
border4.speed(0)
border4.shape("square")
border4.shapesize(stretch_wid=33.5,stretch_len=0.3)
border4.color("white")
border4.left(45)
border4.penup()
border4.goto(0,0)

border5 = turtle.Turtle()
border5.speed(0)
border5.shape("square")
border5.shapesize(stretch_wid=33.5,stretch_len=0.3)
border5.color("white")
border5.right(45)
border5.penup()
border5.goto(0,0)

pos1 = turtle.Turtle()
pos1.color("white")
pos1.shape('circle')
pos1.shapesize(stretch_wid=2,stretch_len=2)
pos1.goto(-240,240)

pos2 = turtle.Turtle()
pos2.color("white")
pos2.shape('circle')
pos2.shapesize(stretch_wid=2,stretch_len=2)
pos2.goto(0,240)

pos3 = turtle.Turtle()
pos3.color("white")
pos3.shape('circle')
pos3.shapesize(stretch_wid=2,stretch_len=2)
pos3.goto(240,240)

pos4 = turtle.Turtle()
pos4.color("white")
pos4.shape('circle')
pos4.shapesize(stretch_wid=2,stretch_len=2)
pos4.goto(-240,0)

pos5 = turtle.Turtle()
pos5.color("white")
pos5.shape('circle')
pos5.shapesize(stretch_wid=2,stretch_len=2)
pos5.goto(0,0)

pos6 = turtle.Turtle()
pos6.color("white")
pos6.shape('circle')
pos6.shapesize(stretch_wid=2,stretch_len=2)
pos6.goto(240,0)

pos7 = turtle.Turtle()
pos7.color("white")
pos7.shape('circle')
pos7.shapesize(stretch_wid=2,stretch_len=2)
pos7.goto(-240,-240)

pos8 = turtle.Turtle()
pos8.color("white")
pos8.shape('circle')
pos8.shapesize(stretch_wid=2,stretch_len=2)
pos8.goto(0,-240)

pos9 = turtle.Turtle()
pos9.color("white")
pos9.shape('circle')
pos9.shapesize(stretch_wid=2,stretch_len=2)
pos9.goto(240,-240)

#player 1
player1a = turtle.Turtle()
player1a.speed(0)
player1a.shape("circle")
player1a.color("black")
player1a.fillcolor("yellow")
player1a.shapesize(stretch_wid=2,stretch_len=2)
player1a.penup()   
player1a.goto(340,40)
player1a.dx = 10
player1a.dy = 10

player1b = turtle.Turtle()
player1b.speed(0)
player1b.shape("circle")
player1b.color("black")
player1b.fillcolor("yellow")
player1b.shapesize(stretch_wid=2,stretch_len=2)
player1b.penup()   
player1b.goto(340,90)
player1b.dx = 10
player1b.dy = 10

player1c = turtle.Turtle()
player1c.speed(0)
player1c.shape("circle")
player1c.color("black")
player1c.fillcolor("yellow")
player1c.shapesize(stretch_wid=2,stretch_len=2)
player1c.penup()   
player1c.goto(340,140)
player1c.dx = 10
player1c.dy = 10

#square
player2a = turtle.Turtle()
#player2a.speed(0)
player2a.color("black")
player2a.fillcolor("red")
player2a.shape('circle')
player2a.shapesize(stretch_wid=2,stretch_len=2)
player2a.penup()   
player2a.goto(-340,-40)
player2a.dx = 10
player2a.dy = 10


player2b = turtle.Turtle()
#player2b.speed(0)
player2b.color("black")
player2b.fillcolor("red")
player2b.shape('circle')
player2b.shapesize(stretch_wid=2,stretch_len=2)
player2b.penup()  
player2b.width(5)
player2b.goto(-340,-90)
player2b.dx = 10
player2b.dy = 10


player2c = turtle.Turtle()
#player2c.speed(0)
player2c.color("black")
player2c.fillcolor("red")
player2c.shape('circle')
player2c.shapesize(stretch_wid=2,stretch_len=2)
player2c.penup()
player2c.goto(-340,-140)
player2c.dx = 10
player2c.dy = 10

# function to move player 1 chip a
def move_player_1a(x,y):
	player1a.ondrag(None)
	logging.info("P1a")
	player1a.setheading(player1a.towards(x,y))
	player1a.goto(x,y)
	print(player1a.position())
	logging.info("P1a Position: " + player1a.position())
	player1a.ondrag(move_player_1a)

# function to move player 1 chip b
def move_player_1b(x,y):
	print("Moving P1b")
	player1b.ondrag(None)
	player1b.setheading(player1b.towards(x,y))
	player1b.goto(x,y)
	print(player1b.position())
	print("This is x cor: " + playar1b.xcor())
	print("This is x cor: " + player1b.ycor())
	logging.info("P1b Position: " + player1b.position())
	player1b.ondrag(move_player_1b)

# function to move player 1 chip c
def move_player_1c(x,y):
	print("Moving P1c")
	player1c.ondrag(None)
	player1c.setheading(player1c.towards(x,y))
	player1c.goto(x,y)
	print(player1c.position())
	logging.info("P1c Position: " + player1c.position())
	player1c.ondrag(move_player_1c)

# function to move player 2 chip a
def move_player_2a(x,y):
	print("Moving p2a")
	player2a.ondrag(None)
	player2a.setheading(player2a.towards(x,y))
	player2a.goto(x,y)
	print(player2a.position())
	logging.info("P2a Position: " + player2a.position())
	player2a.ondrag(move_player_2a)

# function to move player 2 chip b
def move_player_2b(x,y):
	print("Moving p2b")
	player2b.ondrag(None)
	player2b.setheading(player2b.towards(x,y))
	player2b.goto(x,y)
	print(player2b.position())
	logging.info("P2b Position: " + player2b.position())
	player2b.ondrag(move_player_2b)

# function to move player 2 chip c
def move_player_2c(x,y):
	print("Moving p2c")
	player2c.ondrag(None)
	player2c.setheading(player2c.towards(x,y))
	player2c.goto(x,y)
	print(player2c.position())
	logging.info("P2c Position: " + player2c.position())
	player2c.ondrag(move_player_2c)

# creates the help menue item
def help_():
	help_button = turtle.Turtle()
	help_button.shape("square")
	help_button.color("white")
	help_button.penup()
	help_button.hideturtle()
	help_button.goto(-340,300)
	help_button.write("HELP [h]", align="center", font=("Courier", 16, "normal"))
	help_button.dx = 50
	help_button.dy = 15

# creates the close menu item
def close_():
	close_button = turtle.Turtle()
	close_button.shape("square")
	close_button.color("white")
	close_button.penup()
	close_button.hideturtle()
	close_button.goto(-240,300)
	close_button.write("ClOSE [x]", align="center", font=("Courier", 16, "normal"))
	close_button.dx = 50
	close_button.dy = 15

# Creates the restart menu item
def restart_():
	restart_button = turtle.Turtle()
	restart_button.shape("square")
	restart_button.color("white")
	restart_button.penup()
	restart_button.hideturtle()
	restart_button.goto(-120,300)
	restart_button.write("RESTART [r]", align="center", font=("Courier", 16, "normal"))
	restart_button.dx = 50
	restart_button.dy = 15

# help window popup
# it will be binded to the letter 'h'
def help_function():
	msg = "Implementation is needed\n" + "   This is just a test   "
	popup = tk.Tk()
	popup.wm_title("HELP")
	def close_popup():
		print("Help window has been closed")
		popup.destroy()
	label = tk.Label(popup, text=msg)
	label.pack(side="top", fill="x", pady=10)
	btn = tk.Button(popup, text="OK", command=close_popup)
	btn.pack()
	print("help function has been activated")
	move_players()

# End the game
# it will be binded to the letter c
def close_function():
	print("Game has been closed")
	wn.bye()

# resets players to initial position
# it will be bind to the letter 'r'
def restart_function(str = None):
	player1a.goto(300,40)
	player1b.goto(300,90)
	player1c.goto(300,140)
	player2a.goto(-300,-40)
	player2b.goto(-300,-90)
	player2c.goto(-300,-140)
	player1a.fillcolor("yellow")
	player1b.fillcolor("yellow")
	player1c.fillcolor("yellow")
	player2a.fillcolor("red")
	player2b.fillcolor("red")
	player2c.fillcolor("red")
	if str != None:
		print(str)
	move_players()

# user is able to drag and move the chips
def move_players():
	# player 2 moves
	player2b.ondrag(move_player_2b)
	player2a.ondrag(move_player_2a)
	player2c.ondrag(move_player_2c)
	# player 1 moves
	player1b.ondrag(move_player_1b)
	player1a.ondrag(move_player_1a)
	player1c.ondrag(move_player_1c)

def close_wn():
	wn.bye()

# Banner that displays the games scores
def close_game_banner():
	banner = turtle.Turtle()
	banner.speed(0)
	banner.shape("square")
	banner.color("white")
	banner.penup()
	banner.hideturtle()
	banner.goto(0,-310)
	banner.write("Press Esc Key to Exit Game", align="center", font=("Courier", 24, "normal"))

def refresh():
	wn.update()
	time.sleep(2)	
	restart_function()
	wn.update()
	time.sleep(0.5)
	restart_function()

# Keyboard bindings
wn.listen()
wn.onkeypress(close_wn,"Escape")
wn.onkeypress(help_function, "h")
wn.onkeypress(close_function, "x")
wn.onkeypress(restart_function, "r")
# End of Keyboard bindings

def main():
	game = GameLogic()
	score_1 = 0
	score_2 = 0

	def winning ():

		if game.diagonal_forward(player1a, player1b, player1c):
			return 1
		if game.diagonal_forward(player2a, player2b, player2c):
			return 2
		if game.diagonal_backward(player1a, player1b, player1c):
			return 1
		if game.diagonal_backward(player2a, player2b, player2c):
			return 2
		if game.horizontal_top(player1a, player1b, player1c):
			return 1
		if game.horizontal_top(player2a, player2b, player2c):
			return 2
		if game.horizontal_middle(player1a, player1b, player1c):
			return 1
		if game.horizontal_middle(player2a, player2b, player2c):
			return 2
		if game.horizontal_bottom(player1a, player1b, player1c):
			return 1
		if game.horizontal_bottom(player2a, player2b, player2c):
			return 2
		if game.vertical_left(player1a, player1b, player1c):
			return 1
		if game.vertical_left(player2a, player2b, player2c):
			return 2
		if game.vertical_middle(player1a, player1b, player1c):
			return 1
		if game.vertical_middle(player2a, player2b, player2c):
			return 2
		if game.vertical_right(player1a, player1b, player1c):
			return 1
		if game.vertical_right(player2a, player2b, player2c):
			return 2

	while GAME_ON:

		help_()
		close_()
		restart_()
		close_game_banner()
		move_players()

		# These allow the players to aligned the chip or token to the correct spot on the board
		game.position(player2a)
		game.position(player2b)
		game.position(player2c)
		game.position(player1a)
		game.position(player1b)
		game.position(player1c)
		
		if winning() == 1:
			score_1 += 1
			refresh() # this function is needed so the score does not increase for the same win

		if winning() == 2:
			score_2 += 1
			refresh()

		pen.clear()
		pen.write("Yellow: {} Red: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))

		wn.update()


# calling main function
if __name__ == "__main__":

	main()
	


	

