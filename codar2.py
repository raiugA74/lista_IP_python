def produto(a, b):
    if (a == 1):
        return b
        
    else:
        return b + produto(a-1, b)

x = produto(2,3)
print(x)

def fibonacci(n):
    if (n==0):
        return 1
    elif n ==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

x= []
for i in range(0,17):
    x.append(fibonacci(i))
print(x)



import turtle
import time

myTurtle = turtle.Turtle()
myWin = turtle.Screen()


def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

time.sleep(8)
drawSpiral(myTurtle,100)
myWin.exitonclick()
