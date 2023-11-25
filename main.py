import pygame as p
from os.path import join
from set import *

p.init()

s = p.display.set_mode((WI, HE))
p.display.set_caption(TLE)

run = True
# Флаг для отслеживания состояния кнопки
btn_cld = False
cl = p.time.Clock()


def gt_bg(name):
    image = p.image.load(join("assets", "Bg", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WI // width + 1):
        for j in range(HE // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image


def draw(s, bg, bg_im):
    for tile in bg:
        s.blit(bg_im, tile)
    p.display.update()


bg, bg_im = gt_bg("Blue.png")

# Основной игровой цикл
running = True
while running:
    for ev in p.event.get():
        if ev.type == p.QUIT:
            running = False
        elif ev.type == p.MOUSEBUTTONDOWN:
            ms_x, ms_y = p.mouse.get_pos()
            ms_psd = p.mouse.get_pressed()
            if btn_x <= ms_x <= btn_x + btn_wi and btn_y <= ms_y <= btn_y + btn_he:
                btn_cld = True
            else:
                btn_cld = False
        elif ev.type == p.MOUSEBUTTONUP:
            btn_cld = False

    # Отрисовка графики
    draw(s, bg, bg_im)
    # Отрисовка кнопки

    if btn_cld:
        p.draw.rect(s, RED, (btn_x, btn_y, btn_wi, btn_he))
    else:
        p.draw.rect(s, WHT, (btn_x, btn_y, btn_wi, btn_he))

    p.display.update()
    cl.tick(FPS)

p.quit()
