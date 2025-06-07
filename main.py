from pygame import*
import pygame
from random import*
import random
import js
import time
pygame.init()
fps=60
timer= pygame.time.Clock()
fenetre = pygame.display.set_mode((1068,700))
liste_carte=0
accueil=1
tirage_fenetre=0

loevan_save=0

random.seed(time.time()) 

fon=pygame.image.load("assets/fond.png")
fond=pygame.image.load("assets/fondd.png")
fond_tirage=pygame.image.load("assets/fond_tirage.png")
fond_cartes=pygame.transform.smoothscale(pygame.image.load("assets/fond_cartes.png"),(1068,700))
coffre= pygame.transform.smoothscale(pygame.image.load("assets/coffre.png"),(600,450))
add=pygame.transform.smoothscale(pygame.image.load("assets/add_friend.png"),(100,100))
liste=pygame.transform.smoothscale(pygame.image.load("assets/liste.png"),(100,100))
home=pygame.transform.smoothscale(pygame.image.load("assets/home.png"),(50,50))
xadd=0
yadd=0
xliste=0
yliste=50

etoile1=pygame.transform.smoothscale(pygame.image.load("assets/1.1.png"),(50,50))
etoile2=pygame.transform.smoothscale(pygame.image.load("assets/1.2.png"),(50,50))
etoile3=pygame.transform.smoothscale(pygame.image.load("assets/1.3.png"),(50,50))

choix=None

éléments = ['loevan', 'enzo', 'evhann','hugo','noah','mathys','yann','lucas','alwyn','gweltaz','theo','malo','evanne','illy','erenn','elliot','youn','nathan','laou','awen','antoine']
probabilités = [4.975,4.975,1,
                1,5.8,4.975,
                1,3.8,4.975,
                5.8,3.5,3.5,
                4.975,4.975,4.975,
                1,3.8,3.5,
                4.975,3.5,3.8]
def tirage():
    global choix
    choix = random.choices(éléments, weights=probabilités, k=1)[0]
    print(choix)
    return choix

cartes = {
    'loevan': pygame.transform.smoothscale(pygame.image.load("assets/loevan.png"),(357,500)).convert_alpha(),
    'enzo': pygame.transform.smoothscale(pygame.image.load("assets/enzo.png").convert_alpha(),(357,500)).convert_alpha(),
    'evhann': pygame.transform.smoothscale(pygame.image.load("assets/evhann.png").convert_alpha(),(357,500)).convert_alpha(),
    'hugo': pygame.transform.smoothscale(pygame.image.load("assets/hugo.png").convert_alpha(),(357,500)).convert_alpha(),
    'noah': pygame.transform.smoothscale(pygame.image.load("assets/noah.png").convert_alpha(),(357,500)).convert_alpha(),
    'mathys': pygame.transform.smoothscale(pygame.image.load("assets/mathys.png").convert_alpha(),(357,500)).convert_alpha(),
    'yann': pygame.transform.smoothscale(pygame.image.load("assets/yann.png").convert_alpha(),(357,500)).convert_alpha(),
    'lucas': pygame.transform.smoothscale(pygame.image.load("assets/lucas.png").convert_alpha(),(357,500)).convert_alpha(),
    'alwyn': pygame.transform.smoothscale(pygame.image.load("assets/alwyn.png").convert_alpha(),(357,500)).convert_alpha(),
    'gweltaz': pygame.transform.smoothscale(pygame.image.load("assets/gweltaz.png").convert_alpha(),(357,500)).convert_alpha(),
    'theo': pygame.transform.smoothscale(pygame.image.load("assets/theo.png").convert_alpha(),(357,500)).convert_alpha(),
    'malo': pygame.transform.smoothscale(pygame.image.load("assets/malo.png").convert_alpha(),(357,500)).convert_alpha(),
    'evanne': pygame.transform.smoothscale(pygame.image.load("assets/evanne.png").convert_alpha(),(357,500)).convert_alpha(),
    'illy': pygame.transform.smoothscale(pygame.image.load("assets/illy.png").convert_alpha(),(357,500)).convert_alpha(),
    'erenn': pygame.transform.smoothscale(pygame.image.load("assets/erenn.png").convert_alpha(),(357,500)).convert_alpha(),
    'elliot': pygame.transform.smoothscale(pygame.image.load("assets/elliot.png").convert_alpha(),(357,500)).convert_alpha(),
    'youn': pygame.transform.smoothscale(pygame.image.load("assets/youn.png").convert_alpha(),(357,500)).convert_alpha(),
    'nathan': pygame.transform.smoothscale(pygame.image.load("assets/nathan.png").convert_alpha(),(357,500)).convert_alpha(),
    'laou': pygame.transform.smoothscale(pygame.image.load("assets/laou.png").convert_alpha(),(357,500)).convert_alpha(),
    'awen': pygame.transform.smoothscale(pygame.image.load("assets/awen.png").convert_alpha(),(357,500)).convert_alpha(),
    'antoine': pygame.transform.smoothscale(pygame.image.load("assets/antoine.png").convert_alpha(),(357,500)).convert_alpha(),
}

scores = {
    'loevan': 0,
    'enzo': 0,
    'evhann': 0,
    'hugo': 0,
    'noah': 0,
    'mathys': 0,
    'yann': 0,
    'lucas':0,
    'alwyn': 0,
    'gweltaz':0,
    'theo': 0,
    'malo':0,
    'evanne': 0,
    'illy': 0,
    'erenn': 0,
    'elliot': 0,
    'youn': 0,
    'nathan': 0,
    'laou': 0,
    'awen': 0,
    'antoine': 0,
}

affi = {
    'loevan': 0,
    'enzo': 0,
    'evhann': 0,
    'hugo': 0,
    'noah': 0,
    'mathys': 0,
    'yann': 0,
    'lucas':0,
    'alwyn': 0,
    'gweltaz':0,
    'theo': 0,
    'malo':0,
    'evanne': 0,
    'illy': 0,
    'erenn': 0,
    'elliot': 0,
    'youn': 0,
    'nathan': 0,
    'laou': 0,
    'awen': 0,
    'antoine': 0,
}

def ajouter_point(nom):
    if nom in scores:
        if scores[nom]==0:
            fonte = pygame.font.Font("assets/ecriture.ttf",35)
            text = fonte.render("Nouvelle carte débloquée",1,(255,255,255))
            fenetre.blit(text,(365,40))

        scores[nom] += 1
        sauvegarder_scores()
        print(f"{nom} a maintenant {scores[nom]} points.")

def nb_cartes(nomb):
    fonte = pygame.font.Font("assets/ecriture.ttf",35)
    text = fonte.render(f"{scores[nomb]} cartes collectées",1,(255,255,255))
    fenetre.blit(text,(425,580))
        

def afficher_image_choix():
    global nom
    nom = choix 
    if nom in cartes:
        fenetre.blit(fon,(0,0))
        temp = cartes[nom].copy()
        temp.set_alpha(100)
        fenetre.blit(temp, (355, 95))
        fenetre.blit(etoile1, (720, 105))
        fenetre.blit(etoile1, (300, 450))

def afficher_image_choix2():
    nom = choix 
    if nom in cartes:
        fenetre.blit(fon,(0,0))
        temp = cartes[nom].copy()
        temp.set_alpha(175)
        fenetre.blit(temp, (355, 95))
        fenetre.blit(etoile2, (720, 105))
        fenetre.blit(etoile2, (300, 450))

def afficher_image_choix3():
    nom = choix 
    if nom in cartes:
        fenetre.blit(fon,(0,0))
        temp = cartes[nom].copy()
        temp.set_alpha(255)
        fenetre.blit(temp, (355, 95))
        fenetre.blit(etoile3, (720, 105))
        fenetre.blit(etoile3, (300, 450))
        
def charger_scores():
    for nom in scores:
        valeur = js.window.localStorage.getItem(nom)
        if valeur is not None:
            scores[nom] = int(valeur)  
    
def sauvegarder_scores():
    for nom, score in scores.items():
        js.window.localStorage.setItem(nom, str(score))


carte_grande=0        
click=0
maxclick=5
dernier_tirage_fait=False

while accueil:
    charger_scores()
    fenetre.blit(fond,(0,0))
    fenetre.blit(add,(400,550))
    fenetre.blit(liste,(550,550))
    for event in pygame.event.get():
           if event.type == QUIT:
               accueil=0
           if event.type == pygame.MOUSEBUTTONDOWN:
                xpos,ypos=event.pos
                if (xpos>400 and xpos<400+100) and (ypos>550 and ypos<550+100):
                    tirage_fenetre=1
                    
                if (xpos>550 and xpos<550+100) and (ypos>550 and ypos<550+100):
                    liste_carte=1
                    
                
    while tirage_fenetre:
        
        
        for event in pygame.event.get():
            if event.type == QUIT:
                tirage_fenetre=0
            if event.type == pygame.MOUSEBUTTONDOWN and click<maxclick:
                click+=1    
                tirage()
                afficher_image_choix()
                pygame.display.flip()
                time.sleep(0.05)
                afficher_image_choix2()
                pygame.display.flip()
                time.sleep(0.05)
                afficher_image_choix3()
                ajouter_point(nom)
                pygame.display.flip()
                dernier_tirage_fait=True
                time.sleep(0.4)
        if not dernier_tirage_fait:
            fenetre.blit(fond_tirage, (0, 0))
            fenetre.blit(coffre, (240, 100))
            pygame.display.flip()
        
        if click>=maxclick: 
            dernier_tirage_fait=False   
            tirage_fenetre=0 
            click=0   
                
        pygame.display.flip()
    
    while liste_carte:
        fenetre.blit(fond_cartes,(0,0))
        fenetre.blit(home,(0,0))
        
        
        
        for event in pygame.event.get():
           
            if event.type == QUIT:
               liste_carte=0
            if event.type == pygame.MOUSEBUTTONDOWN:
                xpos,ypos=event.pos
                if (xpos>xadd and xpos<xadd+50) and (ypos>yadd and ypos<yadd+50):
                    liste_carte=0
                if (xpos>610 and xpos<740) and (ypos>467 and ypos<667):
                    if scores['elliot']>=1:
                        carte_grande=1
                        affi['elliot']=1
                if (xpos>470 and xpos<600) and (ypos>467 and ypos<667):
                    if scores['awen']>=1:
                        carte_grande=1
                        affi['awen']=1
        if scores['noah']>=1:
            fenetre.blit(pygame.transform.smoothscale(cartes['noah'],(130,201)),(50,47))
            if (xpos>50 and xpos<180) and (ypos>47 and ypos<247):
                carte_grande=1
                affi['noah']=1
                
                
        if scores['gweltaz']>=1:
            fenetre.blit(pygame.transform.smoothscale(cartes['gweltaz'],(130,200)),(190,47))
            if (xpos>190 and xpos<320) and (ypos>47 and ypos<247):
                carte_grande=1
                affi['gweltaz']=1
        
        
        if scores['illy']>=1:
            fenetre.blit(pygame.transform.smoothscale(cartes['illy'],(130,200)),(330,47))
            if (xpos>330 and xpos<460) and (ypos>47 and ypos<247):
                carte_grande=1
                affi['illy']=1

        if scores['laou']>=1:
            fenetre.blit(pygame.transform.smoothscale(cartes['laou'],(130,200)),(470,47))
            if (xpos>470 and xpos<600) and (ypos>47 and ypos<247):
                carte_grande=1
                affi['laou']=1
        
        if scores['loevan']>=1:
            fenetre.blit(pygame.transform.smoothscale(cartes['loevan'],(130,201)),(610,47))
            if (xpos>610 and xpos<740) and (ypos>47 and ypos<247):
                carte_grande=1
                affi['loevan']=1

        if scores['mathys']>=1:
            fenetre.blit(pygame.transform.smoothscale(cartes['mathys'],(130,200)),(750,47))
            if (xpos>750 and xpos<880) and (ypos>47 and ypos<247):
                carte_grande=1
                affi['mathys']=1
        
        if scores['erenn']>=1:
            fenetre.blit(pygame.transform.smoothscale(cartes['erenn'],(130,200)),(890,47))
            if (xpos>890 and xpos<1020) and (ypos>47 and ypos<247):
                carte_grande=1
                affi['erenn']=1

        if scores['alwyn']>=1:
            fenetre.blit(pygame.transform.smoothscale(cartes['alwyn'],(132,201)),(50,257))
            if (xpos>50 and xpos<180) and (ypos>257 and ypos<457):
                carte_grande=1
                affi['alwyn']=1

        if scores['enzo']>=1:
            fenetre.blit(pygame.transform.smoothscale(cartes['enzo'],(130,201)),(190,257))
            if (xpos>190 and xpos<320) and (ypos>257 and ypos<457):
                carte_grande=1
                affi['znzo']=1

        if scores['evanne']>=1:
            fenetre.blit(pygame.transform.smoothscale(cartes['evanne'],(130,201)),(330,257))
            if (xpos>330 and xpos<460) and (ypos>257 and ypos<457):
                carte_grande=1
                affi['evanne']=1
        
        if scores['lucas']>=1:
            fenetre.blit(pygame.transform.smoothscale(cartes['lucas'],(130,201)),(470,257))
            if (xpos>470 and xpos<600) and (ypos>257 and ypos<457):
                carte_grande=1
                affi['lucas']=1
                
                
        if scores['youn']>=1:
            fenetre.blit(pygame.transform.smoothscale(cartes['youn'],(130,201)),(610,257))
            if (xpos>610 and xpos<740) and (ypos>257 and ypos<457):
                carte_grande=1
                affi['youn']=1
        
        
        if scores['evhann']>=1:
            fenetre.blit(pygame.transform.smoothscale(cartes['evhann'],(130,201)),(750,257))
            if (xpos>750 and xpos<880) and (ypos>257 and ypos<457):
                carte_grande=1
                affi['evhann']=1

        if scores['antoine']>=1:
            fenetre.blit(pygame.transform.smoothscale(cartes['antoine'],(130,201)),(890,257))
            if (xpos>890 and xpos<1020) and (ypos>257 and ypos<457):
                carte_grande=1
                affi['antoine']=1
        
        if scores['nathan']>=1:
            fenetre.blit(pygame.transform.smoothscale(cartes['nathan'],(130,202)),(50,467))
            if (xpos>50 and xpos<180) and (ypos>467 and ypos<667):
                carte_grande=1
                affi['nathan']=1

        if scores['malo']>=1:
            fenetre.blit(pygame.transform.smoothscale(cartes['malo'],(130,202)),(190,467))
            if (xpos>190 and xpos<320) and (ypos>467 and ypos<667):
                carte_grande=1
                affi['malo']=1
        
        if scores['theo']>=1:
            fenetre.blit(pygame.transform.smoothscale(cartes['theo'],(130,202)),(330,467))
            if (xpos>330 and xpos<460) and (ypos>467 and ypos<667):
                carte_grande=1
                affi['theo']=1

        if scores['awen']>=1:
            fenetre.blit(pygame.transform.smoothscale(cartes['awen'],(130,202)),(470,467))
            

        if scores['elliot']>=1:
            fenetre.blit(pygame.transform.smoothscale(cartes['elliot'],(130,202)),(610,467))
            

        if scores['yann']>=1:
            fenetre.blit(pygame.transform.smoothscale(cartes['yann'],(130,202)),(750,467))
            if (xpos>750 and xpos<880) and (ypos>467 and ypos<667):
                carte_grande=1
                affi['yann']=1

        if scores['hugo']>=1:
            fenetre.blit(pygame.transform.smoothscale(cartes['hugo'],(130,202)),(890,467))
            if (xpos>890 and xpos<1020) and (ypos>467 and ypos<667):
                carte_grande=1
                affi['hugo']=1

        while carte_grande:
            fenetre.blit(fon,(0,0))
            fenetre.blit(home,(0,0))
            
            
            
            if affi['loevan']==1:
                fenetre.blit(pygame.transform.smoothscale(cartes['loevan'],(357,500)),(355,50))
                nb_cartes('loevan')
            if affi['enzo']==1:
                fenetre.blit(pygame.transform.smoothscale(cartes['enzo'],(357,500)),(355,50))
                nb_cartes('enzo')
            if affi['evhann']==1:
                fenetre.blit(pygame.transform.smoothscale(cartes['evhann'],(357,500)),(355,50))
                nb_cartes('evhann')
            if affi['gweltaz']==1:
                fenetre.blit(pygame.transform.smoothscale(cartes['gweltaz'],(357,500)),(355,50))
                nb_cartes('gweltaz')
            if affi['hugo']==1:
                fenetre.blit(pygame.transform.smoothscale(cartes['hugo'],(357,500)),(355,50))
                nb_cartes('hugo')
            if affi['yann']==1:
                fenetre.blit(pygame.transform.smoothscale(cartes['yann'],(357,500)),(355,50))
                nb_cartes('yann')
            if affi['noah']==1:
                fenetre.blit(pygame.transform.smoothscale(cartes['noah'],(357,500)),(355,50))
                nb_cartes('noah')
            if affi['mathys']==1:
                fenetre.blit(pygame.transform.smoothscale(cartes['mathys'],(357,500)),(355,50))
                nb_cartes('mathys')
            if affi['lucas']==1:
                fenetre.blit(pygame.transform.smoothscale(cartes['lucas'],(357,500)),(355,50))
                nb_cartes('lucas')
            if affi['alwyn']==1:
                fenetre.blit(pygame.transform.smoothscale(cartes['alwyn'],(357,500)),(355,50))
                nb_cartes('alwyn')
            if affi['theo']==1:
                fenetre.blit(pygame.transform.smoothscale(cartes['theo'],(357,500)),(355,50))
                nb_cartes('theo')
            if affi['antoine']==1:
                fenetre.blit(pygame.transform.smoothscale(cartes['antoine'],(357,500)),(355,50))
                nb_cartes('antoine')
            if affi['elliot']==1:
                fenetre.blit(pygame.transform.smoothscale(cartes['elliot'],(357,500)),(355,50))
                nb_cartes('elliot')
            if affi['malo']==1:
                fenetre.blit(pygame.transform.smoothscale(cartes['malo'],(357,500)),(355,50))
                nb_cartes('malo')
            if affi['nathan']==1:
                fenetre.blit(pygame.transform.smoothscale(cartes['nathan'],(357,500)),(355,50))
                nb_cartes('nathan')
            if affi['youn']==1:
                fenetre.blit(pygame.transform.smoothscale(cartes['youn'],(357,500)),(355,50))
                nb_cartes('youn')
            if affi['laou']==1:
                fenetre.blit(pygame.transform.smoothscale(cartes['laou'],(357,500)),(355,50))
                nb_cartes('laou')
            if affi['erenn']==1:
                fenetre.blit(pygame.transform.smoothscale(cartes['erenn'],(357,500)),(355,50))
                nb_cartes('erenn')
            if affi['illy']==1:
                fenetre.blit(pygame.transform.smoothscale(cartes['illy'],(357,500)),(355,50))
                nb_cartes('illy')
            if affi['evanne']==1:
                fenetre.blit(pygame.transform.smoothscale(cartes['evanne'],(357,500)),(355,50))
                nb_cartes('evanne')
            if affi['awen']==1:
                fenetre.blit(pygame.transform.smoothscale(cartes['awen'],(357,500)),(355,50))
                nb_cartes('awen')
            
            
            
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    carte_grande=0
                if event.type == pygame.MOUSEBUTTONDOWN:
                        xpos,ypos=event.pos
                        if (xpos>xadd and xpos<xadd+50) and (ypos>yadd and ypos<yadd+50):
                            carte_grande=0
                            for key in affi:
                                affi[key] = 0
            pygame.display.flip()

        pygame.display.flip()

    
    pygame.display.flip()

pygame.quit()
