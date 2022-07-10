# Tic Tac Toe in python
# Python version 3.9.1
# File name; game_logic.py
# by @Maturana
# date: 06/30/2022

import turtle
import tkinter as tk
from turtle import Screen, Turtle
from functools import partial
import os
import logging
import time

class position:

    POS1 = '(-240.00,240.00)'
    POS2 = '(240.00,0.00)'
    POS3 = '(240.00,240.00)'
    POS4 = '(-240.00,0.00)'
    POS5 = '(0.00,0.00)'
    POS6 = '(0.00,240.00)'
    POS7 = '(-240.00, -240.00)'
    POS8 = '(0.00,-240.00)'
    POS9 = '(-240.00,-240.00)'
    
class GameLogic:

	def __init__(self):
		''' init '''
		self._matrix = [['','',''],['','',''],['','','']]

	# token or chip colors change when there is a winner
	def win_color(self, obj1, obj2, obj3):

		obj1.fillcolor('blue')
		obj2.fillcolor('blue')
		obj3.fillcolor('blue')

		
	def game_logic(self, x1, x2, x3, l1, l2, l3):

		if(str(x1.position()) == l1 and str(x2.position()) == l2 and str(x3.position()) == l3):
			print("Player wins")
			self.win_color(x1, x2, x3)
			return True

		if(str(x2.position()) == l1 and str(x3.position()) == l2 and str(x1.position()) == l3):
			print("Plyaer wins")
			self.win_color(x1, x2, x3)
			return True

		if(str(x3.position()) == l1 and str(x1.position()) == l2 and str(x2.position()) == l3):
			print("Plyaer wins")
			self.win_color(x1, x2, x3)
			return True

		if(str(x1.position()) == l1 and str(x3.position()) == l2 and str(x2.position()) == l3):
			print("Plyaer wins")
			self.win_color(x1, x2, x3)
			return True

		if(str(x2.position()) == l1 and str(x1.position())== l2 and str(x3.position()) == l3):
			print("Plyaer wins")
			self.win_color(x1, x2, x3)
			return True

		if(str(x3.position()) == l1 and str(x2.position()) == l2 and str(x1.position()) == l3):
			print("Plyaer wins")
			self.win_color(x1, x2, x3)
			return True

		else:
			print("No winner")
			return False


	# function returns true if the all chips line up diagonally
	def diagonal_forward(self, x1, x2, x3):
		return self.game_logic(x1, x2, x3, '(-240.00,240.00)', '(0.00,0.00)', '(240.00,-240.00)')

	# function returns true if the all chips line up diagonally
	def diagonal_backward(self, x1, x2, x3):
		return self.game_logic(x1, x2, x3, '(-240.00,-240.00)', '(0.00,0.00)', '(240.00,240.00)')

	def horizontal_top(self, x1, x2, x3):
		return self.game_logic(x1, x2, x3, '(-240.00,240.00)', '(0.00,240.00)', '(240.00,240.00)')

	def horizontal_middle(self, x1, x2, x3):
		return self.game_logic(x1, x2, x3, '(-240.00,0.00)', '(0.00,0.00)', '(240.00,0.00)')

	def horizontal_bottom(self, x1, x2, x3):
		return self.game_logic(x1,x2, x3, '(-240.00,-240.00)', '(0.00,-240.00)', '(240.00,-240.00)')

	def vertical_left(self, x1, x2, x3):
		return self.game_logic(x1, x2, x3, '(-240.00,240.00)', '(-240.00,0.00)', '(-240.00,-240.00)')

	def vertical_middle(self, x1, x2, x3):
		return self.game_logic(x1, x2, x3, '(0.00,240.00)', '(0.00,0.00)', '(0.00,-240.00)')

	def vertical_right(self, x1, x2, x3):
		return self.game_logic(x1, x2, x3, '(240.00,-240.00)', '(240.00,0.00)', '(240.00,240.00)')

	# Following fucntion return empty positions
	def possible_plays(self, x1, x2, x3, x4, x5, x6):

		self.list_chips = [str(x1.position()), str(x2.position()), str(x3.position()), 
						   str(x4.position()), str(x5.position()), str(x6.position())]		
	
		self.list_ = ['(0.00,0.00)','(-240.00,0.00)','(-240.00,-240.00)', 
		              '(-240.00,240.00)','(240.00,0.00)','(240.00,-240.00)',
		              '(240.00,240.00)', '(0.00,-240.00)','(0.00,240.00)']

		# checking if an space is not taken
		for i in self.list_chips:
			for j in self.list_:
				if(i==j):
					self.list_.remove(j)

		return self.list_

	# Future implementation to make the computer play
	def computer_play(self, obj, x1, x2, x3, x4, x5):
		cnt = 0 	# counter
		self.list_ = []		#creates a list

		# position 1
		if (obj.position() == position.POS1):
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS2):
				print ("Move " + str(obj) + " to " + position.POS2)
				obj.goto(0,240)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS5):
				print ("Move " + str(obj) + " to " + position.POS5)
				obj.goto(0,0)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS4):
				print ("Move " + str(obj) + " to " + position.POS4)
				obj.goto(-240,0)

		# position 2
		if (obj.position() == position.POS2):
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS1):
				print ("Move " + str(obj) + " to " + position.POS1)
				obj.goto(-240,240)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS5):
				print ("Move " + str(obj) + " to " + position.POS5)
				obj.goto(0,0)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS3):
				print ("Move " + str(obj) + " to " + position.POS3)
				obj.goto(240,240)

		# position 3
		if (obj.position() == position.POS3):
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS2):
				print ("Move " + str(obj) + " to " + position.POS2)
				obj.goto(0,240)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS5):
				print ("Move " + str(obj) + " to " + position.POS5)
				obj.goto(0,0)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS6):
				print ("Move " + str(obj) + " to " + position.POS6)
				obj.goto(-240,0)

		# position 4
		if (obj.position() == position.POS4):
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS1):
				print ("Move " + str(obj) + " to " + position.POS1)
				obj.goto(-240,240)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS5):
				print ("Move " + str(obj) + " to " + position.POS5)
				obj.goto(0,0)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS7):
				print ("Move " + str(obj) + " to " + position.POS7)
				obj.goto(240,240)

		# position 5
		if (obj.position() == position.POS5):
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS1):
				print ("Move " + str(obj) + " to " + position.POS1)
				obj.goto(-240,240)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS2):
				print ("Move " + str(obj) + " to " + position.POS2)
				obj.goto(0,240)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS3):
				print ("Move " + str(obj) + " to " + position.POS3)
				obj.goto(240,240)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS4):
				print ("Move " + str(obj) + " to " + position.POS4)
				obj.goto(0,240)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS5):
				print ("Move " + str(obj) + " to " + position.POS5)
				obj.goto(0,0)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS6):
				print ("Move " + str(obj) + " to " + position.POS6)
				obj.goto(-240,0)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS7):
				print ("Move " + str(obj) + " to " + position.POS7)
				obj.goto(0,0)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS8):
				print ("Move " + str(obj) + " to " + position.POS8)
				obj.goto(-240,0)

		# position 6
		if (obj.position() == position.POS6):
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS1):
				print ("Move " + str(obj) + " to " + position.POS1)
				obj.goto(-240,240)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS5):
				print ("Move " + str(obj) + " to " + position.POS5)
				obj.goto(0,0)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS3):
				print ("Move " + str(obj) + " to " + position.POS3)
				obj.goto(240,240)

		# position 7
		if (obj.position() == position.POS7):
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS4):
				print ("Move " + str(obj) + " to " + position.POS4)
				obj.goto(-240,0)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS5):
				print ("Move " + str(obj) + " to " + position.POS5)
				obj.goto(0,0)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS8):
				print ("Move " + str(obj) + " to " + position.POS8)
				obj.goto(0,-240)

		# position 8
		if (obj.position() == position.POS8):
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS7):
				print ("Move " + str(obj) + " to " + position.POS7)
				obj.goto(-240,-240)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS5):
				print ("Move " + str(obj) + " to " + position.POS5)
				obj.goto(0,0)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS9):
				print ("Move " + str(obj) + " to " + position.POS9)
				obj.goto(240,-240)

		# position 9
		if (obj.position() == position.POS9):
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS6):
				print ("Move " + str(obj) + " to " + position.POS1)
				obj.goto(240,0)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS8):
				print ("Move " + str(obj) + " to " + position.POS5)
				obj.goto(0,-240)
			if self._ocupied(x1, x2, x3, x4, x5, postion.POS5):
				print ("Move " + str(obj) + " to " + position.POS3)
				obj.goto(0,0)

	# this function allows the player to position the chip or token exactly in one of the 9 spots
	def position(self, obj):

		# position 1
		if ((obj.ycor() < 300 and obj.ycor() > 180) and (obj.xcor() > -300 and obj.xcor() < -180)):
			obj.goto(-240,240)
		# position 2
		if ((obj.ycor() < 300 and obj.ycor() > 180) and (obj.xcor() > -180 and obj.xcor() < 180)):
			obj.goto(0,240)
		# position 3
		if ((obj.ycor() < 300 and obj.ycor() > 180) and (obj.xcor() < 300 and obj.xcor() > 180)):
			obj.goto(240,240)
		# position 4
		if ((obj.ycor() < 60 and obj.ycor() > -60) and (obj.xcor() > -300 and obj.xcor() < -180)):
			obj.goto(-240,0)
		# position 5
		if ((obj.ycor() < 60 and obj.ycor() > -60) and (obj.xcor() > -60 and obj.xcor() < 60)):
			obj.goto(0,0)
		# position 6
		if ((obj.ycor() < 60 and obj.ycor() > -60) and (obj.xcor() > 180 and obj.xcor() < 300)):
			obj.goto(240,0)
		# position 7
		if ((obj.ycor() < -180 and obj.ycor() > -300) and (obj.xcor() > -300 and obj.xcor() < -180)):
			obj.goto(-240,-240)
		# position 8
		if ((obj.ycor() < -180 and obj.ycor() > -300) and (obj.xcor() > -60 and obj.xcor() < 60)):
			obj.goto(0,-240)
		# poistion 9
		if ((obj.ycor() < -180 and obj.ycor() > -300) and (obj.xcor() < 300 and obj.xcor() > 180)):
			obj.goto(240,-240)

	# The following function return False if a position is occupied
	def _ocupied(self, obj1, obj2, obj3, obj4, obj5, position):
		if (str(obj.position()) == position):
			return False 
		if (str(obj.position()) == position):
			return False
		if (str(obj.position()) == position):
			return False	
		if (str(obj.position()) == position):
			return False
		if (str(obj.position()) == position):
			return False
		else:
			return True


# testing the class
def main():
	sample = GameLogic()
	sample.test()


# calling main fucntion
if __name__ == '__main__':

	main()





