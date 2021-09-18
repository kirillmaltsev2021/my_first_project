from turtle import *
import time

screen = Screen()
screen.screensize(1000,1000)

for i in range(8):
    forward(50)
    right(90)
for i in range(4):
    forward(250)
    right(90)
right(90/2)
forward(250*1.41)
mainloop()