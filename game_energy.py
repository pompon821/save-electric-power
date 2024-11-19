#This code was written by sauka
#And ancho helped me

#importing libraries
from pygame import *
from random import * 

#initializations
font.init()

#constants
save_energy,save_energy1, save_energy2, save_energy3,save_energy4,save_energy5,save_energy6,save_energy7 = 0, 0, 0, 0, 0, 0, 0, 0
width,height = 1000,589
fps = 60
timer_duration = 19
a,b,c,d,sas,g,l,v = 0,0,0,0,0,0,0,0


#images
p_img = 'player_games1.png'
img_bg1 = 'background_game.png'
img_light_bulb_off = 'light_off.png'
img_light_bulb_on = 'light_on.png'
img_switch = 'switch.png'
img_electric_stove_on = 'electric_stove_on1.png'
img_electric_stove_off = 'electric_stove_off1.png'
img_nuke_off = 'nuke_off.png'
img_nuke_on = 'nuke_on.png'
img_game_over = '2bg_game.png'
img_toaster_on = 'toaster1_on.png'
img_toaster_off = 'toaster1_off.png'
img_2background = '2background.png'
img_doors = 'door.png'
img_monitor_on = 'monitor_on.png'
img_monitor_off = 'monitor_off.png'
img_fan_on = 'fan_on.png'
img_fan_off = 'fan_off.png'
img_for_bg = 'for_bg_processed.png'
img_light2_off = 'light2_off.png'
img_light2_on = 'light2_on.png'

#blank for the text
font1 = font.SysFont('Arial', 20)
font2 = font.SysFont('Arial', 60)
font3 = font.SysFont('Arial', 80)
timer_font = font.SysFont('Arial', 30)

#creating an application
window = display.set_mode((width, height))
background = transform.scale(image.load(img_bg1), (width, height))
background2 = transform.scale(image.load(img_2background), (width, height))
backgrounds = transform.scale(image.load(img_game_over), (width, height))
display.set_caption('energy')
clock = time.Clock()


#the main class for creating others
class GameSprite(sprite.Sprite):
    def __init__(self, p_img: str, x: int, y: int, w: int, h: int, speed: int):
        super().__init__()
        self.image = transform.scale(image.load(p_img), (w, h))
        self.rect = self.image.get_rect() 
        self.rect.x = x 
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x , self.rect.y))


#a class for a character
class Player(GameSprite):
    def update(self):

        keys = key.get_pressed()

        if keys[K_w] and self.rect.y >= 5 and waiting == True:
            self.rect.y -= self.speed

        elif keys[K_s] and self.rect.y <= 435 and waiting == True:
            self.rect.y += self.speed

        if keys[K_a] and self.rect.x >= 5 and waiting == True:
            self.rect.x -= self.speed

        elif keys[K_d] and self.rect.x <= 920 and waiting == True:
            self.rect.x += self.speed


#a class for objects
class Objects(GameSprite):
    pass


#instances of classes
light_bulb = Objects(img_light_bulb_on, 560, 5, 40, 90, 0)
switch = Objects(img_switch, 900, 301, 50, 50, 0)
electric_stove = Objects(img_electric_stove_on, 130, 226, 168, 215, 0)
nuke = Objects(img_nuke_on, 645, 241, 106, 48, 0)
toaster = Objects(img_toaster_on, 368, 210, 80, 80, 0)
doors = Objects(img_doors, 990, 500, 10, 89, 0)
monitor = Objects(img_monitor_on, 920555, 200, 156, 130, 0)
fan = Objects(img_fan_on, 6446, 150, 70, 120, 0)
armchair = Objects(img_for_bg, 4666, 150, 195, 320, 0)
lamp = Objects(img_light2_on, 8698, 120, 80, 120, 0)
player = Player(p_img, 500, 400, 80, 150, 6)


#texts
text_press_Q = font1.render('press Q', 1, (0,0,0))
text_press_E = font1.render('press E', 1, (0,0,0))
text_start1 = font1.render('you have 15 seconds to save as much energy as possible,', 1,(0, 0, 0))
text_energy_spent = timer_font.render('You failed! You have saved 0 of your energy', 1, (255, 0, 0))
text_game_over = font3.render('GAME OVER', 1, (0, 0, 0))
TEXT_AUTHOR = font1.render('by sauka', 1, (0, 0, 0))


run = True
waiting = False
finish = False

start_time = time.get_ticks() 

#The main cycle
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:      

        #text
        text_save_energy = timer_font.render('You are doing well! You have saved ' + str(save_energy) + ' of your energy', 1, (0, 255, 0))

        remaining_time = timer_duration - (time.get_ticks() - start_time) // 1000
        timer_text = timer_font.render(str(remaining_time), 1, (0, 0, 0))


        #setting the background
        window.blit(background, (0,0))

        #character movements
        player.update()

        #drawing objects
        electric_stove.reset()
        nuke.reset()
        toaster.reset()
        switch.reset()
        doors.reset()    
        fan.reset()
        armchair.reset()
        lamp.reset()
        monitor.reset()    
        player.reset()
        light_bulb.reset()

        if remaining_time <= 15:
            window.blit(timer_text, (5, 5))  


        #conditions for displaying text
        if waiting == False:
            window.blit(text_start1, (230, 8))

        #drawing the second room
        if sprite.collide_rect(player, doors) and sas == 0:
            player.rect.x = 200

            light_bulb = Objects(img_light_bulb_on, 5611, 5, 40, 90, 0)
            switch = Objects(img_switch, 9111, 248, 50, 50, 0)
            electric_stove = Objects(img_electric_stove_on, 130111, 173, 168, 215, 0)
            nuke = Objects(img_nuke_on, 6111, 188, 106, 48, 0)
            toaster = Objects(img_toaster_on, 11111, 158, 80, 80, 0)
            armchair = Objects(img_for_bg, 800, 170, 195, 320, 0)

            if g == 1:
                monitor = Objects(img_monitor_off, 736, 124, 156, 130, 0)

            elif g == 0:
                monitor = Objects(img_monitor_on, 736, 124, 156, 130, 0)

            if l == 1:
                fan = Objects(img_fan_off, 620, 135, 80, 120, 0)

            elif l == 0:
                fan = Objects(img_fan_on, 620, 135, 80, 120, 0)
            
            if v == 1:
                lamp = Objects(img_light2_off, 450, 200, 130, 220, 0)

            elif v == 0:
                lamp = Objects(img_light2_on, 450, 200, 130, 220, 0)

            background = transform.scale(image.load(img_2background), (width, height))
            window.blit(background2, (0, 0))
            doors = Objects(img_doors, 0, 500, 10, 89, 0)

            sas += 1


        #checking for sprite collisions
        elif sprite.collide_rect(player, doors) and sas == 1:
            player.rect.x = 800

            if a == 1:
                light_bulb = Objects(img_light_bulb_off, 560, 5, 40, 90, 0)

            elif a == 0:
                light_bulb = Objects(img_light_bulb_on, 560, 5, 40, 90, 0)

            if b == 1:
                electric_stove = Objects(img_electric_stove_off, 130, 226, 168, 215, 0)

            elif b == 0:
                electric_stove = Objects(img_electric_stove_on, 130, 226, 168, 215, 0)
            
            if c == 1:
                nuke = Objects(img_nuke_off, 645, 241, 106, 48, 0)

            elif c == 0:
                nuke = Objects(img_nuke_on, 645, 241, 106, 48, 0)
            
            if d == 1:
                toaster = Objects(img_toaster_off, 368, 210, 80, 80, 0)

            elif d == 0:
                toaster = Objects(img_toaster_on, 368, 210, 80, 80, 0)

            switch = Objects(img_switch, 900, 301, 50, 50, 0)
            doors = Objects(img_doors, 990, 500, 10, 89, 0)
            monitor = Objects(img_monitor_on, 926660, 200, 156, 130, 0)
            fan = Objects(img_fan_on, 6565, 150, 70, 120, 0)
            armchair = Objects(img_for_bg, 4669, 150, 195, 320, 0)
            lamp = Objects(img_light2_on, 86868, 120, 80, 120, 0)

            background = transform.scale(image.load(img_bg1), (width, height))
            window.blit(background2, (0, 0))
            doors = Objects(img_doors, 990, 500, 10, 89, 0)

            sas -= 1


        #checking for sprite collisions
        if sprite.collide_rect(player, lamp) and v == 0:
            window.blit(text_press_E, (510, 120))
            if e.type == KEYDOWN:
                if e.key == K_e:
                    lamp = Objects(img_light2_off, 450, 200, 130, 220, 0)
                    v += 1
                    save_energy7 += randint(20, 30)

        
        #checking for sprite collisions
        elif sprite.collide_rect(player, lamp) and v == 1:
            window.blit(text_press_Q, (510, 120))
            if e.type == KEYDOWN:
                if e.key == K_q:
                    lamp = Objects(img_light2_on, 450, 200, 130, 220, 0)
                    v -= 1
                    save_energy7 -= save_energy7


        #checking for sprite collisions
        if sprite.collide_rect(player, fan) and  l == 0:
            window.blit(text_press_E, (646, 100))       
            if e.type == KEYDOWN:
                if e.key == K_e:
                    fan = Objects(img_fan_off, 620, 135, 80, 120, 0)
                    l += 1
                    save_energy6 += randint(20, 35)


        #checking for sprite collisions
        elif sprite.collide_rect(player, fan) and  l == 1:
            window.blit(text_press_Q, (646, 100))       
            if e.type == KEYDOWN:
                if e.key == K_q:
                    fan = Objects(img_fan_on, 620, 135, 80, 120, 0)
                    l -= 1
                    save_energy6 -= save_energy6


        #checking for sprite collisions
        if sprite.collide_rect(player, monitor) and g == 0:
            window.blit(text_press_E, (775, 48))
            if e.type == KEYDOWN:
                if e.key == K_e:
                    monitor = Objects(img_monitor_off, 736, 124, 156, 130, 0)
                    g += 1
                    save_energy5 += randint(30, 50)


        #checking for sprite collisions
        elif sprite.collide_rect(player, monitor) and g == 1:
            window.blit(text_press_Q, (775, 48))
            if e.type == KEYDOWN:
                if e.key == K_q:
                    monitor = Objects(img_monitor_on, 736, 124, 156, 130, 0)
                    g -= 1
                    save_energy5 -= save_energy5

            
        #checking for sprite collisions
        if sprite.collide_rect(player, switch) and a == 0:
            window.blit(text_press_E, (905, 218))
            if e.type == KEYDOWN:
                if e.key == K_e:
                    light_bulb = Objects(img_light_bulb_off, 560, 5, 40, 90, 0)
                    a += 1
                    save_energy1 += randint(10, 20)
        

        #checking for sprite collisions
        elif sprite.collide_rect(player, switch) and a == 1:
            window.blit(text_press_Q, (905, 218))
            if e.type == KEYDOWN:
                if e.key == K_q:
                    light_bulb = Objects(img_light_bulb_on, 560, 5, 40, 90, 0)
                    a -= 1
                    save_energy1 -= save_energy1


        #checking for sprite collisions
        if sprite.collide_rect(player, electric_stove) and b == 0:
            window.blit(text_press_E, (170, 168))
            if e.type == KEYDOWN:
                if e.key == K_e:
                    electric_stove = Objects(img_electric_stove_off, 130, 226, 168, 215, 0)
                    b += 1
                    save_energy2 += randint(25, 40)


        #checking for sprite collisions
        elif sprite.collide_rect(player, electric_stove) and b == 1:
            window.blit(text_press_Q, (170, 168))
            if e.type == KEYDOWN:
                if e.key == K_q:
                    electric_stove = Objects(img_electric_stove_on, 130, 226, 168, 215, 0)
                    b -= 1
                    save_energy2 -= save_energy2

        #checking for sprite collisions
        if sprite.collide_rect(player, nuke) and c == 0:
            window.blit(text_press_E, (655, 160))
            if e.type == KEYDOWN:
                if e.key == K_e:
                    nuke = nuke = Objects(img_nuke_off, 645, 241, 106, 48, 0)
                    c += 1
                    save_energy3 += randint(15, 25)


        #checking for sprite collisions
        elif sprite.collide_rect(player, nuke) and c == 1:
            window.blit(text_press_Q, (655, 160))
            if e.type == KEYDOWN:
                if e.key == K_q:
                    nuke = nuke = Objects(img_nuke_on, 645, 241, 106, 48, 0)
                    c -= 1
                    save_energy3 -= save_energy3


        #checking for sprite collisions
        if sprite.collide_rect(player, toaster) and d == 0:
            window.blit(text_press_E, (378, 128))
            if e.type == KEYDOWN:
                if e.key == K_e:
                    toaster = Objects(img_toaster_off, 368, 210, 80, 80, 0)
                    d += 1
                    save_energy4 += randint(15, 25)


        #checking for sprite collisions
        elif sprite.collide_rect(player, toaster) and d == 1:
            window.blit(text_press_Q, (378, 128))
            if e.type == KEYDOWN:
                if e.key == K_q:
                    toaster = Objects(img_toaster_on, 368, 210, 80, 80, 0)
                    d -= 1
                    save_energy4 -= save_energy4

        
        #timer
        if remaining_time == 0:

                finish = True
                window.blit(backgrounds, (0, 0))

                window.blit(text_game_over, (270, 50))

                if save_energy <= 0:
                    window.blit(text_energy_spent, (225, 158))

                elif save_energy > 0:
                    window.blit(text_save_energy, (150, 158))     

                window.blit(TEXT_AUTHOR, (450, 308))  

        elif remaining_time == 15 and waiting == False:
            waiting = True        

            
        save_energy = save_energy1 + save_energy2 + save_energy3 + save_energy4 + save_energy5 + save_energy6 + save_energy7

    display.update()
    clock.tick(fps)