Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Turtle()
>>> t.shape("turtle")
>>> 
>>> lista = []
>>> lista.append(int(input("x1:  ")))
x1:  0
>>> lista.append(int(input("y1:  ")))
y1:  0
>>> lista.append(int(input("x2:  ")))
x2:  100
>>> lista.append(int(input("y2:  ")))
y2:  100
>>> lista.append(int(input("x3:  ")))
x3:  200
>>> lista.append(int(input("y3:  ")))
y3:  100
>>> t.goto(lista[0], lista[1])
>>> t.goto(lista[2]. lista[3])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    t.goto(lista[2]. lista[3])
AttributeError: 'int' object has no attribute 'lista'
>>> t.goto(lista[2], lista[3])
>>> t.goto(lista[4], lista[5])
>>> t._screen.exitonclick()
