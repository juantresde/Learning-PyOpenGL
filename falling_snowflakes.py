from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
from random import randint

width, height = 400, 400								# width and height of the window
field_width, field_height = 460, 450					# size of window where snowflakes appear


RECT_DELAY = 0
RECT_DELAY1 = 20
dx = 0.07
dy = - 0.8
snowflakes = []


def refresh2d(width, height):
	glViewport(0, 0, width, height)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
	glMatrixMode (GL_MODELVIEW)
	glLoadIdentity()


def draw_circle(cx, cy, r, num_segments):				# drawing the circle
	theta = 2 * math.pi / num_segments
	c = math.cos (theta)
	s = math.sin(theta)
	t = 0.0

	x = r
	y = 0

	glBegin(GL_POLYGON)
	for i in range(0, num_segments):
		glVertex2f(x + cx, y + cy)
		
		t = x
		x = c * x - s * y
		y = s * t + c * y

	glEnd()


def snow_random(value):									# generation of snowflakes 
	r = randint(0,50)
	if r == 0:
		x, y = randint(-30, field_width), randint(420, field_height) 
		snowflakes.append({"X":x,"Y": y})

	glutTimerFunc(RECT_DELAY, snow_random, 0)


def draw_snowflakes():									# drawing snowflakes 
	glColor3f(1.0, 1.0, 1.0)
	for i in snowflakes:
		draw_circle(i["X"],i["Y"], 0.9, 40)


def falling_of_snowflakes(value):						# falling and disappearing
	for i in snowflakes:
		i["X"] += dx
		i["Y"] += dy

		if i["Y"] <= 0 :
			snowflakes.remove(i)
	glutTimerFunc(RECT_DELAY1, falling_of_snowflakes, 0)


def draw():												# ondraw is called all the time
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)	# clear the screen
	glLoadIdentity()									# reset position

	# ToDo draw rectangle
	refresh2d(width, height)
	draw_snowflakes()

	glutSwapBuffers() 									# important for double buffering



	# initialization
glutInit()												# initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)						# set window size
glutInitWindowPosition(0, 0)							# set window position
window = glutCreateWindow("Falling snowflakes")				# create window with title
glutDisplayFunc(draw)									# set draw function callback
glutIdleFunc(draw)										# draw all the time
glutTimerFunc(RECT_DELAY, snow_random, 0)
glutTimerFunc(RECT_DELAY1, falling_of_snowflakes, 0)
glutMainLoop() 