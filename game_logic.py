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

class GameLogic:

	def __init__(self):
		''' init '''

	def game_logic(self, x1, x2, x3, l1, l2, l3):

		self.x1_ = x1
		self.x2_ = x2
		self.x3_ = x3
		self.l1_ = l1
		self.l2_ = l2
		self.l3_ = l3


		if(str(self.x1_.position()) == self.l1_ and str(self.x2_.position()) == self.l2_ and str(self.x3_.position()) == self.l3_):
			print("Players wins")
			return True

		if(str(self.x2_.position()) == self.l1_ and str(self.x3_.position()) == self.l2_ and str(self.x1_.position()) == self.l3_):
			print("Plyaers wins")
			return True

		if(str(self.x3_.position()) == self.l1_ and str(self.x1_.position()) == self.l2_ and str(self.x2_.position()) == self.l3_):
			print("Plyaers wins")
			return True

		if(str(self.x1_.position()) == self.l1_ and str(self.x3_.position()) == self.l2_ and str(self.x2_.position()) == self.l3_):
			print("Plyaers wins")
			rsl = True

		if(str(self.x2_.position()) == self.l1_ and str(self.x1_.position())== self.l2_ and str(self.x3_.position()) == self.l3_):
			print("Plyaers wins")
			return True

		if(str(self.x3_.position()) == self.l1_ and str(self.x2_.position()) == self.l2_ and str(self.x1_.position()) == self.l3_):
			print("Plyaers wins")
			return True

		else:
			print("No winner")
			return False



	# function returns true if the all chips line up diagonally
	def diagonal_forward(self, x1, x2, x3):
		print(x1.position())
		print(x2.position())
		print(x3.position())
		return self.game_logic(x1, x2, x3, '(-240.00,240.00)', '(0.00,0.00)', '(240.00,-240.00)')

	def diagonal_backward(self, x1, x2, x3):
		return self.game_logic(x1, x2, x3, '(-240.00,-240.00)', '(0.00,0.00)', '(240.00,240.00)')

	def horizontl_top(self, x1, x2, x3):
		return self.game_logic(x1, x2, x3, '(-240.00,240.00)', '(0.00,240.00)', '(240.00,240.00)')

	def horizontl_middle(self, x1, x2, x3):
		return self.ame_logic(x1, x2, x3, '(-240.00,0.00)', '(0.00,240.00)', '(0.00,240.00)')

	def horizontl_bottom(self, x1, x2, x3):
		return self.game_logic(x1,x2, x3, '(-240.00,-240.00)', '(0.00,-240.00)', '(240.00,-240.00)')

	def horizontl_lef(self, x1, x2, x3):
		return self.game_logic(x1, x2, x3, '(-240.00,240.00)', '(-240.00,0.00)', '(-240.00,-240.00)')

	def vertical_middle(self, x1, x2, x3):
		return self.game_logic(x1, x2, x3, "(0,240)", "(0,0)", "(0,-240)")

	def vertical_middle(self, x1, x2, x3):
		return self.game_logic(x1, x2, x3, "(240,-240)", "(240,0)", "(-240,-240)")


	def test(self):
		print("This is a test of class GameLogic")

# testing the class
def main():
	sample = GameLogic()
	sample.test()


# calling main fucntion
if __name__ == '__main__':

	main()









