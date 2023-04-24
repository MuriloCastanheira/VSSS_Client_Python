from Communication import Communication # Aqui importamos a classe Communication

info = Communication()  # Logo depois declaramos uma variável que serve para receber e enviar as informações recebidas

ball = info.ball()  # em seguida declaramos uma variável para receber a posição da bola

ball_x = ball.x
ball_y = ball.y
print(ball_x, ball_y)  # e printamos a posição recebida