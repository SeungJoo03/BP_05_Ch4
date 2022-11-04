Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
t = turtle.Turtle()
t.shpae("turtle")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t.shpae("turtle")
AttributeError: 'Turtle' object has no attribute 'shpae'. Did you mean: 'shape'?
t.shape("turtle")
\
lista = []
color = input("색상 #1를 입력하시오: ")
색상 #1를 입력하시오: yellow
lista.append(color)
color = input("색상 #2를 입력하시오: ")
색상 #2를 입력하시오: red
lista.append(color)
color = input("색상 #3를 입력하시오: ")
색상 #3를 입력하시오: blue
>>> lista.append(color)
>>> 
>>> t.fillcolor(lista[0])
>>> t.begin_fill()
>>> t.circle(50)
>>> t. end_fill()
>>> 
>>> t.up()
>>> t.goto(100, 0)
>>> t.down()
>>> t.fillcolor(lista[1]
... 
...    t.begin_fill()
...             
SyntaxError: '(' was never closed
>>> t.fillcolor(lista[1])
...             
>>> t.begin_fill()
...             
>>> t.circle(50)
...             
>>> t.end_fill()
...             
>>> t.up()
...             
>>> t.goto(200, 0)
...             
>>> t.down()
...             
>>> t.fillcolor(lista [2])
...             
>>> t.begin_fill()
...             
>>> t.circle(50)
...             
>>> t.end_fill()
...             
>>> t._screen.exitonclick()   # 화면을 마우스로 클릭해야 종료되게 하는 부분
...             
