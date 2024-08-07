from turtle import *

def A(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy)
    down()
    goto(vx+10*multi,vy+40*multi)
    goto(vx+20*multi,vy)
    up()
    goto(vx+(10+300/40)*multi,vy+10*multi)
    down()
    goto(vx+(10-300/40)*multi,vy+10*multi)
    up()
    return 20*multi+5
    
def B(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy)
    setheading(180)
    down()
    goto(vx,vy+40*multi)
    goto(vx+10*multi,vy+40*multi)
    circle(10*multi,-180)
    goto(vx+7*multi,vy+20*multi)
    goto(vx+10*multi,vy+20*multi)
    setheading(180)
    circle(10*multi,-180)
    goto(vx,vy)
    up()
    return 20*multi+5
    
def C(vx,vy,multi=40):
    multi=multi/40
    goto(vx+20*multi,vy+30*multi)
    setheading(90)
    down()
    circle(10*multi,180)
    forward(20*multi)
    circle(10*multi,180)
    up()
    return 20*multi+5
    
def D(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy)
    setheading(180)
    down()
    goto(vx,vy+40*multi)
    goto(vx+3*multi,vy+40*multi)
    circle(20*multi,-180)
    goto(vx,vy)
    up()
    return 20*multi+5
    
def E(vx,vy,multi=40):
    multi=multi/40
    goto(vx+20*multi,vy)
    down()
    goto(vx,vy)
    goto(vx,vy+40*multi)
    goto(vx+20*multi,vy+40*multi)
    up()
    goto(vx+10*multi,vy+20*multi)
    down()
    goto(vx,vy+20*multi)
    up()
    return 20*multi+5
    
def F(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy)
    down()
    goto(vx,vy+40*multi)
    goto(vx+20*multi,vy+40*multi)
    up()
    goto(vx+10*multi,vy+20*multi)
    down()
    goto(vx,vy+20*multi)
    up()
    return 20*multi+5

def G(vx,vy,multi=40):
    multi=multi/40
    C(vx,vy,multi*40)
    down()
    goto(vx+20*multi,vy)
    up()
    goto(vx+20*multi,vy+10*multi)
    down()
    goto(vx+10*multi,vy+10*multi)
    up()
    return 20*multi+5
    
def H(vx,vy,multi=40):
    multi=multi/40
    for vi in range(0,21,20):
        goto(vx+vi*multi,vy)
        down()
        goto(vx+vi*multi,vy+40*multi)
        up()
    goto(vx,vy+20*multi)
    down()
    goto(vx+20*multi,vy+20*multi)
    up()
    return 20*multi+5
    
def I(vx,vy,multi=40):
    multi=multi/40
    for vi in range(0,41,40):
        goto(vx+20*multi,vy+vi*multi)
        down()
        goto(vx,vy+vi*multi)
        up()
    goto(vx+10*multi,vy+40*multi)
    down()
    goto(vx+10*multi,vy)
    up()
    return 20*multi+5
    
def J(vx,vy,multi=40):
    multi=multi/40
    goto(vx+10*multi,vy+40*multi)
    setheading(90)
    down()
    goto(vx+20*multi,vy+40*multi)
    goto(vx+20*multi,vy+10*multi)
    circle(10*multi,-180)
    up()
    return 20*multi+5

def K(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy)
    down()
    goto(vx,vy+40*multi)
    up()
    goto(vx,vy+10*multi)
    down()
    goto(vx+20*multi,vy+40*multi)
    up()
    goto(vx+8*multi,vy+20*multi)
    down()
    goto(vx+20*multi,vy)
    up()
    return 20*multi+5
    
def L(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy+40*multi)
    down()
    goto(vx,vy)
    goto(vx+20*multi,vy)
    up()
    return 20*multi+5
    
def M(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy)
    down()
    goto(vx,vy+40*multi)
    goto(vx+10*multi,vy+25*multi)
    goto(vx+20*multi,vy+40*multi)
    goto(vx+20*multi,vy)
    up()
    return 20*multi+5

def N(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy)
    down()
    goto(vx,vy+40*multi)
    goto(vx+20*multi,vy)
    goto(vx+20*multi,vy+40*multi)
    up()
    return 20*multi+5
    
def O(vx,vy,multi=40):
    multi=multi/40
    goto(vx+20*multi,vy+30*multi)
    setheading(90)
    down()
    circle(10*multi,180)
    forward(20*multi)
    circle(10*multi,180)
    forward(20*multi)
    up()
    return 20*multi+5
    
def P(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy)
    down()
    goto(vx,vy+40*multi)
    goto(vx+10*multi,vy+40*multi)
    setheading(180)
    circle(10*multi,-180)
    goto(vx,vy+20*multi)
    up()
    return 20*multi+5
    
def Q(vx,vy,multi=40):
    multi=multi/40
    O(vx,vy,multi*40)
    goto(vx+10*multi,vy+9*multi)
    down()
    goto(vx+20*multi,vy)
    up()
    return 20*multi+5
    
def R(vx,vy,multi=40):
    multi=multi/40
    P(vx,vy,multi*40)
    goto(vx+7*multi,vy+20*multi)
    down()
    goto(vx+20*multi,vy)
    up()
    return 20*multi+5
    
def S(vx,vy,multi=40):
    multi=multi/40
    goto(vx+20*multi,vy+30*multi)
    down()
    setheading(90)
    circle(10*multi,270)
    setheading(180)
    circle(10*multi,-270)
    up()
    return 20*multi+5

def T(vx,vy,multi=40):
    multi=multi/40
    goto(vx+10*multi,vy)
    down()
    goto(vx+10*multi,vy+40*multi)
    up()
    goto(vx-2*multi,vy+40*multi)
    down()
    goto(vx+22*multi,vy+40*multi)
    up()
    return 20*multi+5
    
    
def U(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy+40*multi)
    down()
    goto(vx,vy+10*multi)
    setheading(270)
    circle(10*multi,180)
    goto(vx+20*multi,vy+40*multi)
    up()
    return 20*multi+5
    
def V(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy+40*multi)
    down()
    goto(vx+10*multi,vy)
    goto(vx+20*multi,vy+40*multi)
    up()
    return 20*multi+5
    
def W(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy+40*multi)
    down()
    goto(vx+5*multi,vy)
    goto(vx+10*multi,vy+10*multi*2)
    goto(vx+15*multi,vy)
    goto(vx+20*multi,vy+40*multi)
    up()
    return 20*multi+5
    
    
def X(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy)
    down()
    goto(vx+20*multi,vy+40*multi)
    up()
    goto(vx+20*multi,vy)
    down()
    goto(vx,vy+40*multi)
    up()
    return 20*multi+5

def Y(vx,vy,multi=40):
    multi=multi/40
    goto(vx+10*multi,vy)
    down()
    goto(vx+10*multi,vy+20*multi)
    goto(vx,vy+40*multi)
    up()
    goto(vx+10*multi,vy+20*multi)
    down()
    goto(vx+20*multi,vy+40*multi)
    up()
    return 20*multi+5

def Z(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy+40*multi)
    down()
    goto(vx+20*multi,vy+40*multi)
    goto(vx,vy)
    goto(vx+20*multi,vy)
    up()
    return 20*multi+5

#Les minuscules ont la même largeur que les majuscules mais font 30pvx au lieu de 40pvx
    
def a(vx,vy,multi=40):
    vx-=4
    multi=multi/40
    goto(vx+20*multi,vy+10*multi)
    down()
    setheading(80)
    circle(8*multi,140)
    up()
    goto(vx+20*multi,vy+10*multi)
    down()
    goto(vx+10*multi,vy+10*multi)
    setheading(180)
    circle(5*multi,180)
    goto(vx+20*multi,vy)
    goto(vx+20*multi,vy+10*multi)
    up()
    return 16*multi+5

def b(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy)
    down()
    setheading(270)
    goto(vx,vy+10*multi)
    circle(10*multi)
    goto(vx,vy+30*multi)
    up()
    return 20*multi+5

def c(vx,vy,multi=40):
    multi=multi/40
    goto(vx+10*multi+(10*multi*3**0.5/2),vy+10*multi+(10*multi*1/2))
    down()
    setheading(115)
    circle(10*multi,300)
    up()
    return 17*multi+5
    
    
def d(vx,vy,multi=40):
    multi=multi/40
    goto(vx+20*multi,vy)
    down()
    setheading(90)
    goto(vx+20*multi,vy+10*multi)
    circle(10*multi)
    goto(vx+20*multi,vy+30*multi)
    up()
    return 20*multi+5
    
def e(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy+10*multi)
    down()
    goto(vx+20*multi,vy+10*multi)
    setheading(90)
    circle(10*multi,330)
    up()
    goto(vx+20*multi,vy+10*multi)
    down()
    goto(vx,vy+10*multi)
    up()
    return 20*multi+5
    
    
def f(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy)
    down()
    goto(vx,vy+11*multi)
    goto(vx+10*multi,vy+11*multi)
    goto(vx,vy+11*multi)
    goto(vx,vy+20*multi)
    setheading(270)
    circle(10*multi,-180)
    up()
    return 20*multi+5
    
def g(vx,vy,multi=40):
    multi=multi/40
    goto(vx+10*multi,vy+10*multi)
    o(vx,vy,multi*40)
    goto(vx+20*multi,vy+20*multi)
    down()
    goto(vx+20*multi,vy)
    circle(10*multi,-170)
    up()
    return 20*multi+5
    
def h(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy+40*multi)
    down()
    goto(vx,vy)
    goto(vx,vy+10*multi)
    setheading(270)
    circle(10*multi,-180)
    goto(vx+20*multi,vy)
    up()
    return 20*multi+5
    
def i(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy)
    down()
    goto(vx,vy+20*multi)
    up()
    goto(vx,vy+30*multi)
    down()
    dot(2, "black")
    up()
    return 6

def j(vx,vy,multi=40):
    multi=multi/40
    goto(vx+5*multi,vy+20*multi)
    down()
    goto(vx+5*multi,vy-5*multi)
    setheading(90)
    circle(5*multi,-180)
    up()
    goto(vx+5*multi,vy+30*multi)
    dot(2, "black")
    return 5*multi+5
    
def k(vx,vy,multi=40):
    multi=multi/40
    K(vx,vy,20*multi)
    goto(vx,vy)
    down()
    goto(vx,vy+30*multi)
    up()
    return 10*multi+5
    
def l(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy)
    down()
    goto(vx,vy+30*multi)
    up()
    return 6

def m(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy)
    down()
    goto(vx,vy+20*multi)
    for vi in range(1,3):
        goto((vx+10*multi*(vi-1)),vy+15*multi)
        setheading(270)
        circle(5*multi,-180)
        goto(vx+10*vi*multi,vy)
    up()
    return 20*multi+5

def n(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy)
    down()
    goto(vx,vy+20*multi)
    goto(vx,vy+10*multi)
    setheading(270)
    circle(10*multi,-180)
    goto(vx+20*multi,vy)
    up()
    return 20*multi+5
    
def o(vx,vy,multi=40):
    multi=multi/40
    goto(vx+20*multi,vy+10*multi)
    setheading(90)
    down()
    circle(10*multi)
    up()
    return 20*multi+5
    
def p(vx,vy,multi=40):
    multi=multi/40
    o(vx,vy,multi*40)
    goto(vx,vy+15*multi)
    down()
    goto(vx,vy-10*multi)
    up()
    return 20*multi+5
    
def q(vx,vy,multi=40):
    multi=multi/40
    o(vx,vy,multi*40)
    goto(vx+20*multi,vy+15*multi)
    down()
    goto(vx+20*multi,vy-10*multi)
    up()
    return 20*multi+5


def r(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy)
    down()
    goto(vx,vy+20*multi)
    goto(vx,vy+10*multi)
    setheading(270)
    circle(10*multi,-115)
    up()
    return 10*multi+5
    
def s(vx,vy,multi=40):
    S(vx,vy,20*multi/40)
    return 10*multi/40+5
    
def t(vx,vy,multi=40):
    multi=multi/40
    goto(vx+5*multi,vy+30*multi)
    down()
    goto(vx+5*multi,vy+10*multi)
    setheading(270)
    circle(10*multi,90)
    up()
    goto(vx,vy+20*multi)
    down()
    goto(vx+15*multi,vy+20*multi)
    up()
    return 15*multi+5

def u(vx,vy,multi=40):
    multi=multi/40
    vy2=vy+20*multi
    goto(vx,vy2)
    down()
    goto(vx,vy+10*multi)
    setheading(270)
    circle(10*multi,180)
    goto(vx+20*multi,vy+20*multi)
    goto(vx+20*multi,vy)
    up()
    return 20*multi+5
    
    
def v(vx,vy,multi=40):
    V(vx,vy,20*multi/40)
    return 10*multi/40+5
    
def w(vx,vy,multi=40):
    W(vx,vy,20*multi/40)
    return 10*multi/40+5
    
def x(vx,vy,multi=40):
    X(vx,vy,20*multi/40)
    return 10*multi/40+5
    
def y(vx,vy,multi=40):
    multi=multi/40
    goto(vx,vy+20*multi)
    down()
    goto(vx+10*multi,vy)
    goto(vx+20*multi,vy+20*multi)
    goto(vx+5*multi,vy-10*multi)
    up()
    return 20*multi+5
    
def z(vx,vy,multi=40):
    Z(vx,vy,20*multi/40)
    return 10*multi/40+5

### Accents et lettres accentuées ###

def circonflexe(vx:int, vy:int, multi=40):
    multi/=40
    goto(vx,vy)
    down()
    goto(vx+10*multi,vy+10*multi)
    goto(vx+20*multi,vy)
    up()
    
def grave(vx:int, vy:int, multi=40):
    goto(vx+5*multi/40,vy+15*multi/40)
    down()
    goto(vx+15*multi/40,vy+5*multi/40)
    up()
    
def aigu(vx:int, vy:int, multi=40):
    goto(vx+2*multi/40,vy)
    down()
    goto(vx+17*multi/40,vy+10*multi/40)
    up()
#################################  
def e_circonflexe(vx,vy,multi=40):
    aj=e(vx,vy,multi=40)
    circonflexe(vx,vy+20*multi/40,multi=40)
    return aj

def a_circonflexe(vx,vy,multi=40):
    aj=a(vx,vy,multi=40)
    circonflexe(vx,vy+20*multi/40,multi=40)
    return aj

def o_circonflexe(vx,vy,multi=40):
    aj=o(vx,vy,multi=40)
    circonflexe(vx,vy+20*multi/40,multi=40)
    return aj

def u_circonflexe(vx,vy,multi=40):
    aj=u(vx,vy,multi=40)
    circonflexe(vx,vy+20*multi/40,multi=40)
    return aj

def i_circonflexe(vx,vy,multi=40):
    aj=i(vx,vy,multi=40)
    circonflexe(vx-10.5*multi/40,vy+20*multi/40,multi=40)
    return aj
##########################################
def e_aigu(vx,vy,multi=40):
    aj=e(vx,vy,multi=40)
    aigu(vx,vy+20*multi/40,multi=40)
    return aj

def a_aigu(vx,vy,multi=40):
    aj=a(vx,vy,multi=40)
    aigu(vx,vy+20*multi/40,multi=40)
    return aj

def o_aigu(vx,vy,multi=40):
    aj=o(vx,vy,multi=40)
    aigu(vx,vy+20*multi/40,multi=40)
    return aj

def i_aigu(vx,vy,multi=40):
    aj=i(vx,vy,multi=40)
    aigu(vx-10.5*multi/40,vy+20*multi/40,multi=40)
    return aj
##########################################
def e_grave(vx,vy,multi=40):
    aj=e(vx,vy,multi=40)
    grave(vx,vy+20*multi/40,multi=40)
    return aj

def a_grave(vx,vy,multi=40):
    aj=a(vx,vy,multi=40)
    grave(vx,vy+20*multi/40,multi=40)
    return aj

def o_grave(vx,vy,multi=40):
    aj=o(vx,vy,multi=40)
    grave(vx,vy+20*multi/40,multi=40)
    return aj

def i_grave(vx,vy,multi=40):
    aj=i(vx,vy,multi=40)
    grave(vx,vy+20*multi/40,multi=40)
    return aj

def u_grave(vx,vy,multi=40):
    aj=u(vx,vy,multi=40)
    grave(vx-10.5*multi/40,vy+20*multi/40,multi=40)
    return aj