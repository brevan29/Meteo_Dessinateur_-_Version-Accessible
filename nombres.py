from turtle import *
from lettres import *

def un(vx: int, vy: int,multi=40):
    multi=multi/40
    goto(vx+10*multi,vy)
    down()
    goto(vx+10*multi,vy+40*multi)
    goto(vx,vy+20*multi)
    up()
    return 10*multi+5

def deux(vx: int, vy: int,multi=40):
    multi=multi/40
    goto(vx+20*multi,vy)
    down()
    setheading(0)
    backward(int(20*multi))
    setheading(40)
    goto(vx+int(16*multi),vy+int(22*multi))
    circle(int(10*multi),270)
    up()
    return 20*multi+5

def trois(vx: int, vy: int,multi=40):
    multi=multi/40
    goto(vx+10*multi,vy+20*multi)
    setheading(0)
    down()
    circle(10*multi,270)
    up()
    goto(vx,vy+10*multi)
    setheading(270)
    down()
    circle(10*multi,270)
    up()
    return 20*multi+5

def quatre(vx: int, vy: int,multi=40):
    multi=multi/40
    goto(vx+15*multi,vy)
    down()
    goto(vx+15*multi,vy+20*multi)
    up()
    goto(vx+15*multi,vy+40*multi)
    down()
    goto(vx,vy+10*multi)
    goto(vx+20*multi,vy+10*multi)
    up()
    return 20*multi+5
    
def cinq(vx: int, vy: int,multi=40):
    multi=multi/40
    goto(vx+int(18*multi),vy+int(40*multi))
    setheading(180)
    down()
    forward(int(18*multi))
    left(90)
    forward(int(15*multi))
    up()
    goto(vx,vy)
    down()
    setheading(339)
    circle(13.5*multi,220)
    up()
    return 20*multi+5
    
    
def six(vx: int, vy: int,multi=40):
    multi=multi/40
    goto(vx,vy+int(10*multi))
    down()
    setheading(270)
    circle(int(10*multi))
    backward(int(20*multi))
    circle(int(10*multi),-145)
    up()
    return 20*multi+5
    
def sept(vx: int, vy: int,multi=40):
    multi=multi/40
    goto(vx,vy+int(40*multi))
    down()
    goto(vx+int(20*multi),vy+int(40*multi))
    goto(vx,vy)
    up()
    return 20*multi+5

def huit(vx: int, vy: int,multi=40):
    multi=multi/40
    setheading(90)
    for vi in range (10,31,20):
        goto(vx+20*multi,vy+vi*multi)
        down()
        circle(10*multi)
        up()
    return 20*multi+5

def neuf(vx: int, vy: int,multi=40):
    multi=multi/40
    goto(vx+int(20*multi),vy+int(30*multi))
    setheading(90)
    down()
    circle(int(10*multi))
    goto(vx+int(20*multi),vy+int(10*multi))
    circle(int(10*multi),-150)
    up()
    return 20*multi+5

def zero(vx: int, vy: int,multi=40):
    multi=multi/40
    goto(vx+20*multi,vy+30*multi)
    setheading(90)
    down()
    circle(10*multi,180)
    goto(vx,vy+10*multi)
    circle(10*multi,180)
    goto(vx+20*multi,vy+30*multi)
    up()
    return 20*multi+5
    #Tracer un trait en diagonale afin de le distinquer de O / 0

def degré(vx: int, vy: int,multi=40):
    multi=multi/40
    goto(vx+5*multi,vy+multi*30)
    down()
    circle(5*multi)
    up()
    return 10*multi+5
    
def tiret(vx: int, vy: int, derniercar="a", taille=40):
    if derniercar.isupper():
        vy+=10
    goto(vx,vy+10*taille/40)
    down()
    goto(vx+20*taille/40,vy+10*taille/40)
    up()
    return 20*taille/40+5

def copyrights(vx: int, vy: int,taille=40):
    setheading(0)
    multi=taille/30
    vx+=10
    goto(vx,vy)
    down()
    circle(10*multi)
    up()
    goto(vx+4*multi,vy+12*multi)
    down()
    setheading(90)
    circle(4*multi,180)
    goto(vx-4*multi,vy+7*multi)
    circle(4*multi,180)
    up()
    return 20*multi+5

def apostrophe(vx: int, vy: int,multi=40):
    multi/=40
    goto(vx+5*multi,vy+40*multi)
    down()
    goto(vx,vy+25*multi)
    up()
    return 6

def barre_oblique(vx: int,vy: int,multi=40):
    multi/=40
    goto(vx,vy)
    down()
    goto(vx+15*multi,vy+40*multi)
    up()
    return 20*multi+5

def point(vx: int, vy: int, multi=40):
    goto(vx,vy)
    down()
    dot(2)
    up()
    return 10*multi/40
    
def deux_points(vx: int,vy: int, multi=40):
    point(vx,vy)
    point(vx,vy+20*multi/40)
    return 5*multi/40

def virgule(vx: int,vy: int, multi=40):
    multi/=40
    goto(vx+5*multi, vy+5*multi)
    down()
    goto(vx, vy-5*multi)
    up()
    return 10*multi

def point_virgule(vx: int,vy: int, multi=40):
    multi/=40
    point(vx,vy+20*multi/40,multi)
    virgule(vx,vy,multi)
    return 10*multi

def taille_phrase(phrase="", multi=40):
    taille=0.0
    caractères_fins={"1":10, "°":10, "'":1, ".":10, ",":10, ":":5,"c":17, "i":1, "j":5, "k":10, "l":1, "r":10, "s":10, "t":15, "v":10, "w":10, "x":10,"z":10}
    for element in phrase:
        if element==" ":
            taille+=10*multi/40
        else:
            try:
                taille+=caractères_fins[element]*multi/40+5
            except KeyError:
                taille+=20*multi/40+5
    return taille 
# Penser à faire varier la taille du bordel quand j'aurais du temps à perdre.    
# Penser à faire la même avec des minuscules. Ça peut être long, je sais

def écriture(vx: int,vy: int,phrase="",multi=40, centrage=False, changeur_de_multi=()):
    caractères_spéciaux={"0":"zero", "1":"un", "2":"deux", "3":"trois", "4":"quatre", "5":"cinq", "6":"six", "7":"sept", "8":"huit", "9":"neuf", "°":"degré", "C":"C", "-":"tiret", "©":"copyrights", "'":"apostrophe", "/":"barre_oblique", ".":"point", ":":"deux_points", ",":"virgule", "ê":"e_circonflexe", "â":"a_circonflexe", "î":"i_circonflexe", "û":"u_circonflexe", "ô":"o_circonflexe", "à":"a_grave","è":"e_grave","ù":"u_grave","é":"e_aigu"}
    if centrage==False:
        x_mod=vx-taille_phrase(phrase)/2
    else:
        x_mod=vx
    for vi in range(len(phrase)):
        if len(changeur_de_multi)!=0 and changeur_de_multi[0]==vi:
            multi=changeur_de_multi[1]
        setheading(0)
        if phrase[vi]=="-" :
            if phrase[vi-1]==" " and vi>2:
                x_mod+=tiret(x_mod,vy,phrase[vi-2],multi)
            else:
                x_mod+=tiret(x_mod,vy,phrase[vi-1],multi)
        elif phrase[vi] in "1234567890-°©/'./:,âêûîôéèàù":
            x_mod+=globals()[caractères_spéciaux[phrase[vi]]](x_mod,vy,multi)
        elif phrase[vi]!=" " and phrase[vi] not in "}?;+=)!({":
            x_mod+=globals()[phrase[vi]](x_mod,vy,multi)
        else:
            x_mod+=10*(multi/40)

def ecriture_sur_pluiseurs_lignes(phrase : str, multi : int):
    #Recherche d'espaces
    p=[]
    ai=0
    for i in range(len(phrase)):
        if phrase[i]==" ":
            p.append(phrase[ai:i])
            ai=i+1
    p.append(phrase[ai:])

    #Recherche des additions de mots:
    p_ecrivable=[]
    extrait=""
    for element in p:
        if taille_phrase(extrait)+10+taille_phrase(element)>1365:
            p_ecrivable.append(extrait)
            extrait=element
        else:
            extrait=extrait+" "+element

    #écriture
    for j in range(len(p_ecrivable)):
        écriture(-660, 380-50*j, p_ecrivable[j],multi, True)
