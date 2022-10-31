import turtle 

turtle.shape("arrow")
turtle.speed(10)
turtle.color("red")

for i in range (20) :
  turtle.lt (80)
  turtle.fd (200)
  for i in range (4) :
    turtle.rt(145)
    turtle.fd(200)

turtle.exitonclick()
