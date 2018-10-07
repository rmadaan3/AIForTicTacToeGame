
import unittest
from a2 import game1
from a2 import game2
from a2 import game3
from a2 import game
from a2 import win
from a2 import validBoard
from a2 import validmove

import a2


# TEST cases should cover t different boundary cases.

class testpoint(unittest.TestCase):
	def test_validmove(self) :
		import tile
		tile.tile1 = tile.tile3 = tile.tile5 = 1 ; tile.tile2 = tile.tile7 = 2 ; tile.tile4 = tile.tile6 = tile.tile8 = tile.tile9 = 0  #This is the state at the given time
		self.assertEqual(validmove(3),False)
		self.assertEqual(validmove(8),True)
		self.assertEqual(validmove(9),True)
		tile.tile1 = tile.tile3 = tile.tile8 = 1 ; tile.tile2 = 2 ; tile.tile4 = tile.tile6 = tile.tile7 = tile.tile5 = tile.tile9 = 0 #This is the state at the given time
		self.assertEqual(validmove(7),True)	
		self.assertEqual(validmove(7),True)	
		tile.tile1 = tile.tile3 = tile.tile5 = 2 ; tile.tile2 = tile.tile7 = 1 ; tile.tile4 = tile.tile6 = tile.tile8 = tile.tile9 = 0 #This is the state at the given time
		self.assertEqual(validmove(4),True)
		tile.tile1 = tile.tile2 = tile.tile4 = 2 ; tile.tile5 = tile.tile6 = tile.tile7 = tile.tile9 = 1 ; tile.tile8 = tile.tile3 = 0#This is the state at the given time
		self.assertEqual(validmove(1),False)
		self.assertEqual(validmove(2),False)
		
	def test_win(self) :
		import tile
		tile.tile1 = tile.tile3 = tile.tile5 = 1 ; tile.tile2 = tile.tile7 = 2 ; tile.tile4 = tile.tile6 = tile.tile8 = tile.tile9 = 0 #This is the state at the given time
		self.assertEqual(win(),False)
		tile.tile1 = tile.tile3 = tile.tile5 = 1 ; tile.tile2 = 2 ; tile.tile4 = tile.tile6 = tile.tile7 = tile.tile8 = tile.tile9 = 0 #This is the state at the given time
		self.assertEqual(win(),False)		
		tile.tile1 = tile.tile3 = tile.tile5 = 2 ; tile.tile2 = tile.tile7 = 1 ; tile.tile4 = tile.tile6 = tile.tile8 = tile.tile9 = 0 #This is the state at the given time
		self.assertEqual(win(),False)
		tile.tile1 = tile.tile2 = tile.tile3 = tile.tile4 = 2 ; tile.tile5 = tile.tile6 = tile.tile7 = tile.tile9 = 1 ; tile.tile8 = 0 #This is the state at the given time
		self.assertEqual(win(),True)
		tile.tile1 = tile.tile3 = tile.tile5 = 1 ; tile.tile2 = tile.tile7 =tile.tile9 = 2 ; tile.tile4 = tile.tile6 = tile.tile8  = 0 #This is the state at the given time
		self.assertEqual(win(),False)
		
	def test_validBoard(self):
		import tile
		tile.move1=5
		tile.move2=5
		self.assertEqual(validBoard(),True)
		tile.move1=5
		tile.move2=6
		self.assertEqual(validBoard(),False)		
		tile.move1=0
		tile.move2=1
		self.assertEqual(validBoard(),False)
		tile.move1=1
		tile.move2=0
		self.assertEqual(validBoard(),True)
	
	def test_game(self):
		self.assertEqual(game(3),0)

	def test_game1(self):
		self.assertAlmostEqual(game1(1000), 0.35,delta=0.15)
		self.assertAlmostEqual(game1(10000),0.35,delta=0.15)
		self.assertAlmostEqual(game1(100), 0.35,delta=0.15)
		self.assertAlmostEqual(game1(250), 0.35,delta=0.15)
		self.assertAlmostEqual(game1(2000), 0.35,delta=0.15)
		
	def test_game2(self):
		self.assertAlmostEqual(game2(1000), 0, delta=0.1)
		self.assertAlmostEqual(game2(10000),0, delta=0.1)
		self.assertAlmostEqual(game2(100), 0, delta=0.1)
		self.assertAlmostEqual(game2(250), 0, delta=0.1)
		self.assertAlmostEqual(game2(2000), 0, delta=0.1)
	
	def test_game3(self):
		self.assertAlmostEqual(game3(1000), 0)
		self.assertAlmostEqual(game3(10000),0)
		self.assertAlmostEqual(game3(100), 0)
		self.assertAlmostEqual(game3(250),0)
		self.assertAlmostEqual(game3(2000), 0) 

	
	
	

if __name__=='__main__':
	unittest.main()
