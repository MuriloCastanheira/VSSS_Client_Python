# VSSS_Client_Python
API para o FIRASim - VSSS

# Primeiro Passo:

Você deve abrir o arquivo "Communication.py" e alterar o endereço da quarta linha para o endereço de pasta protos que está no nesso computador.

# Exemplo de Código 1 - Get_Ball:

    from Communication import Communication # Aqui importamos a classe Communication

    info = Communication()  # Logo depois declaramos uma variável que serve para receber e enviar as informações recebidas

    ball = info.ball()  # em seguida declaramos uma variável para receber a posição da bola

    ball_x = ball.x
    ball_y = ball.y
    print(ball_x, ball_y)  # e printamos a posição recebida
  
  # Exemplo de Código 2 - Get_Robot:
    from Robot import Robot # Aqui importamos a classe Robot

    car = Robot(0, True) # Logo depois declaramos uma variável que serve para receber e enviar as informações recebidas, passanda o número do robo como paramento
                         # e se True para o time amarelo e False para o time azul

    car_x = car.x()
    car_y = car.y()
    car_ori = car.orient()

    print("x: ",car_x)
    print("z: ",car_y)
    print("ori: ",car_ori)
    
 # Exemplo de Código 3 - Move_Robot:

    from Communication import Communication # Aqui importamos a classe Communication

    info = Communication()  # Logo depois declaramos uma variavel que serve para receber e enviar as informações recebidas

    info.move(0, True, 10, 10)
