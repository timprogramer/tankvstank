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

time_start=time.time()

while 1==1:
    time_end=time.time()
    raznica=time_end-time_start
    raznica=int(raznica)
    raznica=str(raznica)
    minus = time_end-time_start
    sollox=random.randint(50,450)
    solloy=random.randint(50,550)
    if minus>=1:
        tankskin = random.choice(["tank_enemy_size3_yellow1", "tank_player_size3_purple1","tank_enemy_size1_white2"])
        wrap.sprite.remove(tank)
        time.sleep(1)
        tank=wrap.sprite.add("battle_city_tanks",sollox,solloy)
        wrap.sprite.set_costume(tank,tankskin)
        time.sleep(1)




























































































































































































