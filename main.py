import pygame
import random
import time

# Inicializace hry
pygame.init()

# Barvy
tyrkys = "#00fff8"
# Obrazovka
width = 1200
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Starwars")

# Nastavení hry
fps = 60
clock = pygame.time.Clock()


######################################################################x
# Classy

class Game:
    def __init__(self, our_player1, our_player2, group_of_stones):
        
        self.round_time = 0                             #Čas trvání aktuálního kola hry.
        self.slow_down_cycle = 0                        #Počítadlo cyklů pro zpomalení aktualizace času kola.        
        self.our_player_1 = our_player1             #Odkazy na objekty hráčů.
        self.our_player_2 = our_player2             #Odkazy na objekty hráčů.
        self.group_of_stones = group_of_stones          #Skupina meteoritů.  

        self.last_stone_time = 0                        #Poslední čas vytvoření meteoritu.
        self.stone_cooldown = 10                        #  self.stone_cooldown ŘÍKÁ ZA JAK DLOUHO SE VYGENERUJE DALŠÍ SÉRIE METEORITŮ (časové intervali mezi generování meteriotů)

            #Hudba v pozadí
        pygame.mixer.music.load("media/bg_starwars.mp3")
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.05)

            
            # Obrázek v pozadí
        self.background_image = pygame.image.load("img/bg_starwars3.webp")
        self.background_image = pygame.transform.scale(self.background_image, (1250, 400))
        self.background_image_rect = self.background_image.get_rect()
        self.background_image_rect.topleft = (0, 100)
        
        self.background_space_img = pygame.image.load("img/bg_space.jpg")
        self.background_space_img = pygame.transform.scale(self.background_space_img, (1200, 100))
        self.background_space_img_rect = self.background_space_img.get_rect()
        self.background_space_img_rect.topleft = (0,500)

            # Fonty
        self.stone_font = pygame.font.SysFont("ebrima", 15)
        self.custom_font_small=pygame.font.Font("fonts/DeathStar-VmWB.ttf",10)
        self.custom_font_medium=pygame.font.Font("fonts/DeathStar-VmWB.ttf",25)
        self.custom_font_large=pygame.font.Font("fonts/DeathStar-VmWB.ttf",40)
    
        #kód volán stále dokola je to zde pro získávámí času pro časomíru pod názvem hry kdž je hraspuštěna
        # a vemírné lodě po sobě mohou střílet
    def update(self):
        self.slow_down_cycle += 1
        if self.slow_down_cycle == fps:
            self.round_time += 1
            self.slow_down_cycle = 0
        #vykreslování ve hře 
    def draw(self):
        dark_yellow = pygame.Color("#938f0c")
        
            #Nastevení textu
        catch_text = self.custom_font_large.render("Star", True, dark_yellow)
        catch_text_rect = catch_text.get_rect()
        catch_text_rect.centerx = width // 2
        catch_text_rect.top = 5
        catch_text1 = self.custom_font_large.render("wars", True, dark_yellow)
        catch_text_rect1 = catch_text1.get_rect()
        catch_text_rect1.centerx = width // 2
        catch_text_rect1.top = 40

        player_text_2= self.custom_font_medium.render("PLAYER  2", True, dark_yellow)
        player_text_2_rect = player_text_2.get_rect()
        player_text_2_rect.topleft = (10, 4)

        player_text_1 = self.custom_font_medium.render("PLAYER  1", True, dark_yellow)
        player_text_1_rect = player_text_1.get_rect()
        player_text_1_rect.topright = (width - 5, 4)

        lives_text_2 = self.custom_font_medium.render(f"Zivoty: {self.our_player_2.lives}", True, dark_yellow)
        lives_text_rect_2 = lives_text_2.get_rect()
        lives_text_rect_2.topleft = (10, 30)

        lives_text_1 = self.custom_font_medium.render(f"Zivoty: {self.our_player_1.lives}", True, dark_yellow)
        lives_text_rect_1 = lives_text_1.get_rect()
        lives_text_rect_1.topright = (width - 5, 30)

            #POUZE sekundy
        #time_text = self.stone_font.render(f"Cas hry: {self.round_time}s", True, dark_yellow)
        #time_text_rect = time_text.get_rect()
        #time_text_rect.centerx = width//2
        #time_text_rect.top = 75

            #Sedkundy a minuty
        minutes = int(self.round_time // 60)
        seconds = int(self.round_time % 60)
        time_text1 = self.stone_font.render(f"Čas: {minutes} min {seconds} s", True, dark_yellow)
        time_text_rect1=time_text1.get_rect()
        time_text_rect1.center=(width // 2 , 85)
                                
            #Vykreslení (blitting) do obrazovky
        screen.blit(catch_text, catch_text_rect)
        screen.blit(catch_text1, catch_text_rect1)
        screen.blit(player_text_1, player_text_1_rect)
        screen.blit(player_text_2, player_text_2_rect)
        screen.blit(lives_text_1, lives_text_rect_1)
        screen.blit(lives_text_2, lives_text_rect_2)
        #screen.blit(time_text, time_text_rect)     # Pouze sekundy
        screen.blit(time_text1, time_text_rect1)
        
            #Tvary
            #Ohraničení + dělící čára
        pygame.draw.rect(screen, tyrkys, (0, 100, width, height - 200), 5)
        pygame.draw.line(screen, tyrkys, (width // 2, 105), (width // 2, 495), 5)
    
        #Generování nových kamenů
    def kameny(self):
            #current_time = pygame.time.get_ticks()
        #print(self.round_time)
        #print(self.last_stone_time)
        #print(self.stone_cooldown)
        #print(current_time)

        if self.round_time - self.last_stone_time >= self.stone_cooldown:                                                                
            for i in range(random.randint(1,3)):
                self.group_of_stones.add(RedStone(1300, random.randint(120, 470), pygame.image.load("img/red_stone.png"), 0))
                self.group_of_stones.add(WhiteStone(-100, random.randint(120, 470), pygame.image.load("img/white_stone.png"), 1))
                self.last_stone_time = self.round_time
                
            if self.stone_cooldown > 2:                                        # RYCHLOST PŘIDÁVÁNÍ METEORITŮ
                self.stone_cooldown -= 1                                 # kdyby zde nebyla podmínka tak bys potom neřízeně generovalo až moc rychle 
            else:
                pass                                                                     


    
        #Pozastavení hry na začátku a před novou hrou 
    def pause_game(self, main_text, subheading_text,subheading_text_2):

        global lets_continue            # Globální proměnná stejná v celém kódu


        #Nastavíme barvy 
        dark_yellow = "#938f0c"
        black=(0,0,0)

        # Hlavní text pro pauzu
        main_text_craete = self.custom_font_large.render(main_text, True, dark_yellow)
        main_text_craete_rect = main_text_craete.get_rect()
        main_text_craete_rect.center = (width//2, height//2 - 60)

        # Podnadpis pro puaznutí
        subheading_text_create = self.custom_font_medium.render(subheading_text,True, dark_yellow)
        subheading_text_create_rect = subheading_text_create.get_rect() 
        subheading_text_create_rect.center = (width//2, height//2 + 20)

        # Pro start
        subheading_text_2_create = self.custom_font_small.render(subheading_text_2,True, dark_yellow)
        subheading_text_2_create_rect = subheading_text_2_create.get_rect() 
        subheading_text_2_create_rect.center = (width//2, height//2 + 60)
        
        #Zobrazení hlavního textu a podnapisu
        screen.fill(black)
        screen.blit(main_text_craete,main_text_craete_rect)
        screen.blit(subheading_text_create,subheading_text_create_rect)
        screen.blit(subheading_text_2_create,subheading_text_2_create_rect)

        pygame.display.update()

        #Zastevení hry 
        
        paused = True
        while paused:
            for one_event in pygame.event.get():
                if one_event.type == pygame.KEYDOWN:
                    if one_event.key == pygame.K_RETURN:
                        paused = False
                
                if one_event.type == pygame.QUIT:
                        paused = False
                        lets_continue = False
   
class Player_1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/red_space.png")
        self.image = pygame.transform.rotate(self.image, 270)
        self.image = pygame.transform.scale(self.image, (65, 65))
        self.rect = self.image.get_rect()
        self.rect.centerx = width - 150
        self.rect.centery = height // 2
        self.lives = 5
        self.speed = 8
        self.bullets = pygame.sprite.Group()

        self.zap_sound = pygame.mixer.Sound("media/zap.wav")
        self.zap_sound.set_volume(0.02)
        self.demage_by_stone = pygame.mixer.Sound("media/lod_s_meteoritem.wav")
        self.demage_by_stone.set_volume(0.02)
        self.demage_by_bullet_sound = pygame.mixer.Sound("media/strela_s_lod.wav")
        self.demage_by_bullet_sound.set_volume(0.02)
        self.destroy_sound = pygame.mixer.Sound("media/strela_s_meteoritem.wav")
        self.destroy_sound.set_volume(0.02)

        self.last_shot_time = 0
        self.shot_cooldown = 50  # Cooldown time in milliseconds       #  self.shot_cooldown ŘÍKÁ JAKÝ JE ROZESTUP BULLETS + ZA JAK DLOUHO SE VYSTŘELÍ DALŠÍ SÉRIE KULEK
                                                                        #    len ŘÍKÁ KOLIK KULEK SE VYSTŘELÍ 
        #kód volán stále dokola                                                                
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 605:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < width - 10:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 108:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < height - 108:
            self.rect.y += self.speed
            #střelba
        if keys[pygame.K_SPACE]:
            self.fire_bullet()
            

        self.bullets.update()

        #Limit střel
    def fire_bullet(self):
        current_time = pygame.time.get_ticks()
        if len(self.bullets) < 3 and current_time - self.last_shot_time >= self.shot_cooldown:
            bullet = Bullet(self.rect.left, self.rect.centery, -10, shooter=1)          #10 ; shooter=1
            self.bullets.add(bullet)
            self.last_shot_time = current_time
            self.zap_sound.play()
        #Vykreslení střel
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.bullets.draw(surface)

class Player_2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/white_space.png")
        self.image = pygame.transform.rotate(self.image, 270)
        self.image = pygame.transform.scale(self.image, (65, 65))
        self.rect = self.image.get_rect()
        self.rect.centerx = 150
        self.rect.centery = height // 2
        self.lives = 5
        self.speed = 8
        self.bullets = pygame.sprite.Group()

        self.zap_sound = pygame.mixer.Sound("media/zap.wav")
        self.zap_sound.set_volume(0.02)
        self.demage_by_stone = pygame.mixer.Sound("media/lod_s_meteoritem.wav")
        self.demage_by_stone.set_volume(0.02)
        self.demage_by_bullet_sound = pygame.mixer.Sound("media/strela_s_lod.wav")
        self.demage_by_bullet_sound.set_volume(0.02)
        self.destroy_sound = pygame.mixer.Sound("media/strela_s_meteoritem.wav")
        self.destroy_sound.set_volume(0.02)

        self.last_shot_time = 0
        self.shot_cooldown = 50  # Cooldown time in milliseconds

        #kód volán stále dokola   
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > 10:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < width - 605:
            self.rect.x += self.speed
        if keys[pygame.K_w] and self.rect.top > 108:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < height - 108:
            self.rect.y += self.speed
        if keys[pygame.K_c]:
            self.fire_bullet()
            
            

        self.bullets.update()
            #Limit střel
    def fire_bullet(self):
        current_time = pygame.time.get_ticks()
        if len(self.bullets) < 3 and current_time - self.last_shot_time >= self.shot_cooldown:
            bullet = Bullet(self.rect.right, self.rect.centery, 10, shooter=2)      #-10, shooter=2
            self.bullets.add(bullet)
            self.last_shot_time = current_time
            self.zap_sound.play()
            #Vykreslení střel
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.bullets.draw(surface)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, shooter):
        super().__init__()
        self.image = pygame.Surface((15, 5))
        
            #barvy střel
        if shooter==1:
                self.image.fill((255, 165, 0))
        else:
                self.image.fill((0, 0, 255))

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = speed
        self.shooter = shooter
        
            #Putování střely
    def update(self):           
        self.rect.x += self.speed
        if self.rect.right < 0 or self.rect.left > width:
            self.kill()

class RedStone(pygame.sprite.Sprite):
    def __init__(self, x, y, image, stone_type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.type = stone_type
        self.speed = random.randint(1, 5)
            #putování stone
    def update(self):
        self.rect.x -= self.speed

class WhiteStone(pygame.sprite.Sprite):
    def __init__(self, x, y, image, stone_type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.type = stone_type
        self.speed = random.randint(1, 5)
            #putování stone
    def update(self):
        self.rect.x += self.speed





# Skupina meteority
stone_group = pygame.sprite.Group()

# Skupina hráčů
player_group = pygame.sprite.Group()
one_player_1 = Player_1()
player_group.add(one_player_1)
one_player_2 = Player_2()
player_group.add(one_player_2)

# Objekt Game
my_game = Game(one_player_1, one_player_2, stone_group)
lets_continue = True
my_game.kameny()
my_game.pause_game("STARWARS", "Stiskni enter pro zahajeni hry"," ")
clock = pygame.time.Clock()
start_time = time.time()



# Hlavní cyklus hry
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    screen.fill((0, 0, 0))          #překryje obrazovku černou barvou                         
    screen.blit(my_game.background_image, my_game.background_image_rect)           #vykreslí se požadované pozadí
    screen.blit(my_game.background_space_img,my_game.background_space_img_rect)    #vyreslí se požadované pozadí
#vykreslí se a aktualizují se skupiny meteoritů a hráčů a dalších prvků 
    stone_group.draw(screen)
    stone_group.update()
    player_group.draw(screen)
    player_group.update()
    my_game.update()
    my_game.draw()
#kontrola, zda je čas vytvořit nové meteority, a pokud ano, vytvoří je a přidá do skupiny meteoritů.
    my_game.kameny()
#Vykreslení hráčů
    one_player_1.draw(screen)
    one_player_2.draw(screen)

    #####################   kolize Player_2         ######################################xxx

    # Detect bullet collisions
    for bullet in one_player_1.bullets:
        if pygame.sprite.collide_rect(bullet, one_player_2):
            bullet.kill()                                   #KDYBY zde nebylo bullet.kill() tak se životy budou odečítat hrozně rychle
            one_player_2.lives -= 1
            one_player_2.demage_by_bullet_sound.play()
           
        # Collision detection with WhiteStone
        for white_stone in [stone for stone in stone_group if isinstance(stone, WhiteStone)]:
            if pygame.sprite.collide_rect(bullet, white_stone):
                bullet.kill()                                       #kdyby zde nebylo bullet.kill() tak nebudou mizet střely (šipky hráče) při střtu s meteoritem
                white_stone.kill()
                one_player_1.destroy_sound.play()
        # Collision detection with RedStone
        for red_stone in [stone for stone in stone_group if isinstance(stone, RedStone)]:
            if pygame.sprite.collide_rect(bullet, red_stone):
                bullet.kill()                                       #kdyby zde nebylo bullet.kill() tak nebudou mizet střely (šipky hráče) při střtu s meteoritem
                red_stone.kill()
                one_player_1.destroy_sound.play()

    # Collision detection with RedStone
    for red_stone in [stone for stone in stone_group if isinstance(stone, RedStone)]:
        if pygame.sprite.collide_rect(red_stone, one_player_2):
            red_stone.kill()                                        
            one_player_2.lives -= 1
            one_player_2.demage_by_stone.play()
    #####################   kolize Player_1     ###################################xx

    for bullet in one_player_2.bullets:
        if pygame.sprite.collide_rect(bullet, one_player_1):
            bullet.kill()                                   #KDYBY zde nebylo bullet.kill() tak se životy budou odečítat hrozně rychle
            one_player_1.lives -= 1
            one_player_1.demage_by_bullet_sound.play()

        # Collision detection with RedStone
        for red_stone in [stone for stone in stone_group if isinstance(stone, RedStone)]:
            if pygame.sprite.collide_rect(bullet, red_stone):
                bullet.kill()                                       #kdyby zde nebylo bullet.kill() tak nebudou mizet střely (w,s,a,d hráče) při střtu s meteoritem
                red_stone.kill()
                one_player_2.destroy_sound.play()

            # Collision detection with WhiteStone
        for white_stone in [stone for stone in stone_group if isinstance(stone, WhiteStone)]:
            if pygame.sprite.collide_rect(bullet, white_stone):
                bullet.kill()                                       #kdyby zde nebylo bullet.kill() tak nebudou mizet střely (w,s,a,d hráče) při střtu s meteoritem
                white_stone.kill()
                one_player_2.destroy_sound.play()
        
    # Collision detection with WhiteStone
    for white_stone in [stone for stone in stone_group if isinstance(stone, WhiteStone)]:
        if pygame.sprite.collide_rect(white_stone, one_player_1):
            white_stone.kill()
            one_player_1.lives -= 1
            one_player_1.demage_by_stone.play()

    # Check for game over
    if one_player_1.lives <= 0:
        my_game.pause_game("Game Over", "Player 2 wins", "Press Enter to Restart")
        one_player_1.lives = 5
        one_player_2.lives = 5

        my_game.last_stone_time = 0
        my_game.stone_cooldown = 10
            

        my_game.round_time = 0
        my_game.slow_down_cycle = 0
                #Vyprázdnění/smazání meteoritů a střel
        stone_group.empty()
        one_player_1.bullets.empty()
        one_player_2.bullets.empty()
            #Původní poloha
        one_player_1.rect.centerx = width - 150
        one_player_1.rect.centery = height // 2
        one_player_2.rect.centerx = 150
        one_player_2.rect.centery = height // 2
        my_game.kameny()
        pygame.mixer.music.play(-1, 0.0)

    if one_player_2.lives <= 0:
        my_game.pause_game("Game Over", "Player 1 wins", "Press Enter to Restart")
        one_player_1.lives = 5
        one_player_2.lives = 5

        my_game.last_stone_time = 0
        my_game.stone_cooldown = 10


        my_game.round_time = 0
        my_game.slow_down_cycle = 0
            #Vyprázdnění/smazání meteoritů a střel
        stone_group.empty()
        one_player_1.bullets.empty()
        one_player_2.bullets.empty()
            #Původní poloha
        one_player_1.rect.centerx = width - 150
        one_player_1.rect.centery = height // 2
        one_player_2.rect.centerx = 150
        one_player_2.rect.centery = height // 2
        my_game.kameny()
        pygame.mixer.music.play(-1, 0.0) 

    pygame.display.update()
    clock.tick(fps)

pygame.quit()






"""
# Hlavní cyklus hry
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    screen.fill((0, 0, 0))
    stone_group.draw(screen)
    stone_group.update()
    player_group.draw(screen)
    player_group.update()
    my_game.update()
    my_game.draw()

    my_game.kameny()

    one_player_1.draw(screen)
    one_player_2.draw(screen)

    # Detect bullet collisions
    for bullet in one_player_1.bullets:
        if pygame.sprite.collide_rect(bullet, one_player_2):
            bullet.kill()
            one_player_1.lives -= 1
    
    for bullet in one_player_2.bullets:
        if pygame.sprite.collide_rect(bullet, one_player_1):
            bullet.kill()
            one_player_2.lives -= 1

    pygame.display.update()
    clock.tick(fps)

pygame.quit()

"""