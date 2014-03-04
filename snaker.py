# snaker! by Ethan Jurman
# the snake goes around the screen and when it hits the rat it gets points for the amount of distance it traveled from his tail
import random
import math
import tkinter as Tkinter
canvasSize = 300

class Snake:
	def __init__(self, canvas):
		self.points = 0
		self.head = (0,10)
		self.body = []
		self.tail = (0,0)
		self.direction = "up"
		self.canvas = canvas
		self.rat = (round(random.randrange(canvasSize - 10), -1), round(random.randrange(canvasSize - 10), -1))
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
		
	def eraseSnake(self):
		for i in range(len(self.body)):
			sect = self.body[i]
			self.canvas.create_rectangle(sect[0], sect[1], sect[0] + 10, sect[1] + 10, fill="white", outline="grey")
		
	def update(self):
		self.body.append(self.head)
		print(self.head)
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
		if self.head == self.rat:
			print("LEVEL UP")
			self.speed = round(self.speed / 1.2)
			self.points += int((len(self.body) * len(self.body)) // 10 * self.level)
			self.eraseSnake()
			print("POINTS: " + str(self.points))
			self.feed()
			self.drawRat()
		self.drawSnake()
		if self.run:
			speedMod = len(self.body)
			if len(self.body) > 30:
				speedMod = 30
			self.canvas.after(self.speed - speedMod, self.update)
		else:
			#self.canvas.after(500, newGame)
			pass
	
	def changeDirection(self, event):
		direction = event.char
		if direction == "s" and self.direction != "down":
			self.direction = "up"
		elif direction == "w" and self.direction != "up":
			self.direction = "down"
		elif direction == "a" and self.direction != "right":
			self.direction = "left"
		elif direction == "d" and self.direction != "left":
			self.direction = "right"
		
	def feed(self):
		self.body = []
		self.tail = self.head
		self.rat = (round(random.randrange(canvasSize), -1), round(random.randrange(canvasSize), -1))
		self.drawRat()
		
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