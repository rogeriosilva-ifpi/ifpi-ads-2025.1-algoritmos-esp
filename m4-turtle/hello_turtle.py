import turtle


def principal():
  bob = turtle.Turtle()
  configurar_turtle(bob)
  
  # desenhar um quadrado
  quadrado(bob)

  turtle.mainloop()


def configurar_turtle(bob: turtle.Turtle):
  # mudar os valores padrão: cor, shape, velocidade
  bob.shape('square')


def quadrado(bob: turtle.Turtle):
  bob.fd(200)
  bob.left(90)
  bob.fd(200)
  bob.left(90)
  bob.fd(200)
  bob.left(90)
  bob.fd(200)
  bob.left(90)
  

principal()