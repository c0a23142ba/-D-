import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False) #練習7-1
    kk_img = pg.image.load("fig/3.png") #練習2
    kk_img = pg.transform.flip(kk_img,True,False) #練習3
    kk_rct = kk_img.get_rect()#練習8-1
    kk_rct.center = 300 , 200 #練習8-2
    tmr = 0
    x = 0
    y = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            key_lst =pg.key.get_pressed()
        x,y = 0,0
        if key_lst[pg.K_UP]:
            y -= 1
        if key_lst[pg.K_DOWN]:
            y += 1
        if key_lst[pg.K_LEFT]:
            x -=1
        if key_lst[pg.K_RIGHT]:
            x += 3
        if key_lst[pg.K_UP]  or key_lst[pg.K_DOWN] or key_lst[pg.K_LEFT] == False or key_lst[pg.K_RIGHT] == False:
            x -=1
        kk_rct.move_ip(x,y) 
            

        x = tmr%3200
    
        screen.blit(bg_img, [-x, 0])#練習6
        screen.blit(bg_img2,[-x+1600,0])#練習7-1
        screen.blit(bg_img, [-x+3200, 0])#練習7-2
        screen.blit(bg_img2,[-x+4800,0])#練習7-2
        screen.blit(kk_img,kk_rct) #練習4
        pg.display.update()
        tmr += 1        
        clock.tick(200)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()