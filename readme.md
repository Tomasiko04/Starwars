**Starwars**

>**STRUKTURA README souboru**
1. Popis hry

2. Co potřebujete aby jste kód spustili

3. Ovládání hry

4. Popis kódu

4.1 Základní nastavení hry

4.2 Logika

4.2.1 Classy

4.2.1.1 Game

4.2.1.2 Player_1 (Player_2)

4.2.1.3 Bullet

4.2.1.4 RedStone (WhiteStone)

4.3 Použití logiky

4.3.1 Před hlavní herní smyčkou

4.3.2 Hlavní cyklus

5. ZÁVĚR


>**1. Popis hry**

Tato hra je inspirována sci-fi filmy Star Wars. Jedná se o soubojovou arkádovou hru pro dva hráče, ve které se snažíte zničit nepřátelskou vesmírnou loď a přežít co nejdéle. Každý z hráčů má 5 životů, o které může snadno přijít - buď zásahem střelou, kterou proti němu vyšle protivník, nebo pokud se střetne s nepřátelským meteoroidem. Naopak každá z vesmírných lodí je imunní vůči svým meteoroidům, za které se může schovat při útoku nepřítele.

(player_1 => červená vesmírná loď > imunní proti červeným meteoroidům

player_2 => bílá vesmírná loď > imunní proti bílým meteoroidům)

>**2. Co potřebujete aby jste kód spustili**

>>Stáhnou si veškeré dokumenty k tomuto kódu (main.py, fonts, img, media)
>>Pokud používáte pro spuštění kódu Visual Studio Code musíte si nainstalovat knihovnu pygame
Jak na to? 
Když otevřete vaše Visual Studio Code a otevřete si soubor main.py, který si stáhnete klikněte na Terminal > New Terminal > dole se vám otevře okno > napište do něj *pip install pygame* a stikněte klávesu ENETR > po chvíli se vám stáhne tato knihovna (pygame)


>**3. Ovládání hry:**

Hráč 1:

    Pohyb: Šipky (nahoru, dolů, vlevo, vpravo)

    Střelba: Mezerník (podle délky stisku klávesy se vystřelí určitý počet střel min.1 max.3)


Hráč 2:

    Pohyb: W, S, A, D

    Střelba: Klávesa "C" (podle délky stisku klávesy se vystřelí určitý počet střel min.1 max.3)

>**4. Popis kódu** 

>>**4.1 Základní nastavení hry**

V této části, která bude značně nejdelší se Vám pokusím co nejlépe popsat a vysvětlit co daný kód umí.

Na začátku celého kódu musíme importovat několik knihoven (pygame, random, time)

    (řádky v kódu 1-3)
        import pygame
        import random
        import time


Poté je potřeba inicializovat celou hru pomocí
        
    (řádek v kódu 6)
        pygame.init() 
        
určit si barvy a velikost rozlišení obrazovky

    (řádky v kódu 8-12)
        # Barvy
        tyrkys = "#00fff8"
        # Obrazovka
        width = 1200
        height = 600


a pomocí

    (řádek v kódu 13)
        screen = pygame.display.set_mode((width, height))
        
si určit velikost rozlišení obrazovky


a pomocí 

    (řádek v kódu 14)
        pygame.display.set_caption("Starwars")

určit název herního okna


Nastavení hry

    (řádky v kódu 17 a 18 )       
        fps = 60
        clock = pygame.time.Clock()

fps=počet snímků za sekundu
pygame.time.Clock() je konstruktor třídy Clock v knihovně Pygame, který vytváří nový objekt Clock je používán k regulaci rychlosti herní smyčky.


>>**4.2 Logika**

>>**4.2.1 Classy (třídy)**

Classa neboli třída je laicky řečeno jakýsi druh datové struktury, která nám organizuje kód do určitých logických celků. Tyto třídy mohou například reprezentovat herní postavy, překážky, efekty atd. Každá třída může mít atributy (proměnné) a metody (funkce), které definují chování a vlastnosti této třídy.
V této hře máme 6 tříd (Game, Plaeyr_1, Player_2, Bullet, WhiteStone, RedStone)

>>**Popis class a jejich atributů a metod**

>>> **4.2.1.1 Game** -> představuje hlavní herní logiku a funkce pro hru "Starwars" 

**1. Inicializujeme pomocí __init__ () naši class jedná se o tzv. konstruktor, který nastavuje základní atributy (proměnné) dané classy:**

  **1.1 Herní proměnné** 
	    	
            
    (řádky v kódu: 27 až 34)
        self.round_time = 0                         #Čas trvání aktuálního kola hry.
        self.slow_down_cycle = 0                    #Počítadlo cyklů pro zpomalení aktualizace času kola.        
        self.our_player_1 = our_player1             #Odkazy na objekty hráčů.
        self.our_player_2 = our_player2             #Odkazy na objekty hráčů.
        self.group_of_stones = group_of_stones      #Skupina meteoritů.  

        self.last_stone_time = 0                        #Poslední čas vytvoření meteoritu.
        self.stone_cooldown = 10                        #  self.stone_cooldown ŘÍKÁ ZA JAK DLOUHO SE VYGENERUJE DALŠÍ SÉRIE METEORITŮ (časové intervali mezi generování meteriotů)

  **1.2 Hudba v pozadí:**
		Zde se při zavolání classy  Game před hlavní herní smyčkou načte hudba 
        (řádek: 37) a začne se přehrávat hudba (řádek: 38) poté, aby hudba byla jen v pozadí je pomocí řádku 39 ztlumena 
        *hedba je neoficiálně stažena z youtube pomocí webové stránky: https://en3.onlinevideoconverter.pro/297wG/youtube-converter-mp3 
                

    (řádky v kódu: 37 až 39)             
            
            pygame.mixer.music.load("media/bg_starwars.mp3")
            pygame.mixer.music.play(-1, 0.0)
            pygame.mixer.music.set_volume(0.05)

  **1.3 Obrázky v pozadí:** 
        Podobně jako u bodu výše se soubor načte ze složky, kde byl uložen - > poté dané pozadí zmenšíme jak potřebujeme (zde podle velikosti šířky céle obrazovky hry a výšku volíme podle velikosti herního pole kde se nachází kosmické lodě) -> řádek 45 je laicky řečeno  nastaví proměnnou self.background_image_rect na obdélník (rect), který obklopuje celý obrázek self.background_image." -> řádek 46 jedná se o umístění obrázku (v tomto případu je po provedení tohoto řádku kódu levý horní roh obrázku self.background_image umístěn na pozici x=0 a y=100 na obrazovce.)
    **Jinými slovy, tento obdélník bude obsahovat informace o tom, kde se obrázek nachází a jak je velký. Tyto informace jsou užitečné pro umístění obrázku na obrazovku nebo pro detekci kolizí.*

            
        (řádky v kódu: 43 až 46 hlavní pozadí na němž se pohybují vesmírné lodě)
            self.background_image = pygame.image.load("img/bg_starwars3.webp")
            self.background_image = pygame.transform.scale(self.background_image, (1250, 400))
            self.background_image_rect = self.background_image.get_rect()
            self.background_image_rect.topleft = (0, 100)

        (řádky v kódu: 48 až 51 pozadí pod hlavním pozadím)
            self.background_space_img = pygame.image.load("img/bg_space.jpg")
            self.background_space_img = pygame.transform.scale(self.background_space_img, (1200, 100))
            self.background_space_img_rect = self.background_space_img.get_rect()
            self.background_space_img_rect.topleft = (0,500)
        
        
    **pozn. Kdyby jste se divili proč je šířka vrchního pozdí 1250 a dolního jen 1200 je to kvůli tomu aby pozadí výše bylo správně vzhledově umístěno a postavě napravo nebyla u “seknuta hlava“ jinak by zde šla šířka pozadí nastavit pod proměnnou width*

  **1.4 Fonty** 
        V této hře jsem vyzkoušel i dva způsoby vkládání textů. Konkrétně se jedná o tzv. systémové a vlastní fonty
        
                Systémové fonty:
                (řádek v kódu: 54 načtení systémového fontu)
            self.stone_font = pygame.font.SysFont("ebrima", 15)
            
                Pokud byste si chtěli vybrat svůj systémový font, napište do nového dokumentu např. ve Visual Studio tento kód níže a v terminálu se vám zobrazí
                
            import pygame
            fonts = pygame.font.get_fonts()
            for x in fonts:
                print(x)

                Vlastní fonty
                (řádky v kódu: 54 až 57 načtení vlastní fontu z internetu odkaz: )
            
            self.custom_font_small=pygame.font.Font("fonts/DeathStar-VmWB.ttf",10)
            self.custom_font_medium=pygame.font.Font("fonts/DeathStar-VmWB.ttf",25)
            self.custom_font_large=pygame.font.Font("fonts/DeathStar-VmWB.ttf",40)

  **1.5 Aktualizace hry** 
        Tato aktualizace má za úkol, aby při zavolání v této funkce se proměnná round_time zvětšila o 1. Je to důležité jelikož na základě round_time pracuje časomíra, která je zobrazena pod názvem hry, když na sebe mohou vesmírné lodě střílet 
                
                (řádky v kódu: 61 až 65)
            def update(self):
                self.slow_down_cycle += 1
                if self.slow_down_cycle == fps:
                    self.round_time += 1
                    self.slow_down_cycle = 0
    
  **1.6 Vykreslení**
        Metoda (funkce) draw vykresluje herní prvky na obrazovku 
        1. načtu si barvu > 2. Nastavím si texty > 3. vkreslení do obrazovky 

                
            def draw(self):

                1. načtu si barvu (řádky v kódu: 67 až 68)

                dark_yellow = pygame.Color("#938f0c") 


                2. Nastavím si texty (řádky v kódu: 71 až 107) 
                        
                catch_text = self.custom_font_large.render("Star", True, dark_yellow)
                catch_text_rect = catch_text.get_rect()
                catch_text_rect.centerx = width // 2
                catch_text_rect.top = 5
                catch_text1 = self.custom_font_large.render("wars", True, dark_yellow)
                catch_text_rect1 = catch_text1.get_rect()
                catch_text_rect1.centerx = width // 2
                catch_text_rect1.top = 40

                player_text_1 = self.custom_font_medium.render("PLAYER  1", True, dark_yellow)
                player_text_1_rect = player_text_1.get_rect()
                player_text_1_rect.topleft = (10, 4)

                player_text_2 = self.custom_font_medium.render("PLAYER  2", True, dark_yellow)
                player_text_2_rect = player_text_2.get_rect()
                player_text_2_rect.topright = (width - 5, 4)

                lives_text_1 = self.custom_font_medium.render(f"Zivoty: {self.our_player_1.lives}", True, dark_yellow)
                lives_text_rect_1 = lives_text_1.get_rect()
                lives_text_rect_1.topleft = (10, 30)

                lives_text_2 = self.custom_font_medium.render(f"Zivoty: {self.our_player_2.lives}", True, dark_yellow)
                lives_text_rect_2 = lives_text_2.get_rect()
                lives_text_rect_2.topright = (width - 5, 30)

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

                3. vkreslení do obrazovky (řádky v kódu: 110 až 117)
                screen.blit(catch_text, catch_text_rect)
                screen.blit(catch_text1, catch_text_rect1)
                screen.blit(player_text_1, player_text_1_rect)
                screen.blit(player_text_2, player_text_2_rect)
                screen.blit(lives_text_1, lives_text_rect_1)
                screen.blit(lives_text_2, lives_text_rect_2)
                #screen.blit(time_text, time_text_rect)     # Pouze sekundy
                screen.blit(time_text1, time_text_rect1)

                4. + tvary a ohraničení (řádky v kódu: 121 až 122)
                pygame.draw.rect(screen, tyrkys, (0, 100, width, height - 200), 5)
                pygame.draw.line(screen, tyrkys, (width // 2, 105), (width // 2, 495), 5)
    
**2.	Kameny (řádek v kódu125 až 141)**
Metoda kameny +generuje nové meteority v pravidelných intervalech:
Ze začátku mám zakomentované testování poté pokud proměnná do které se zaznamenává čas (round_time) je při odečtu minulého zaznamenaného času *(řádek v kódu 33: atribut self.last_stone_time)* větší nebo rovna *(řádek v kódu 34: atribut self.stone_cooldown)* -> pomocí smyčky for nastaví náhodný počet červených a bílích meteroidů a zavoláme si potřebnou classu do které se zaznamená *x(nastaveno), y(náhoda)* souřadnice a také se načte příslušný obrázek nakonec se určí typ meteroidu (to jsem si uvedl navíc nemuselo by to v kódu být jako ten typ). Dále jak s tím pracuje daná classa  si povíme níže (RedStone, WhiteStone)
Potom se ještě self_last_stone_time se aktualizuje na self.round_time

           
    (řádek v kódu 125 až 141)
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
           
            Určil jsem si také velice důležitou podmínku (řádky v kódu: 138 až 141)
            Zaručuje mi, že se nebude neřízeně generovat až moc meteoroidů (vyzkoušej ji odstranit a uvidíš co se stane)

            if self.stone_cooldown > 2:                                        # RYCHLOST PŘIDÁVÁNÍ METEORITŮ
                self.stone_cooldown -= 1                                 # kdyby zde nebyla podmínka tak bys potom neřízeně generovalo až moc rychle 
            else:
                pass     

**3. Pauza hry**
Metoda pause_game pozastavuje hru a zobrazuje textové zprávy.
V této metodě se nadefinují opět barvy poté si nadefinuje jaký chceceme mít hlavní text, podnadpis a text pro start a jejich umístění. Nakonec si vyplním obrazovku černou barvou a vykreslím(vypálím/vyblituju) daný text a nesmíme zapomenout na update obrazovky

Pod tím následuje smyčka pro pauzu která se v principu podobá hlavní herní smyčce akorát zde se při stisku ENTER pauza nastaví na False a celá hra se spustí 

        (řádky v kódu: 146 až 189)
                
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


>**4.2.1.2 Player_1 (Player_2)**

Uvedu příklad pouze pro player_1 jelikož player_2 je téměř totžný
Pokusím se vám tyto classy co nejlépe popsat a porovnat 

(SPOLEČNÉ) hned ze začátku jak Player_1 tak i  Player_2 představují hráče ve hře a dědí od pygame.sprite.Sprite *(řádky v kódu:Player_1 191; Player_2 247)* >co to znamená >znamená to že jak Player_1 tak Player_2 jsou podtřídou třídy Sprite z modulu pygame.sprite. Dědičnost v objektově orientovaném programování umožňuje, aby třída (potomek) zdědila atributy a metody jiné třídy (rodiče). V našem případě bychom to mohli chápat nějak takto:

1. Vlastnosti a Metody (pygame.sprite.Sprite):

pygame.sprite.Sprite poskytuje základní vlastnosti a metody, které jsou užitečné pro práci s herními objekty, jako jsou například sprity. To zahrnuje možnosti pro správu obdélníků (rect), detekci kolizí, vykreslování a aktualizaci stavu objektů.
Tím, že Player_1 dědí od pygame.sprite.Sprite, automaticky získává tyto vlastnosti a metody a může je využívat nebo přepisovat podle potřeby.

2. Skupiny spritů (pygame.sprite.Group):
*(řádky v kódu:Player_1 191; Player_2 248)*
pygame.sprite.Sprite umožňuje instancím (objektům) být přidávány do skupin spritů (pygame.sprite.Group). Skupiny spritů usnadňují správu a manipulaci s kolekcemi spritů. Můžete například aktualizovat všechny sprity ve skupině najednou nebo je všechny najednou vykreslit.
V kódu Player_1 používá skupinu spritů pro střely *(self.bullets řádek č. 202 a 258)*, což usnadňuje jejich správu a aktualizaci.

3. Metoda __init__ v pygame.sprite.Sprite:
Při volání super().__init__() v konstruktoru Player_1 se volá konstruktor rodičovské třídy pygame.sprite.Sprite. To zajišťuje, že jakékoli inicializační kód v pygame.sprite.Sprite je proveden i pro instanci Player_1. 
>>částečně stejné 
(řádky v kódu: Player_1 194 až 214 s řádky Player_2 250 až 270) jsou zde uvedeny atributy(proměnné)  Player_1 a Player_2, kde největší odlišnost je v tom, že při načítání se načte jiný obrázek (popis načítání a umístění obrázku je popsán v bodě 1.3) (je zde ale navíc použito pygame.transform.rotate(self.image, 270)  který obrázek pootočí o požadovaný počet stupňů)

Poté jsou zde doposud nezmíněné atributy jako self.lives = 5 (životy), self.speed = 8 (rychlost vemirných lodí)


>>Metoda update(self)
(SPOLEČNÉ)
díky této metodě, která je volána do hlavní herní smyčky se hráči ovládají, popis ovadání je poznamenán v bodě OVLÁDÁNÍ HRY, na konci této metody je voláno self.bullets.update()  což aktualizuje všechny střely, které patří do skupiny self.bullets.


            (řádky v kódu:Player_1 217 až 229; Player_2 273 až 288)
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


>>Metoda fire_bullet(self):
*částečně stejné akorát (řádek v kódu:Player_1 238 a Player_2 293) se liší 10 a -10 což je ryschlost a zároveň pohybystřely* 
jedná se o jednoduchou metodu kdy při jejím zavolání se current_time nastaví na aktuální čas (zde jsem si chtěl vyzkoušet počítat čas podle metody pygame.time.get_ticks(), která je součástí knihovny  Pygame.) Tento čas se počítá od momentu, kdy byla volána funkce pygame.init() *(řádek v kódu 6)*. Tato metoda vrací počet milisekund, které uplynuly od doby, kdy byla Pygame inicializována. > potom se počítá množství vystřených střel a zároveň musí být splněna podmínka, která hráči umožňuje po uplynutí určité doby vystřelit, tak aby hráč nestřílel neustále, a poté se po každém výstřelu přehraje zvuk střely. 


    (řádky v kódu:Player_1 235 až 241; Player_2 290 až 296)
        def fire_bullet(self):
            current_time = pygame.time.get_ticks()
            if len(self.bullets) < 3 and current_time - self.last_shot_time >= self.shot_cooldown:
                bullet = Bullet(self.rect.left, self.rect.centery, -10, shooter=1)
                self.bullets.add(bullet)
                self.last_shot_time = current_time
                self.zap_sound.play()

>>Metoda draw(self, surface):

Další a zároveň poslední metodou v classe Game je draw, která vykreslí obrázek hráče na daný povrch na pozici danou jeho obdélníkem (rect) a poté vykreslí střely na daný povrch.
            

    (řádky v kódu:Player_1 243 až 245; Player_2 298 až 300)
        def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.bullets.draw(surface)

>**4.2.1.3 Bullet**

*podobně jako u Player_1 a Player_2* 
dědí od pygame.sprite.Sprite (řádek v kódu 302) >co to znamená >znamená to že Bullet je podtřídou třídy Sprite z modulu pygame.sprite. Dědičnost v objektově orientovaném programování umožňuje, aby třída (potomek) zdědila atributy a metody jiné třídy (rodiče). V konstruktoru jsme si definovali i souřednice *x, y* a poté i *speed(rychlost pohybu hráče)* a *shooter(druh střelce)* je zde i *super().__init__()* což je popsáno v bodě 3 v části **Player_1 a Player_2**
self.image = pygame.Surface((15, 5)) je velikost střely a poté pomocí podmínky když známe typ shootra vykreslí se nám pomocí podmínky příslušná barva střel > poté převedeme na rect a umístíme danou střelu podle daných x a y souřadnic 

    (řádky v kódu: 302 až 317)
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

>>Metoda update(self):

>Aktualizace pozice:
Přidává hodnotu speed k souřadnici x obdélníku (rect), což způsobuje pohyb střely ve směru její rychlosti.

    (řádek v kódu 321)
            self.rect.x += self.speed

>Odstranění střely, pokud opustí obrazovku:
Pokud střela opustí obrazovku (její pravý okraj je menší než 0 nebo její levý okraj je větší než šířka obrazovky width), zavolá se metoda kill(), která odstraní střelu ze všech skupin spriteů, ve kterých je.

    (řádek v kódu 322 a 323) 
            if self.rect.right < 0 or self.rect.left > width:
                self.kill()

>**4.2.1.4 RedStone (WhiteStone tato třída je téměř stejná až na to že se x souřadnice přičítá)**

Tato classa představuje ve hře červený kámen/meteoroid, který se pohybuje z levé strany na levou stranu hracího pole. U classy WhiteStone se pohybuje bílý kámen/meteoroid pohybující se pravé strany na levou **což je jediný rozdíl co tyto classy odlišuje** (u classy RedStone se odečítá x a u classy WhiteStone se x odečítá) Obě dvě tyto classy dědí od pygame.sprite.Sprite stejně jako například Player_1.

    (řádky v kódu:RedStone 325 až 335; WhiteStone 337 až 347)

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

>Jako první si vytvoříme konstruktor, co daná classa bude obsahovat 

        (řádek v kódu: 326)
        def __init__(self, x, y, image, stone_type):


>>x, y: Počáteční souřadnice středu kamene.

>>image: Obrázek kamene, který bude zobrazen.

>>stone_type: Typ kamene, který může ovlivňovat jeho vlastnosti nebo chování.

>Inicializace rodičovské třídy: 

    (řádek v kódu 327)
        super().__init__()

>Nastavení obrázku kamene a uložení obrázku, který se použije při vykreslování:
        
    (řádek v kódu 328)
        self.image = image

>Nastavení rect pro pozicování:
Získá rect pro obrázek a nastaví jeho středové souřadnice na (x, y). Tím se určí počáteční pozice kamene na obrazovce.

    (řádky v kódu 329 a 330)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

>Nastavení typu kamene (to jsem si vytvořil pro možné rozšíření kódu)
            
    (řádek v kódu 331)
        self.type = stone_type

>Nastavení rychlosti kamene
Nastaví náhodnou rychlost kamene v rozmezí od 1 do 5. To určuje, jak rychle se kámen pohybuje po obrazovce.

    (řádek v kódu 332)
        self.speed = random.randint(1, 5)

>Metoda update(self)
*zde se liší classa RedStone od WhiteStone*
Metoda, která se volá každým snímkem pro aktualizaci stavu kamene. U classy RedStone se self.speed odečítá od polohy obrázku, kde se zrovna nachází a pohybuje se směrem doleva. Naopak u classy WhiteStone je to naopak zde se self.speed přičítá a kámen se tedy pohybuje doprava.

        (řádky v kódu: RedStone 334 a 335)
        def update(self):
            self.rect.x -= self.speed

        (řádky v kódu: RedStone 346 a 347)
        def update(self):
            self.rect.x += self.speed


Pod tímto by mělo být tzv. použití logiky, kterou jsme si výše udělali a v kódu níže se bude jen volat nad a do hlavní herní smyčky. Jelikož je to moje první hra v pygame zkusil jsem přidat i nějakou herní logiku do a pod hlavní herní smyčku, jelikož určité internetové zdroje uvádí, že to není špatně psát herní logiku do části, kde se nachází hlavní herní smyčka, ale není to přehledné, proto se doporučuje využít objektově orientovaného programování s veškerou herní logiku psát mimo hlavní herní smyčku.

>**4.3 Použití logiky**      
>4.3.1 Před hlavní herní smyčkou 

>>Vytvoříme si dvě skupiny jednu pro hráče a druhou pro meteoroidy 

    (řádky v kódu 354 a 357)  
        
        stone_group = pygame.sprite.Group()
        player_group = pygame.sprite.Group()

>>Do skupin hráčů přidáme hráče

    (řádky v kódu 358 a 360)

        one_player_1 = Player_1()   # one_player_1 instance třídy Player_1()
        one_player_2 = Player_2()   # one_player_2 instance třídy Player_2()

        **Co je to inscenace 
        Když vytvoříte instanci třídy, vytváříte konkrétní výskyt této třídy, který má své vlastní jedinečné hodnoty atributů a může provádět akce pomocí metod definovaných v této třídě. Například, pokud máme třídu Auto, pak instance této třídy může být konkrétní auto s různými vlastnostmi, jako je značka, barva, rychlost atd.

        class Auto:
            def __init__(self, značka, barva):
                self.značka = značka
                self.barva = barva

        auto1 = Auto("Škoda", "červená")
        auto2 = Auto("Ford", "modrá")

        Zde auto1 a auto2 jsou instance třídy Auto. Každá instance má své vlastní hodnoty pro atributy značka a barva.**




>>Vytvoření objektu Game:

je inicializována s hráči one_player_1 a one_player_2 a skupinou stone_group.
my_game je opět instance třídy Game 

    (řádek v kódu 364)
        my_game = Game(one_player_1, one_player_2, stone_group)

>>Poté proměnnou *lets_continue* nastavíme na True tzn. že může probíhat hlavní herní smyčka, dokud se *lets_continue* nenastaví na False.

>>Voláme metodu *my_game.kameny()*, která mi po určitém nastaveném čase přidá meteoroidy. 

>>Před samotným spuštěním hry se pomocí zavolání metody *my_game.pause_game("STARWARS", "Stiskni enter pro zahajeni hry"," ")* hra pozastaví a vypíše mi to předem určený text.

>>*clock = pygame.time.Clock()* vytváří objekt Clock, který se používá pro správu času a nastavování snímkové frekvence.

>>*start_time = time.time()* ukládá aktuální čas do proměnné start_time. Tento čas může být použit pro měření doby trvání hry nebo jiných časově závislých událostí.

>4.3.2 Hlavní cyklus
        (řádky v  kódu 374 až 500)

Jak jsem výše zmiňoval mělo by zde být pouze volání class a jejich metod *(řádky v kódu 379 až 393)*, já jsem se pokusil do tohoto hlavního cyklu přidat i logiku, která by měla být použita výše v kódu 


Celá hra funguje na základě cyklu *while*, ve která se neustále volají funkce a provádí další cyklay jako je např. cyklus *for*

Jako základ hry se dájí považovat řádky v kódu 374 až 377


    while lets_continue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lets_continue = False

,kde pokud je *lets_continue* nasatveno na True hra probíhá a mezitím co hra běží, tak pomocí cyklu *for* se prochází veškeré *event* (jakákoli akce na herním poli) a pokud je tato akce rovna *QUIT* (kliknutí na křížek v pravém horním rohu pro zavření okna, ve kterém hra běží), herní okono se zavře, jelikož se *lets_continue = False* a hra se tím pádem ukončí.

Pokud ale hráč na tento křížek neklikne, hra běží a volají se metody daných class

    (řádky v kódu: 379 až 393)
        screen.fill((0, 0, 0))                                                          #překryje obrazovku černou barvou       
        screen.blit(my_game.background_image, my_game.background_image_rect)                #vykreslí se požadované pozadí
        screen.blit(my_game.background_space_img,my_game.background_space_img_rect)         #vykreslí se požadované pozadí
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

Poté jsme se rozhodl jak jsem výše několikrát zmiňoval, uvést do hlavní herní smyčky herní logiku, která by měla být spíše v nějaké classe a poté se jen zavolá do hlavní herní smyčky.
*Přišlo mi to dobré z důvodu porovnání toho že pokud zařadíme herní logiku přímo do hlavní herní smyčky stane se hlavní herní smyčka docela nepřehledná*

Uvedl jsem si zde za 1. kolize Player_1 a kolize Player_2 a za 2. poté kontrolu konce hry, když jednomu z hráčů dodou životy

>1. Kolize hráčů (popíšu zde kolize Player_2, jelikož kolize Player_1 jsou naprosto stejné akorát jsou zde zaměněné proměnné aby to odpovídalo Player_1)

>>Detekce protivníkovy střely
    (řádky v kódu 398 až 402)

    for bullet in one_player_1.bullets:
        if pygame.sprite.collide_rect(bullet, one_player_2):
            bullet.kill()                                   #KDYBY zde nebylo bullet.kill() tak se životy budou odečítat hrozně rychle
            one_player_2.lives -= 1
            one_player_2.demage_by_bullet_sound.play()

*for bullet in one_player_1.bullets:* ... prochází všechny střely, které hráč 1 vystřelil

*if pygame.sprite.collide_rect(bullet, one_player_2):* ... kontroluje, zda se hranice střely překrývají s hranicemi hráče 2. 

*bullet.kill()* ... odstraní střelu ze hry

*one_player_2.lives -= 1*  ... sníží počet životů hráče 2 o jedna

*one_player_2.demage_by_bullet_sound.play()* ... přehraje zvuk poškození, který signalizuje zásah


>>Detekce kolizí střel hráče s bílými a červenými kameny  (u Player_1 je tato část kódu stejná)

    (řádky v kódu: Player_2 404 až 415; Player_1 431 až 443)

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

*[stone for stone in stone_group if isinstance(stone, WhiteStone)]:* ... vytvoří seznam všech objektů v stone_group, které jsou instance třídy WhiteStone.

*[stone for stone in stone_group if isinstance(stone, RedStone)]:* ... vytvoří seznam všech objektů v stone_group, které jsou instance třídy RedStone.


*for white_stone in [stone for stone in stone_group if isinstance(stone, WhiteStone)]:* ... prochází všechny bílé kameny.

*for red_stone in [stone for stone in stone_group if isinstance(stone, RedStone)]:* ... prochází všechny červené kameny.


*if pygame.sprite.collide_rect(bullet, red_stone):* ... kontroluje, zda se hranice střely překrývají s hranicemi bílého kamene.

*if pygame.sprite.collide_rect(bullet, red_stone):* ... kontroluje, zda se hranice střely překrývají s hranicemi červeného kamene.


*bullet.kill()* ... odstraní střelu ze hry.


*white_stone.kill()* ... odstraní bílý kámen ze hry.

*red_stone.kill()* ... odstraní červený kámen ze hry.


*one_player_1.destroy_sound.play()* ... přehraje zvuk zničení, který signalizuje zásah.

*one_player_2.destroy_sound.play()* ... přehraje zvuk zničení, který signalizuje zásah.

>>Detekce kolizí Player_2 s červenými kameny 

    (řádky v kódu: Player_2 418 až 422; Player_1 446 až 450)

    for white_stone in [stone for stone in stone_group if isinstance(stone, WhiteStone)]:
    if pygame.sprite.collide_rect(white_stone, one_player_1):
        white_stone.kill()
        one_player_1.lives -= 1
        one_player_1.demage_by_stone.play()


*[stone for stone in stone_group if isinstance(stone, WhiteStone)]:* ... vytvoří seznam všech objektů v stone_group, které jsou instance třídy WhiteStone.

*for white_stone in [stone for stone in stone_group if isinstance(stone, WhiteStone)]:* ... prochází všechny bílé kameny.

*if pygame.sprite.collide_rect(bullet, red_stone):* ... kontroluje, zda se hranice bílého kamene překrývají s hranicemi Player_2.

*bullet.kill()* ... odstraní střelu ze hry.

*one_player_2.lives -= 1*  ... sníží počet životů hráče 2 o jedna

*one_player_2.destroy_sound.play()* ... přehraje zvuk zničení, který signalizuje zásah.

>>**u kolizí Player_1 se proměnné *one_player_1* zamění za *one_player_2* a proměnné *one_player_2* se zamění za *one_player_1***

>2. Kontrola konce hry
Ve stručnosti, pokud jeden z hráčů Player_1 nebo Player_2 dosáhne nula životů, hra se zastaví, vypíše se kdo vyhrál popřípadě, jak hrát od znovu (stisknutím klávesy ENTER). Pukod by hráči chtili hrát od začátku hra se resetuje a hra se nastaví do výchozího stavu.

*pygame.display.update()* ... tento příkaz aktualizuje obrazovku *je to ekvivalent "vykreslení" aktuálního stavu hry*

*clock.tick(fps)* ... tento příkaz řídí rychlost herního cyklu


    (řádky v kódu 453 až 497)
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

>Nakonec ***pygame.quit()*** ... tento příkaz slouží k ukončení knihovny Pygame a správnému uzavření všech jejích modulů, což zabrání potenciálním problémům s uvolněním zdrojů

>**5. ZÁVĚR**

Hned ze začátku tohoto závěru bych chtěl zmínit, že se jednalo o nejvíce složitý vytvořený kód, díky němuž jsem se toho dost naučil, hlavně co se týče určitých základů objektivně orientovaného programování. Co se týče nějakého mého hodnocení samotného kódu, určitě by šel zase napsat mnohem jednodušeji a přehledněji, než je napsán např. přidáním funkcí. Dokonce jsem si zkusil převo hry do exe souboru.