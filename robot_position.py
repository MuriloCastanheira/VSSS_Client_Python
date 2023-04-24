from Robot import Robot # Aqui importamos a classe Robot

car = Robot(0, True) # Logo depois declaramos uma variável que serve para receber e enviar as informações recebidas, passanda o número do robo como paramento
                     # e se True para o time amarelo e False para o time azul

car_x = car.x()
car_y = car.y()
car_ori = car.orient()

print("x: ",car_x)
print("z: ",car_y)
print("ori: ",car_ori)