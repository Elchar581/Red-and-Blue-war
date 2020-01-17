import pygame


def collide(walls, x_user, y_uzer):  # проверка на столкновения
    runtime = False
    total_runtime = 0
    for wall in walls:
        if wall[1] >= y_uzer >= wall[1] + wall[3]:
            if wall[0] <= x_user <= wall[0] + wall[2]:
                total_runtime += 1
            elif wall[0] <= x_user + width <= wall[0] + wall[2]:
                total_runtime += 1
            elif x_user < wall[0] and x_user + width > wall[0] + wall[2]:
                total_runtime += 1
        elif wall[1] <= y_uzer + height <= wall[1] + wall[3]:
            if wall[0] <= x_user + 5 <= wall[0] + wall[2]:
                total_runtime += 1
            elif wall[0] <= x_user + width <= wall[0] + wall[2]:
                total_runtime += 1
            elif x_user < wall[0] and x_user + width > wall[0] + wall[2]:
                total_runtime += 1
        elif wall[1] > y_uzer and wall[1] + wall[3] < y_uzer + height:
            if wall[0] <= x_user + 5 <= wall[0] + wall[2]:
                total_runtime += 1
            elif wall[0] <= x_user + width <= wall[0] + wall[2]:
                total_runtime += 1
            elif x_user < wall[0] and x_user + width > wall[0] + wall[2]:
                total_runtime += 1
    if total_runtime > 0:
        runtime = True
    return runtime


def belle_person_blue(x_use, y_use):  # стрельба синего персонажа
    speed_bullet = 20
    x_bullet = x_use + 30
    y_bullet = y_use
    width_bullet = 8
    height_bullet = 4
    win_blue = False
    for i in range(15):
        x_bullet += speed_bullet
        if collide(arr_texture_xy, x_bullet, y_bullet):
            break
        if y2 <= y_bullet <= y2 + width:
            if x2 <= x_bullet <= x2 + width:
                win_blue = True
            elif x2 <= x_bullet + width_bullet <= x2 + width:
                win_blue = True
        else:
            pygame.draw.rect(win, (0, 0, 188), (x_bullet, y_bullet, height_bullet, width_bullet))
            pygame.display.update()
    if win_blue:
        return True
    else:
        return False


def belle_person_red(x_use, y_use):
    speed_bullet = 20
    x_bullet = x_use + 30
    y_bullet = y_use
    width_bullet = 8
    height_bullet = 4
    win_red = False
    for i in range(15):
        x_bullet -= speed_bullet
        if collide(arr_texture_xy, x_bullet, y_bullet):
            break
        if y <= y_bullet <= y + width:
            if x <= x_bullet <= x + width:
                win_red = True
            elif x <= x_bullet + width_bullet <= x + width:
                win_red = True
        else:
            pygame.draw.rect(win, (188, 0, 0), (x_bullet, y_bullet, height_bullet, width_bullet))
            pygame.display.update()
    if win_red:
        return True
    else:
        return False


pygame.init()
win = pygame.display.set_mode((1200, 700))

pygame.display.set_caption('RB cube war')

score_blue = 0
score_red = 0

spawn_x = 50
spawn_y = 350

spawn_x2 = 1120
spawn_y2 = 350

x = 50
y = 350

x2 = 1120
y2 = 350

gun_use_b = False
width = 30
height = 30
speed = 5

font = pygame.font.Font(None, 50)

arr_texture_xy = []

arr_texture_xy.append([600, 100, 1200, 30])
arr_texture_xy.append([1200, 100, 5, 700])
arr_texture_xy.append([1000, 251, 0, 325])
arr_texture_xy.append([905, 95, 0, 230])
arr_texture_xy.append([755, 505, 245, 5])
arr_texture_xy.append([655, 100, 0, 275])
arr_texture_xy.append([655, 455, 0, 120])
arr_texture_xy.append([655, 655, 0, 70])
arr_texture_xy.append([650, 300, 250, 10])

arr_texture_xy.append([0, 100, 600, 30])
arr_texture_xy.append([0, 700, 600, 5])
arr_texture_xy.append([0, 100, 5, 700])
arr_texture_xy.append([205, 251, 0, 325])
arr_texture_xy.append([305, 95, 0, 230])
arr_texture_xy.append([205, 505, 245, 5])
arr_texture_xy.append([550, 100, 0, 275])
arr_texture_xy.append([550, 455, 0, 120])
arr_texture_xy.append([550, 655, 0, 70])
arr_texture_xy.append([305, 300, 245, 10])

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= speed
        if collide(arr_texture_xy, x, y):
            x += speed
    if keys[pygame.K_d] and x + width <= 590:
        x += speed
        if collide(arr_texture_xy, x, y):
            x -= speed
    if keys[pygame.K_w]:
        y -= speed
        if collide(arr_texture_xy, x, y):
            y += speed
    if keys[pygame.K_s]:
        y += speed
        if collide(arr_texture_xy, x, y):
            y -= speed
    if keys[pygame.K_LEFT] and x2 >= 610:
        x2 -= speed
        if collide(arr_texture_xy, x2, y2):
            x2 += speed
    if keys[pygame.K_RIGHT]:
        x2 += speed
        if collide(arr_texture_xy, x2, y2):
            x2 -= speed
    if keys[pygame.K_UP]:
        y2 -= speed
        if collide(arr_texture_xy, x2, y2):
            y2 += speed
    if keys[pygame.K_DOWN]:
        y2 += speed
        if collide(arr_texture_xy, x2, y2):
            y2 -= speed
    if keys[pygame.K_SPACE]:
        bw = belle_person_blue(x, y)
        if bw:
            score_blue += 1
            x2 = spawn_x2
            y2 = spawn_y2

    if keys[pygame.K_RCTRL]:
        rw = belle_person_red(x2, y2)
        if rw:
            score_red += 1
            x = spawn_x
            y = spawn_y

    text_sb = font.render(str(score_blue), 1, (0, 0, 255))  # счёт персонажей
    text_sr = font.render(str(score_red), 1, (255, 0, 0))
    text_wb = font.render('Win', 1, (0, 0, 255))
    text_wr = font.render('Win', 1, (255, 0, 0))

    win.fill((200, 200, 200))

    win.blit(text_sb, (500, 25))
    win.blit(text_sr, (700, 25))

    pygame.draw.rect(win, (0, 0, 255), (0, 100, 600, 5))  # прорисовка карты от сюда

    pygame.draw.rect(win, (255, 0, 0), (600, 100, 1200, 5))
    pygame.draw.rect(win, (255, 0, 0), (1195, 100, 5, 700))
    pygame.draw.rect(win, (255, 0, 0), (995, 250, 5, 300))
    pygame.draw.rect(win, (255, 0, 0), (900, 100, 5, 200))
    pygame.draw.rect(win, (255, 0, 0), (750, 500, 250, 5))
    pygame.draw.rect(win, (255, 0, 0), (650, 100, 5, 250))
    pygame.draw.rect(win, (255, 0, 0), (650, 450, 5, 100))
    pygame.draw.rect(win, (255, 0, 0), (650, 650, 5, 50))
    pygame.draw.rect(win, (155, 155, 155), (655, 105, 245, 195))
    pygame.draw.rect(win, (255, 0, 0), (650, 295, 250, 5))
    pygame.draw.rect(win, (255, 0, 0), (600, 695, 600, 5))

    pygame.draw.rect(win, (155, 155, 155), (595, 105, 10, 590))

    pygame.draw.rect(win, (0, 0, 255), (0, 695, 600, 5))
    pygame.draw.rect(win, (0, 0, 255), (0, 100, 5, 700))
    pygame.draw.rect(win, (0, 0, 255), (200, 250, 5, 300))
    pygame.draw.rect(win, (155, 155, 155), (300, 105, 245, 195))
    pygame.draw.rect(win, (0, 0, 255), (300, 100, 5, 200))
    pygame.draw.rect(win, (0, 0, 255), (200, 500, 250, 5))
    pygame.draw.rect(win, (0, 0, 255), (545, 100, 5, 250))
    pygame.draw.rect(win, (0, 0, 255), (545, 450, 5, 100))
    pygame.draw.rect(win, (0, 0, 255), (300, 295, 250, 5))
    pygame.draw.rect(win, (0, 0, 255), (550, 650, 5, 50))  # прорисовка карты до сюда

    pygame.draw.rect(win, (0, 0, 0), (x, y, width, height))  # прорисовка синего персонажа
    pygame.draw.rect(win, (255, 255, 255), (x + 8, y + 8, width - 16, height - 16))
    pygame.draw.rect(win, (0, 0, 255), (x + 10, y + 10, width - 20, height - 20))

    pygame.draw.rect(win, (0, 0, 0), (x2, y2, width, height))  # прорисовка красного персонажа
    pygame.draw.rect(win, (255, 255, 255), (x2 + 8, y2 + 8, width - 16, height - 16))
    pygame.draw.rect(win, (255, 0, 0), (x2 + 10, y2 + 10, width - 20, height - 20))

    if score_red == 16:
        win.blit(text_wr, (800, 200))
        run = False
    if score_blue == 16:
        win.blit(text_wb, (400, 200))
        run = False

    pygame.display.update()

pygame.quit()
