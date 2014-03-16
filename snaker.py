# snaker! by Ethan Jurman
# the snake goes around the screen and when it hits the rat it gets points for the amount of distance it traveled from his tail and goes to the next level
# if the snake hits a mouse, it will increase the points at the end of the level based on the distance of the snake tail to the mice.
import random
import math
import tkinter as Tkinter
canvasSize = 300

class Snake:
	def __init__(self, canvas):
		self.points = 0
		self.head = (0,10)
		self.body = []
		self.direction = "up"
		self.nDirection = "up"
		self.canvas = canvas
		self.rat = randomPosition()
		self.mice = [randomPosition(), randomPosition(), randomPosition(), randomPosition()]
		self.scoreIncr = 1
		self.run = True
		self.speed = 150
		self.level = 1
		self.drawRat()
		
	def drawSnake(self):
		x = (self.head[0] // 10)*10
		y = (self.head[1] // 10)*10
		self.canvas.create_rectangle(x, y, x+10, y+10, fill="yellow", outline="grey")
		
	def drawRat(self):
		x = (self.rat[0] // 10)*10
		y = (self.rat[1] // 10)*10
		self.canvas.create_rectangle(x, y, x+10, y+10, fill="green", outline="grey")
		for mouse in self.mice:
			x = (mouse[0] // 10)*10
			y = (mouse[1] // 10)*10
			self.canvas.create_rectangle(x, y, x+10, y+10, fill="orange", outline="grey")
			
		
	def eraseSnake(self):
		for i in range(len(self.body)):
			sect = self.body[i]
			self.canvas.create_rectangle(sect[0], sect[1], sect[0] + 10, sect[1] + 10, fill="white", outline="grey")
		for mouse in self.mice:
			x = (mouse[0] // 10)*10
			y = (mouse[1] // 10)*10
			self.canvas.create_rectangle(x, y, x+10, y+10, fill="white", outline="grey")
		
	def update(self):
		self.body.append(self.head)
		self.direction = self.nDirection
		if self.direction == "up":
			self.head = (self.head[0], self.head[1]+10)
		elif self.direction == "down":
			self.head = (self.head[0], self.head[1]-10)
		elif self.direction == "left":
			self.head = (self.head[0]-10, self.head[1])
		elif self.direction == "right":
			self.head = (self.head[0]+10, self.head[1])
		if self.head in self.body or (canvasSize in self.head) or (-10 in self.head):
			print("GAME OVER")
			self.run = False
		if self.head in self.mice:
			self.scoreIncr += (1/len(self.body)) * canvasSize
		if self.head == self.rat:
			self.level += 1
			print("LEVEL UP: " + str(self.level) )
			self.speed = round(self.speed / 1.05)
			self.points += (len(self.body) // 10 * self.level) * int(self.scoreIncr)
			self.eraseSnake()
			print("POINTS: " + str(self.points))
			self.feed()
			self.drawRat()
		self.drawSnake()
		if self.run:
			speedMod = len(self.body)
			if len(self.body) > self.level * 10:
				speedMod = self.level * 10
			self.canvas.after(self.speed - speedMod, self.update)
		else:
			#self.canvas.after(500, newGame)
			pass
	
	def changeDirection(self, event):
		direction = event.char
		if direction == "s" and self.nDirection != "down":
			self.nDirection = "up"
		elif direction == "w" and self.nDirection != "up":
			self.nDirection = "down"
		elif direction == "a" and self.nDirection != "right":
			self.nDirection = "left"
		elif direction == "d" and self.nDirection != "left":
			self.nDirection = "right"
		
	def feed(self):
		self.body = []
		self.rat = randomPosition()
		self.mice = [randomPosition(),randomPosition(),randomPosition(),randomPosition()]
		self.drawRat()
		
def randomPosition():
	return (round(random.randrange(canvasSize - 20), -1), round(random.randrange(canvasSize - 20), -1))
		
def newGame():
	top = Tkinter.Tk()
	top.configure(bg="white")
	can = Tkinter.Canvas(top, width=canvasSize, height=canvasSize)
	can.pack()
	can.focus_set()

	can.create_rectangle(0, 0, canvasSize, canvasSize, fill="white", outline="grey")

	snake = Snake(can)

	#grid lines
	for i in range(0, canvasSize, 10):
		can.create_line(0, i, canvasSize, i, fill="grey")
		can.create_line(i, 0, i, canvasSize, fill="grey")
		
	top.after(500, snake.update)
	can.bind("<Key>", snake.changeDirection)
	
	top.mainloop()

if __name__ == '__main__':
	newGame()