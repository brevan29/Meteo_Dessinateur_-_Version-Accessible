from turtle import *
from random import randint
from datetime import datetime
from nombres import *
from tkinter import *
from tkinter import ttk, filedialog, messagebox
# from METAR import recherche
# © Brévan Météo - 2023-.
# © Brévan HAMEL
# Version 2.5.9

speed(200)
setup(1439,846,0,0)
ht()
up()

title("Brévan Météo 2.5.9 - Dessin")
pensize(2)
possibilités=[" Soleil"," Ciel Voilé"," Éclaircies"," Nuages"," Averse"," Pluie"," Orage"," Neige"," Brouillard"]
prévisions=[]
prim=Tk()
passage=False

def Variation_gris(mode=1.5):
    if mode==3:
        couleur=str(hex(randint(16,100)))[2:]
    else:
        couleur=str(hex(randint(150,200)))[2:]
    return "#"+3*couleur 
 
def vent(x,y,vitesse=0):
    pensize(2)
    color("black")
    y-=35
    goto(x,y-20)
    down()
    goto(x,y+80)
    up()
    pensize(10)
    color("red")
    for vi in range(5):
        goto(x+4*vi*5,y+60+(20-4*vi))
        down()
        goto(x+4*vi*5,y+60-(20-4*vi))
        up()
    #écriture de la vitesse.
    pensize(2)
    écriture(x+60,y-70,str(vitesse)+"km/h")
    pensize(8)

def soleil(x,y):
    color("#FD9230")
    a=randint(0,89)
    for rayon in range (0,360,60):
        goto(x,y-20)
        setheading(rayon+a)
        forward(50)
        down()
        forward(35)
        up()
    setheading(rayon)
    color("#FFD800")
    goto(x-35,y-40)
    begin_fill()
    down()
    circle(40)
    up()
    end_fill()
        
def nuages(vx,vy,mode=1.5):
    vy-=90
    if mode==1:
        nbr_nua=randint(7,13)
    else:
        nbr_nua=10
    vx-=(nbr_nua*14)/2
    setheading(0)
    goto(vx,vy)
    for vi in range(nbr_nua):
        gris=Variation_gris(mode)
        color(gris) 
        begin_fill()
        down()
        circle(randint(int(15*mode),30+int(10*mode)))
        end_fill()
        up()
        goto(vx+(vi+1)*14,vy)
    up()
    return vi
        
def éclaircies(x,y):
    soleil(x,y)
    nuages(x+25,y-10,1)
    
def pluie(x,y,mode="pl"):
    y=y-90
    if mode=="av":
        gouttes=nuages(x+25,y+90,1)
        x+=25
        y+=15
    else:
        gouttes=nuages(x,y+90,1.5)
    if gouttes>6:
        x-=gouttes*8+5
    else:
        x-=60
    goto(x,y)
    color("blue")
    setheading(250)
    for vg in range((gouttes-1)):
        down() 
        forward(33)
        up()
        goto(x+vg*20,y)
        
def geld():
    global opencours
    opencours.set('Gel en cours de dessin')
    flocon(-590,300,20)
    écriture(-670,230,"Risque de", 30, True)
    écriture(-620,190,"gel", 30, True)
    opencours.set('Gel dessiné, vous pouvez continuer')

def gelad():
    global opencours
    opencours.set('Gel en cours de dessin')
    flocon(-590,-60,20)
    écriture(-670,-130,"Risque de",30, True)
    écriture(-620,-170,"gel", 30, True)
    opencours.set('Gel dessiné, vous pouvez continuer')
    
def averse(x,y):
    soleil(x,y)
    pluie(x+10,y-5,'av')
    
def orage(vx,vy):
    if vy>100:
        vy+=15
    else:
        vy+=25
    setheading(0)
    goto(vx,vy)
    nuages(vx,vy,3)
    # éclair
    up()
    pensize(15)
    pencolor("#FAD30B")
    vx,vy=vx-15,vy-90
    goto(vx,vy)
    down()
    goto(vx-10,vy-40)
    goto(vx+10,vy-40)
    goto(vx,vy-80)
    pensize(8)
    up()

def brouillard(vx,vy):
    setheading(0)
    nuages(vx,vy,2)
    color(Variation_gris())
    goto(vx,vy-20)
    pensize(5)
    vx-=80
    vy-=80
    va=randint(0,1)
    for wi in range(3):
        goto(vx-(-1)**(wi+va)*20,vy-20-20*wi)
        down()
        goto(vx+135-(-1)**(wi+va)*20,vy-20-20*wi)
        up()
        
    pensize(8)
    
def flocon(vx,vy,taille=40):
    pencolor("blue")
    for vi in range(0,180,60):
        goto(vx,vy)
        setheading(vi)
        down()
        forward(taille)
        forward(-2*taille)
        up()

def neige(x,y):
    y+=15
    setheading(0)
    goto(x,y)
    vi=nuages(x,y,2)
    y-=90
    x-=70
    goto(x+(vi+1)*14,y)
    color("blue")
    pensize(5)
    lim=(0,4)
    for vh in range(1,3):
        for vj in range(lim[1]):
            flocon(x+vj*35+lim[0],y-25*vh,10)
        lim=(18,3)
    color("black")
    pensize(8)

def Ciel_voile(vx,vy):
    soleil(vx,vy)
    color(Variation_gris())
    pensize(8)
    va=randint(0,1)
    vx-=3
    for wi in range(3):
        goto(vx-(-1)**(wi+va)*20,vy-20-20*wi)
        down()
        goto(vx+135-(-1)**(wi+va)*20,vy-20-20*wi)
        up()

def jour_le_jour():
    limite={"01":31, "02":28, "03":31, "04":30, "05":31, "06":30, "07":31, "08":31, "09":30, "10":31, "11":30, "12":31}
    date=str(datetime.now())[:10]
    if p1.get()==False and ajd_dm.get()!="Demain / Après-Demain":
        date=" - "+str(date[-2:])+"/"+date[5:7]+"/"+date[:4]
    elif int(date[-2:])==limite[date[5:7]]:
        if date[5:7]=='12':
            date=" - 01/01/"+str(int(date[:4])+1)
        elif int(date[5:7])<9:
            date=" - 01/0"+str(int(date[5:7])+1)+"/"+date[:4]
        else:
            date=" - 01/"+str(int(date[5:7])+1)+"/"+date[:4]
    else:
        date=" - "+str(int(date[-2:])+1)+"/"+date[5:7]+"/"+date[:4]
    return date
   

def préparation():
    Couleur={"Vert":"#3CBB00", "Jaune":"#FFE000", "Orange":"#FFA600", "Rouge":"#E00000"}
    date=jour_le_jour()
    position_date=((150.0+taille_phrase(date,30))/2)
    if ajd_dm.get()=="Demain / Après-Demain":
        a_écrire=["DEMAIN"+date,"APRES-DEMAIN","© BREVAN "+str(datetime.now())[:4]]
        emplacements=[(-position_date,370,40,True,(7,30)),(0,25,40,False,()),(600,-400,30,False,())]
    else:
        a_écrire=["AUJOURD'HUI"+date,"DEMAIN","© BREVAN "+str(datetime.now())[:4]]
        emplacements=[(-position_date,370,40,True,(11,30)),(0,25,40,False,()),(600,-400,30,False,())]
    for i in range(3):
        if i==0:
            color(Couleur[vigidem.get()])
        elif i==1:
            color(Couleur[vigiadem.get()])
        else:
            color("Black")
        écriture(emplacements[i][0], emplacements[i][1], a_écrire[i], emplacements[i][2], emplacements[i][3], emplacements[i][4])                

def extraire():
    date=str(datetime.now())[:10]
    image = getcanvas()
    chemin = filedialog.asksaveasfilename(initialfile=date, defaultextension='.ps', title="qu'est-ce ça donne ?")
    print(chemin)
    image.postscript(file=chemin, colormode='color')
    opencours.set("Exportation réalisée")

def chgttaille():
    global tfen, passage
    if passage==False:
        prim.update()
        width=prim.winfo_width()
        height=prim.winfo_height()
        passage=not passage
        tfen=["579x485",str(width)+"x"+str(height),1]
    if tfen[2]==0:
        prim.geometry(tfen[1]) #Grande fenêtre
        tfen[2]=1
    elif tfen[2]==1: #Petite fenêtre
        prim.geometry(tfen[0])
        tfen[2]=0

def prévision(temps):
    vn=0
    pensize(2)
    #print(temps)
    préparation()
    
    if temps[-2]!="0" and temps[-2]!="":
        vent(575,300,temps[-2])
    if temps[-1]!="0" and temps[-1]!="":
        vent(575,-60,temps[-1])

    
    
    for vy in [300,-60]:
        for vx in [-415,0,426]:
            pensize(8)
            temps[vn]=temps[vn][1:]
            try:
                if temps[vn].lower()=="ciel voilé":
                    Ciel_voile(vx,vy)
                else:
                    globals()[temps[vn].lower()](vx,vy)
                pencolor("black")
                pensize(2)
                écriture(vx-len(temps[vn+6])/2*22.5,vy-200,temps[vn+6]+"°C",40,True)
            except KeyError:
                messagebox.showerror(title="Vous n'avez pas suivi mes instructions", message='Certaines cases sont restées vides.')
            except Exception as erreur:
                messagebox.showerror("Erreur non prévue",erreur+'\n Gardez cette erreur de coté et faites-moi part de cette erreur en me donnant le plus de détails possibles')
            vn+=1
    
    vn+=6
    écriture(-650,-400,"Source: "+temps[vn],int(taille.get()),True)
#prévision()
def tailleFen():
    width = prim.winfo_width() # Récupére la hauteur.
    height = prim.winfo_height() 
    print ( "width :" , width) # Affiche la largeur.
    print ( "height :" , height)

def Récupération():
    prevu=[temps1.get(),temps2.get(),temps3.get(),temps4.get(),temps5.get(),temps6.get(),temp1.get(),temp2.get(),temp3.get(),temp4.get(),temp5.get(),temp6.get(),source.get(), ventd.get(), ventad.get()]
    opencours.set("Dessin des prévisions en cours")
    prévision(prevu)
    opencours.set("Dessins réalisés")
    prevu=[temps1.set(''),temps2.set(''),temps3.set(''),temps4.set(''),temps5.set(''),temps6.set(''),temp1.set('0'),temp2.set('0'),temp3.set('0'),temp4.set('0'),temp5.set('0'),temp6.set('0'), source.delete(0,END)]  

def aide():
    global assistance
    assistance=Tk()
    txt=["Bienvenue dans la 2ème version du Brévan-Météo.","IMPORTANT : Ne jamais fermer la fenêtre Turtle (la grande fenêtre blanche) sous peine de devoir relancer l'application.",'Comment faire ?',' ',"1 . Récupération des prévisions\n    - Rentrer les prévisions avec les menus déroulants et les spinbox\n    - AUCUNE case des prévisions ne doit être vide sous peine d'obtenir une erreur et faire arrêter le dessin (vous devrez effacer et recommencer).\n    - Pour notifier la présence de gel appuyer sur le bouton et attendre de pouvoir lire 'Vous pouvez continuer'.\n    - Si vous modifiez la vigilance ou que vous mettez le vent, ils seront inclus avec la prévision. Si il n'y a pas de vent, cette case peut rester vide.\n    - La case vent démarre à 50km/h si jamais vous voulez vraiment notifier un vent inférieur à 50km/h, vous devez l'écrire directement.\n\n2 . Lancement du dessin\n    - Une fois toutes les informations rentrées, pour lancer le dessin appuyez sur le bouton 'Valider'.\n    - NE PAS appuyer sur les autres boutons sous peine d'exporter des esquisses incomplètes ou de dessiner des dessins moches ou incomplets.\n    - Notez que la fin du dessin effacera les prévisions dans les boites.\n\n3 . Exportation\n   - Une fois le dessin réalisé (vous le saurez grâce au message), vous pouvez exporter en appuyant sur le bouton éponyme.\nCela ouvrira une page pour savoir où vous voulez sauvegarder le fichier\n    - IMPORTANT : Le format du fichier enregistré est '.ps', format pas très imagé mais vous avez des lecteurs de fichier .ps\n qui permettent de les visualiser et de les exporter en fichier image classique.\n   - Si vous voulez recommencer votre dessin, apuyez sur 'Effacer', rentrez de nouveaux les prévisions et validez.\n   - SI vous appuyez sur effacer, il va continuer son dessin sans les traces qui ont été effacées\n\nEn bas de l'application de récupération des prévisions se trouve une liste dérouante et un bouton à cocher où c'est marqué 'Ajourd'hui c'est demain'.\nLaissez moi vous expliquer le fonctionnement:\n    - Si vous voulez dessiner les prévisions pour le lendemain et sur-lendemain :\n        - Si vous voulez que ce soit écrit Demain / Après-demain, mettez la liste déroulante sur cette valeur\n       - Si vous voulez que ce soit écrit 'Aujourd'hui / Demain', placez la liste déroulante sur cette valeur et ne cochez pas le bouton en dessous.\n    - Vous faites une prévision pour le jour même: Placez la liste déroulante sur 'Aujourd'hui / Demain' et cochez le bouton en dessous \n(le bouton sert en fait à savoir quel jour prendre suivant le cas de figure)",' ','Bonne navigation dans le Brévan Météo 2.0']
    assistance.title('Aide pour le Brévan Météo')
    for i in range(len(txt)):
        ttk.Label(assistance, text=txt[i], justify='left', anchor=NW).grid(row=i, padx=15)


def tkpres():
    global temp1, temp2, temp3, temp4, temp5, temp6, temps1, temps2, temps3, temps4, temps5, temps6, source, ventd, ventad, taille, vigidem, vigiadem, opencours, ajd_dm, VA, p1

    prim.title("Brévan Météo 2.5.9 -  Récupération des prévisions")
    
    p1=BooleanVar(prim)
    var1, var2, var3, var4, var5, var6 = StringVar(prim), StringVar(prim), StringVar(prim), StringVar(prim), StringVar(prim), StringVar(prim)
    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    
    ajd_dm=StringVar(prim)
    ttk.Label(prim, text="Veuillez rentrer les prévisions pour demain.", justify="center", anchor=CENTER).grid(columnspan=3, row=0, sticky="nsew")
    sec=ttk.Frame(prim)
    sec.grid(column=0, row=0)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    dm=ttk.Labelframe(sec, text="Prévisions pour demain")
    dm.grid(column=0, columnspan=3,row=1)


    ttk.Label(dm, text="Matin", font=("Ubuntu", 10)).grid(column=0, row=0, padx=5, pady=2)
    ttk.Label(dm, text="Après-midi", font=("Ubuntu", 10)).grid(column=1, row=0, padx=5, pady=2)
    ttk.Label(dm, text="Soir", font=("Ubuntu", 10)).grid(column=2, row=0, padx=5, pady=2)
    temps1=ttk.Combobox(dm, values=possibilités, width=10)
    temps2=ttk.Combobox(dm, values=possibilités, width=10)
    temps3=ttk.Combobox(dm, values=possibilités, width=10)
    temp1=ttk.Spinbox(dm, from_=-20, to=50, textvariable=var1, width=5)
    temp2=ttk.Spinbox(dm, from_=-20, to=50, textvariable=var2, width=5)
    temp3=ttk.Spinbox(dm, from_=-20, to=50, textvariable=var3, width=5)

    temps1.grid(column=0,row=1, padx=5, pady=1)
    temps2.grid(column=1,row=1, padx=5, pady=1)
    temps3.grid(column=2,row=1, padx=5, pady=1)
    temp1.grid(column=0,row=2, padx=5, pady=2)
    temp2.grid(column=1,row=2, padx=5, pady=2)
    temp3.grid(column=2,row=2, padx=5, pady=2)


    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    adm=ttk.Labelframe(sec, text="Prévisions pour après-demain")
    adm.grid(row=5, column=0, columnspan=3, padx=5, pady=10)
    
    ttk.Label(adm, text="Matin", font=("Ubuntu", 10)).grid(column=0, row=0, padx=5, pady=2)
    ttk.Label(adm, text="Après-midi", font=("Ubuntu", 10)).grid(column=1, row=0, padx=5, pady=2)
    ttk.Label(adm, text="Soir", font=("Ubuntu", 10)).grid(column=2, row=0, padx=5, pady=2)
    temps4=ttk.Combobox(adm, values=possibilités, width=10)
    temps5=ttk.Combobox(adm, values=possibilités, width=10)
    temps6=ttk.Combobox(adm, values=possibilités, width=10)
    temp4=ttk.Spinbox(adm, from_=-20, to=50, textvariable=var4, width=5)
    temp5=ttk.Spinbox(adm, from_=-20, to=50, textvariable=var5, width=5)
    temp6=ttk.Spinbox(adm, from_=-20, to=50, textvariable=var6, width=5)


    temps4.grid(column=0,row=1, padx=5, pady=1)
    temps5.grid(column=1,row=1, padx=5, pady=1)
    temps6.grid(column=2,row=1, padx=5, pady=1)
    temp4.grid(column=0,row=2, padx=5, pady=2)
    temp5.grid(column=1,row=2, padx=5, pady=2)
    temp6.grid(column=2,row=2, padx=5, pady=2)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    src=ttk.LabelFrame(sec, text="Source")
    src.grid(column=0, columnspan=3, row=9)

    ttk.Label(src, text="Source du jour:", anchor="e", font=("Ubuntu", 10)).grid(column=0, row=0, padx=20, pady=2)
    source=Entry(src, width=10)
    source.grid(column=1, row=0, sticky="nsew", padx=20, pady=2)
    taille=ttk.Spinbox(src, from_=20, to=50, width=4)
    taille.grid(column=2, row=0, sticky="w", padx=5, pady=2)
    taille.set(40)
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    plus=ttk.Labelframe(sec, text="Additionel")
    plus.grid(column=0, columnspan=3, row=10, padx=5, pady=5)
    vigidem=StringVar(plus)
    vigiadem=StringVar(plus)

    ttk.Label(plus, text="Gel à prévoir ?", font=("Ubuntu", 10)).grid(column=0, row=0, padx=5, pady=2)

    ttk.Button(plus, text="Demain", command=geld).grid(column=1,row=0, padx=5, pady=5)
    ttk.Button(plus, text="Après-demain", command=gelad).grid(column=2,row=0, padx=5, pady=5)

    ttk.Label(plus, text="Vent ? (Tel le gel)", font=("Ubuntu", 10)).grid(column=0, row=1, padx=5, pady=2)
    ventd=ttk.Spinbox(plus, from_=50, to=200, width=6)
    ventad=ttk.Spinbox(plus, from_=50, to=200, width=6)
    ventd.grid(column=1,row=1, padx=5, pady=5)
    ventad.grid(column=2, row=1, padx=5, pady=5)

    ttk.Label(plus, text="Vigilance", font=("Ubuntu", 10)).grid(column=0, row=3, padx=5, pady=2)
    dmv=ttk.OptionMenu(plus, vigidem, "Vert", "Vert", "Jaune","Orange","Rouge", direction="flush")
    admv=ttk.OptionMenu(plus, vigiadem, "Vert", "Vert", "Jaune","Orange","Rouge", direction="flush")
    dmv.grid(column=1, row=3, padx=5, pady=2)
    admv.grid(column=2, row=3, padx=5, pady=2)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    act=ttk.Labelframe(sec, text="Actions")
    act.grid(column=0, columnspan=3, row=15, padx=5, pady=5)
    ttk.Button(act, text="Valider",command=Récupération).grid(column=2,row=0, padx=10, pady=5)
    ttk.Button(act, text="Effacer", command=clear).grid(column=0,row=0, padx=10, pady=5)
    ttk.Button(act, text="Exporter", command=extraire).grid(column=1,row=0, padx=10, pady=5)
    ttk.Button(act, text="Aide", command=aide).grid(column=0, row=1, padx=10, pady=5)

    opencours=StringVar(prim)
    opencours.set(value="Veuillez rentrer les prévisions")
    oec=ttk.Label(act, textvariable=opencours) #Opération En Cours
    oec.grid(column=1, columnspan=2,row=1, padx=10, pady=5)
    ttk.OptionMenu(act, ajd_dm, "Demain / Après-Demain","Aujourd'hui / Demain","Demain / Après-Demain").grid(column=3, row=0, padx=20, pady=5)

    VA=ttk.Checkbutton(act, offvalue=False, onvalue=True, variable=p1, text="Aujourd'hui c'est Demain ?")
    VA.grid(column=3, row=1, padx=10, pady=5)
    prim.mainloop()

    

if __name__=="__main__":
    tkpres()