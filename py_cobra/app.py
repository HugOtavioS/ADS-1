import pygame
import time
import random

pygame.init()

# Definindo as cores
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
blue = (50, 153, 213)
fast_food_color = (255, 165, 0)  # Laranja para comida que acelera
slow_food_color = (147, 112, 219)  # Roxo para comida que desacelera
background_color = (40, 44, 52)
grid_color = (60, 64, 72)  # Cor da grade

# Configurações do jogo
dis_width = 600
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game - Velocidade: Normal')

clock = pygame.time.Clock()
snake_block = 20  
base_snake_speed = 5  # Velocidade base aumentada
snake_speed = base_snake_speed

font_style = pygame.font.SysFont('arial', 35)
score_font = pygame.font.SysFont('arial', 25)

# Variáveis para controle dos efeitos temporários
effect_duration = 5000  # 5 segundos em milissegundos
effect_start_time = 0
current_effect = None

def our_snake(snake_block, snake_list):
    for i, x in enumerate(snake_list):
        if i == len(snake_list) - 1:  # Cabeça da cobra
            pygame.draw.rect(dis, (50, 205, 50), [x[0], x[1], snake_block, snake_block])
            pygame.draw.rect(dis, (34, 139, 34), [x[0], x[1], snake_block, snake_block], 1)
        else:  # Corpo da cobra
            pygame.draw.rect(dis, (34, 139, 34), [x[0], x[1], snake_block, snake_block])
            pygame.draw.rect(dis, (0, 100, 0), [x[0], x[1], snake_block, snake_block], 1)

def draw_grid():
    for i in range(0, dis_width, snake_block):
        pygame.draw.line(dis, grid_color, (i, 0), (i, dis_height))
    for i in range(0, dis_height, snake_block):
        pygame.draw.line(dis, grid_color, (0, i), (dis_width, i))

def Your_score(score, speed):
    score_text = score_font.render(f"Pontuação: {score}", True, white)
    speed_text = score_font.render(f"Velocidade: {speed}", True, white)
    effect_text = None
    
    if current_effect == 'fast':
        effect_text = score_font.render("ACELERADO!", True, fast_food_color)
    elif current_effect == 'slow':
        effect_text = score_font.render("DESACELERADO!", True, slow_food_color)
    
    dis.blit(score_text, [10, 10])
    dis.blit(speed_text, [10, 40])
    if effect_text:
        dis.blit(effect_text, [10, 70])

def Die_score(score, speed):
    score_text = score_font.render(f"Pontuação: {score}", True, black)
    speed_text = score_font.render(f"Velocidade: {speed}", True, black)
    effect_text = None
    
    if current_effect == 'fast':
        effect_text = score_font.render("ACELERADO!", True, fast_food_color)
    elif current_effect == 'slow':
        effect_text = score_font.render("DESACELERADO!", True, slow_food_color)
    
    dis.blit(score_text, [(dis_width / 2) - 70, (dis_height / 2)])
    dis.blit(speed_text, [(dis_width / 2) - 70, (dis_height / 2) - 30])
    if effect_text:
        dis.blit(effect_text, [10, 70])

def check_effect_duration():
    global snake_speed, current_effect
    if current_effect and pygame.time.get_ticks() - effect_start_time >= effect_duration:
        snake_speed = base_snake_speed
        current_effect = None
        pygame.display.set_caption('Snake Game - Velocidade: Normal')

def apply_food_effect(food_type):
    global snake_speed, effect_start_time, current_effect
    
    effect_start_time = pygame.time.get_ticks()
    current_effect = food_type
    
    if food_type == 'fast':
        snake_speed = base_snake_speed + 5
        pygame.display.set_caption('Snake Game - Velocidade: RÁPIDA!')
    elif food_type == 'slow':
        snake_speed = base_snake_speed - 3
        pygame.display.set_caption('Snake Game - Velocidade: LENTA!')

def gameLoop():
    game_over = False
    game_close = False

    # Inicialização da posição da cobra no centro da tela
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Inicialização das mudanças de posição da cobra em relação a posição inicial
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1
    
    # Inicialização da posição da comida aleatória
    foodx = round(random.randrange(0, dis_width - snake_block, snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, dis_height - snake_block, snake_block) / snake_block) * snake_block
    food_type = random.choice(['normal', 'fast', 'slow'])

    while not game_over:

        while game_close == True:
            image = pygame.image.load('py_cobra/images/SnakeDie.png')
            dis.blit(image, (0, 0))
            Die_score(length_of_snake - 1, snake_speed)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Verifica se a cobra colidiu com as bordas da tela
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Será desconsiderado até que o usuário pressione uma tecla
        for event in pygame.event.get(): # Aqui é o "trigger"
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:

                # Verifica se a cobra não está indo na direção oposta
                # Se o tamanho da cobra for maior do que um e a direção atual for oposta a direção que o usuário deseja ir
                # O loop é interrompido e pulado para a próxima iteração
                if len(snake_list) > 1:
                    if (event.key == pygame.K_LEFT and pygameKey == pygame.K_RIGHT) or (event.key == pygame.K_RIGHT and pygameKey == pygame.K_LEFT) or(event.key == pygame.K_UP and pygameKey == pygame.K_DOWN) or (event.key == pygame.K_DOWN and pygameKey == pygame.K_UP):
                        continue
                pygameKey = event.key
                if pygameKey == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif pygameKey == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif pygameKey == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif pygameKey == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        x1 += x1_change # Atualiza a posição da cobra
        y1 += y1_change # Atualiza a posição da cobra

        dis.fill(background_color)
        draw_grid()

        # Desenha a comida com efeito de brilho
        food_radius = snake_block // 2
        food_center = (foodx + food_radius, foody + food_radius)
        
        if food_type == 'normal':
            pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        elif food_type == 'fast':
            pygame.draw.rect(dis, fast_food_color, [foodx, foody, snake_block, snake_block])
        elif food_type == 'slow':
            pygame.draw.rect(dis, slow_food_color, [foodx, foody, snake_block, snake_block])

        check_effect_duration()

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        Your_score(length_of_snake - 1, snake_speed)

        if x1 == foodx and y1 == foody:
            if food_type in ['fast', 'slow']:
                apply_food_effect(food_type)

            foodx = round(random.randrange(0, dis_width - snake_block, snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, dis_height - snake_block, snake_block) / snake_block) * snake_block
            food_type = random.choice(['normal', 'fast', 'slow'])
            length_of_snake += 1

        pygame.display.update()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()