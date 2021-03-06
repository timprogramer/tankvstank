"""
Создается спрайт танк.
Каждую секнду он меняет свое положение на случайное.
Задача игрока - попасть по этому танку. Если попал - костюм танка меняется на следующий танк.

При нажатии клавиши Вверх за мышью начинает ходить маленький прицел (спрайт pacman, костюм player2, поворот 0гр).
Размер 50% от оригинального.
При повторном нажатии - прицел становится размером 100% от оригинального.
При повторном нажатии - прицел становится размером 150% от оригинального.
При повторном нажатии - прицел прицел исчезает.
При повторном нажатии опять появляется маленький прицел (50% от оригинального).

Если есть прицел, то попадание считается, если во время клика прицел касался танка.
Если нет прицела, то попаданием считается, если игрок кликнул точно по танку.
"""
import wrap,time,random

wrap.world.create_world(500,600,400,400)

tank=wrap.sprite.add("battle_city_tanks",250,300)

pacman=wrap.sprite.add("pacman",0,0,"player2",visible=False)

wrap.sprite.set_angle(pacman,0)

sollox=random.randint(50,450)
solloy=random.randint(50,550)
@wrap.always(1200)
def sollo():
    sollox = random.randint(50, 450)
    solloy = random.randint(50, 550)
    wrap.sprite.move_to(tank,sollox,solloy)

@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def change(pos_x,pos_y):
    if wrap.sprite.is_collide_point(tank,pos_x,pos_y) == True :
        wrap.sprite.set_costume_next(tank)
    elif wrap.sprite.is_collide_sprite(tank,pacman) == True:
        wrap.sprite.set_costume_next(tank)

@wrap.on_key_down(wrap.K_UP)
def pricel():
    prochentv1 = 0
    prochentw1 = 0
    prochentv=wrap.sprite.get_height_percent(pacman)
    prochentw = wrap.sprite.get_width_percent(pacman)
    if wrap.sprite.is_visible(pacman) == False:
        wrap.sprite.set_size_percent(pacman, 50, 50)
        wrap.sprite.show(pacman)
    elif prochentv == 50 and prochentw == 50:
        wrap.sprite.set_size_percent(pacman,100,100)
    elif prochentv ==100 and prochentw ==100:
        wrap.sprite.set_size_percent(pacman, 150, 150)
    elif prochentv ==150 and prochentw ==150:
        wrap.sprite.hide(pacman)


@wrap.on_mouse_move()
def slozno(pos_x,pos_y):
    wrap.sprite.move_to(pacman,pos_x,pos_y)



